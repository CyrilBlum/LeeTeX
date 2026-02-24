import socket
import threading
import tkinter as tk
from tkinter import ttk
from queue import Queue
import time

# GUI setup
root = tk.Tk()
root.title("Chat Relay Server")
root.geometry("600x400")

# Create frame for title
title_frame = ttk.Frame(root)
title_frame.pack(padx="10", pady="10")
title_label = ttk.Label(title_frame, text="Verbundene Clients", font=("Arial", 14, "bold"))
title_label.pack()

# Create treeview for client statistics
tree_frame = ttk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True, padx="10", pady="10")

columns = ("Name", "Nachrichten gesendet", "Nachrichten empfangen")
tree = ttk.Treeview(tree_frame, columns=columns, height=15)

tree.column("#0", width=0, stretch=tk.NO)
tree.column("Name", width=150, anchor=tk.W)
tree.column("Nachrichten gesendet", width=150, anchor=tk.CENTER)
tree.column("Nachrichten empfangen", width=150, anchor=tk.CENTER)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Name", anchor=tk.W)
tree.heading("Nachrichten gesendet", text="Nachrichten gesendet", anchor=tk.CENTER)
tree.heading("Nachrichten empfangen", text="Nachrichten empfangen", anchor=tk.CENTER)

tree.pack(fill=tk.BOTH, expand=True)

# Add scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscroll=scrollbar.set)

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 12345))
server.listen()

clients = {}
client_stats = {}  # {name: {"socket": socket, "sent": int, "received": int}}
stats_lock = threading.Lock()
gui_queue = Queue()  # For thread-safe GUI updates

def update_gui_from_queue():
    """Process GUI updates from the queue"""
    try:
        while True:
            action, data = gui_queue.get_nowait()
            if action == "add":
                name = data
                tree.insert("", tk.END, values=(name, 0, 0))
            elif action == "update":
                name, sent, received = data
                # Find and update the item
                for item in tree.get_children():
                    if tree.item(item)["values"][0] == name:
                        tree.item(item, values=(name, sent, received))
                        break
            elif action == "remove":
                name = data
                for item in tree.get_children():
                    if tree.item(item)["values"][0] == name:
                        tree.delete(item)
                        break
    except:
        pass
    
    root.after(100, update_gui_from_queue)

def handle_client(client):
    sender_name = None
    try:
        while True:
            nachricht = client.recv(1024).decode()
            if not nachricht:
                break
            
            empfaenger, nachricht = nachricht.split(":", 1)
            sender_name = [name for name, cl in client_stats.items() if cl["socket"] == client]
            
            if sender_name:
                sender_name = sender_name[0]
                
                # Update sender's sent count
                with stats_lock:
                    if sender_name in client_stats:
                        client_stats[sender_name]["sent"] += 1
                        gui_queue.put(("update", (sender_name, client_stats[sender_name]["sent"], client_stats[sender_name]["received"])))
                
                # Send message to recipient
                if empfaenger in client_stats:
                    try:
                        client_stats[empfaenger]["socket"].send(f"{sender_name}: {nachricht}".encode())
                        # Update recipient's received count
                        with stats_lock:
                            client_stats[empfaenger]["received"] += 1
                            gui_queue.put(("update", (empfaenger, client_stats[empfaenger]["sent"], client_stats[empfaenger]["received"])))
                    except:
                        client.send(f"Fehler beim Senden an {empfaenger}.".encode())
                else:
                    client.send(f"Empfänger {empfaenger} nicht gefunden.".encode())
    except:
        pass
    
    # Cleanup
    if sender_name and sender_name in client_stats:
        with stats_lock:
            del client_stats[sender_name]
        gui_queue.put(("remove", sender_name))
        print(f"{sender_name} hat die Verbindung getrennt.")
    
    try:
        client.close()
    except:
        pass

def accept_clients():
    """Accept incoming client connections"""
    while True:
        try:
            client, addr = server.accept()
            name = client.recv(1024).decode()
            
            with stats_lock:
                client_stats[name] = {"socket": client, "sent": 0, "received": 0}
            
            gui_queue.put(("add", name))
            print(f"{name} hat sich verbunden.")
            
            threading.Thread(target=handle_client, args=(client,), daemon=True).start()
        except:
            break

# Start server in background thread
server_thread = threading.Thread(target=accept_clients, daemon=True)
server_thread.start()

# Start GUI update loop
update_gui_from_queue()

# Run GUI
root.mainloop()