import tkinter as tk
import random as rand
import math

window = tk.Tk()
canvas = tk.Canvas(width=600,height=600)

capital = [rand.randint(200,400),rand.randint(200,400)]
towns = []
vilgs = []

canvas.create_oval(capital[0]-10,capital[1]-10,capital[0]+10,capital[1]+10,fill='red')

for i in range(5):
    x,y = rand.randint(20,580),rand.randint(20,580)
    towns.append([x,y])
    canvas.create_oval(x-7,y-7,x+7,y+7,fill='blue')
    canvas.create_text(x,y+11,text='M'+str(i+1))

for i in range(10):
    x,y = rand.randint(20,580),rand.randint(20,580)
    vilgs.append([x,y])
    canvas.create_oval(x-4,y-4,x+4,y+4,fill='green')
    canvas.create_text(x,y+8,text='D'+str(i+1))

lengths=[[],[]]

for i in range(len(towns)):
    canvas.create_line(capital[0],capital[1],towns[i][0],towns[i][1])
    length = int(math.sqrt((capital[0]-towns[i][0])**2+(capital[1]-towns[i][1])**2))
    lengths[0].append(length)
    canvas.create_text(capital[0]-(capital[0]-towns[i][0])/2,capital[1]-(capital[1]-towns[i][1])/2,text=str(length),fill='blue')

for i in range(len(vilgs)):
    canvas.create_line(capital[0],capital[1],vilgs[i][0],vilgs[i][1])
    length = int(math.sqrt((capital[0] - vilgs[i][0]) ** 2 + (capital[1] - vilgs[i][1]) ** 2))
    lengths[1].append(length)
    canvas.create_text(capital[0] - (capital[0] - vilgs[i][0]) / 2, capital[1] - (capital[1] - vilgs[i][1]) / 2,text=str(length), fill='green')

canvas.pack()
window.mainloop()