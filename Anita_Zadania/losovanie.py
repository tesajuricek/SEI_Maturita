import random
rozsah = 8
pocet = 5
tahy = []

while len(tahy) < pocet:
    t = random.randint(0, rozsah)
    if t not in tahy:
        tahy.append(t)

print(tahy)

from tkinter import *

size = (1000//pocet)

win=Tk()

# Set the size of the tkinter window
win.geometry("1000x1000")

# Create a canvas widget
canvas=Canvas(win, width=1000, height=1000)

x = 0
y = 5
y2 = 5 + size

for circle in range(pocet):
    # canvas.create_oval(x,y,x+size,y+size)
    # x += size
    canvas.create_oval((5+size)*circle,y,((5+size)*circle)+size,y2)

canvas.pack()



    

win.mainloop()