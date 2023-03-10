import re
import tkinter as tk

subor = open(file="subor15.txt")

window = tk.Tk()
canvas = tk.Canvas(width = 500, height = 500)
canvas.pack()


lines = subor.readlines()
non=[x[:-1] for x in lines]


for count in range(0,len(lines)):
    shape = re.findall("[A-Z]", non[count])
    if shape == ["S"]:
        raw = re.findall("[0-9]+", non[count])
        x = int(raw[0])
        y = int(raw[1])
        s = int(raw[2])
        canvas.create_rectangle(x,y,x+s,y+s)
    elif shape == ["K"]:
        raw = re.findall("[0-9]+",non[count])
        x = int(raw[0])
        y = int(raw[1])
        r = int(raw[2])
        canvas.create_oval(x-r,y-r,x+r,y+r)
    else:
        raw = re.findall("[0-9]+",non[count])
        x1 = raw[0]
        y1 = raw[1]
        x2 = raw[2]
        y2 = raw[3]
        canvas.create_line(x1,y1,x2,y2)

window.mainloop()