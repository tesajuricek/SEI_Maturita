import random
import tkinter as tk

coordinates = []
size = 20
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]


def create_point(event):
    x, y = event.x, event.y
    new_point = True
    for point in coordinates:
        if (point[0] - size <= x <= point[0] + size) and (point[1] - size <= y <= point[1] + size):
            canvas.create_oval(
                point[0] - size,
                point[1] - size,
                point[0] + size,
                point[1] + size,
                fill=random.choice(colors)
            )
            new_point = False
    if new_point:
        canvas.create_oval(x - size, y - size, x + size, y + size, fill="red")
        coordinates.append((x, y))


window = tk.Tk()
window.title("Create Point on Mouse Click")
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()
canvas.bind("<Button-1>", create_point)

window.mainloop()
