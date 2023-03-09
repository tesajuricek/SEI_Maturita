import tkinter as tk
import random

window = tk.Tk()
canvas = tk.Canvas(width = 1000, height = 1000)
canvas.pack()
colours = ["red","green","yellow","blue"]


for x in range(0,5):
    colour = random.choice(colours)
    canvas.create_rectangle(x*200 + 5,5,x*200 + 200,300, width=3)
    canvas.create_oval(x*200 + 10,10,x*200 + 70,70, fill = colour)
    canvas.create_oval(x*200+ 130,230,x*200+ 190,290, fill = colour)
    canvas.create_rectangle(x*200+ 25,115,x*200+ 175,185, fill = "black")
    canvas.create_text(x*200+ 100,150, text = "BILGYM", fill = colour, font = ("Comic Sans", "18", "bold"))

    number = str(random.randint(1,9))
    for y in range(0,2):
        canvas.create_text(x*200 + y*120 + 40, y*220 + 40, text = number, font = ("Comic Sans", "18", "bold"))


window.mainloop()