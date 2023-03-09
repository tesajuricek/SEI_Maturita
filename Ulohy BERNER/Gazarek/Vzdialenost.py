import tkinter as tk
import random
import math

window = tk.Tk()
canvas = tk.Canvas(width = 500, height = 500)
canvas.pack()

hlmesto = [random.randint(100,200),random.randint(100,200)]
mestecka = []
dedinky = []

canvas.create_oval(hlmesto,hlmesto[0]+20,hlmesto[1]+20, fill = "red")

for m in range(0,5):
    x,y = random.randint(14,286),random.randint(14,286)
    mestecka.append([x,y])
    canvas.create_oval(x,y,x+14,y+14, fill = "blue")
    canvas.create_text(x+20,y+20,text = "M"+str(m+1))

for d in range(0,10):
    x,y = random.randint(8,292),random.randint(8,292)
    dedinky.append([x,y])
    canvas.create_oval(x,y,x+8,y+8, fill = "green")
    canvas.create_text(x+18,y+18,text = "D"+str(d+1))

for x in range(0,len(mestecka)):
    canvas.create_line(hlmesto[0]+10,hlmesto[1]+10,mestecka[x][0]+7,mestecka[x][1]+7)
    length = math.sqrt(((mestecka[x][0]+7-hlmesto[0]+10)**2)+((mestecka[x][1]+7-hlmesto[1]+10)**2))
    canvas.create_text((mestecka[x][0] + length)/2, (mestecka[x][1]+length)/2, text = length)

for x in range(0,len(dedinky)):
    canvas.create_line(hlmesto[0]+10,hlmesto[1]+10,dedinky[x][0]+4,dedinky[x][1]+4)


window.mainloop()

