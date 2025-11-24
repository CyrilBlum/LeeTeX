import tkinter as tk

CELL_SIZE = 100
GRID_SIZE = 3


def draw_grid(canvas):
    for i in range(1, GRID_SIZE):
        # Vertical lines
        canvas.create_line(
            i * CELL_SIZE, 0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE, width=5, fill="gray"
        )
        # Horizontal lines
        canvas.create_line(
            0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE, i * CELL_SIZE, width=5, fill="gray"
        )


def handle_click(event):
    x = event.x // CELL_SIZE
    y = event.y // CELL_SIZE
    cx = x * CELL_SIZE + CELL_SIZE // 2
    cy = y * CELL_SIZE + CELL_SIZE // 2

    if event.num == 1:  # Left mouse button
        # Draw blue circle
        canvas.create_oval(cx - 45, cy - 45, cx + 45, cy + 45, outline="blue", width=5)
    else:  # Other mouse button
        # Draw red cross
        canvas.create_line(cx - 45, cy - 45, cx + 45, cy + 45, fill="red", width=5)
        canvas.create_line(cx - 45, cy + 45, cx + 45, cy - 45, fill="red", width=5)


root = tk.Tk()
root.title("Tic Tac Toe")

canvas = tk.Canvas(
    root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white"
)
canvas.pack()

draw_grid(canvas)
canvas.bind("<Button-1>", handle_click)  # Left click
canvas.bind("<Button-3>", handle_click)  # Right click

root.mainloop()
