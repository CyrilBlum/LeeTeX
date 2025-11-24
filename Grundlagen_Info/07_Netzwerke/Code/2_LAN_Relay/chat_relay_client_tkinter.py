import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

SERVER_HOST = "192.168.1.23"  # anpassen
SERVER_PORT = 5000


class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")

        # Rahmen oben: Username + Connect
        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)

        tk.Label(top_frame, text="Benutzername:").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(top_frame, width=15)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        self.connect_button = tk.Button(
            top_frame, text="Verbinden", command=self.connect
        )
        self.connect_button.pack(side=tk.LEFT)

        # Chat-Fenster
        self.chat_box = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED
        )
        self.chat_box.pack(padx=10, pady=10)

        # Nachrichteneingabe
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(pady=5)

        self.msg_entry = tk.Entry(bottom_frame, width=50)
        self.msg_entry.pack(side=tk.LEFT, padx=5)
        self.msg_entry.bind("<Return>", self.send_message_event)

        self.send_button = tk.Button(
            bottom_frame, text="Senden", command=self.send_message
        )
        self.send_button.pack(side=tk.LEFT)

        self.socket = None
        self.connected = False

    def connect(self):
        if self.connected:
            return

        username = self.name_entry.get().strip()
        if not username:
            messagebox.showerror("Fehler", "Bitte einen Benutzernamen eingeben.")
            return

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((SERVER_HOST, SERVER_PORT))
        except Exception as e:
            messagebox.showerror("Verbindungsfehler", f"Konnte nicht verbinden:\n{e}")
            return

        # Username registrieren
        self.socket.send(f"/register {username}".encode())
        self.connected = True
        self.connect_button.config(state=tk.DISABLED)
        self.name_entry.config(state=tk.DISABLED)
        self.add_message("[Verbunden mit dem Server]\n")

        # Hintergrundthread zum Empfangen
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if not data:
                    break
                self.add_message(data.decode())
            except:
                break

        self.add_message("\n[Verbindung getrennt]\n")
        self.connected = False

    def add_message(self, msg):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, msg)
        self.chat_box.yview(tk.END)
        self.chat_box.config(state=tk.DISABLED)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        if not self.connected:
            messagebox.showerror(
                "Nicht verbunden", "Du bist nicht mit dem Server verbunden."
            )
            return

        msg = self.msg_entry.get().strip()
        if msg:
            try:
                self.socket.send(msg.encode())
            except:
                self.add_message("[Fehler beim Senden]\n")
            self.msg_entry.delete(0, tk.END)

    def close(self):
        try:
            if self.socket:
                self.socket.close()
        except:
            pass
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", client.close)
    root.mainloop()
