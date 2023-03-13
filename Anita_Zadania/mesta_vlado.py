import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(width=500, height=500)
canvas.pack()

hlavne_mesto = [random.randint(220, 280), random.randint(220, 280)]
mesta = []
dediny = []

for a in range(5):
    x, y = random.randint(14, 486), random.randint(14, 486)
    mesta.append([x, y])
    canvas.create_line(hlavne_mesto[0] + 10, hlavne_mesto[1] + 10, x + 7, y + 7)
    canvas.create_oval(x, y, x + 14, y + 14, fill="light blue")
    canvas.create_text(x + 20, y + 20, text="M" + str(a + 1))
for b in range(10):
    x, y = random.randint(14, 486), random.randint(14, 486)
    dediny.append([x, y])
    canvas.create_line(hlavne_mesto[0] + 10, hlavne_mesto[1] + 10, x + 4, y + 4)
    canvas.create_oval(x, y, x + 8, y + 8, fill="light green")
    canvas.create_text(x + 14, y + 14, text="D" + str(b + 1))
canvas.create_oval(hlavne_mesto[0], hlavne_mesto[1], hlavne_mesto[0] + 20, hlavne_mesto[1] + 20, fill="red")
root.mainloop()
