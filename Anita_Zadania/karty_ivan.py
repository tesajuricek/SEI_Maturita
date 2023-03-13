import tkinter as tk
import random as rand

window = tk.Tk()
canvas = tk.Canvas(width=1300, height=400)

mode = int(input('random 1,\nchoice 2,: '))
colors = ['red', 'blue', 'yellow', 'green']

for a in range(5):
    if mode == 1:
        color = rand.choice(colors)
        number = rand.randint(1, 9)
    else:
        color = colors[int(input('red 0,\nblue 1,\nyellow 2,\ngreen 3,: '))]
        number = int(input('number: '))
    x,y = 50+a*250,50
    canvas.create_rectangle(x, y, x+200, y+300, width=3)
    for b in range(2):
        canvas.create_oval(x+6+(b*128),y+6+(b*228),x+66+(b*128),y+66+(b*228),fill=color,width=0)
    canvas.create_rectangle(x+25,y+115,x+175,y+185,fill='black')
    for c in range(2):
        canvas.create_text(c*128+x+36,c*228+86,text=number,font=('Comic Sans','18','bold'))
    canvas.create_text(x+100,y+150,text='BILGYM',fill=color, font=('Comic Sans','18','bold'))

canvas.pack()
window.mainloop()
