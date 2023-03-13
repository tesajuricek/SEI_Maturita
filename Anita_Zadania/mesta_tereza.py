import tkinter as tk
import random
import math

w = tk.Tk()
c = tk.Canvas(w, width=400, height=400)
coords = []

center = c.create_oval(145,145,155,155,fill="white")

for i in range(5):
    x = random.randint(5,295)
    y = random.randint(5,295)
    dist = math.sqrt((150-x)**2+(150-y)**2)
    label = c.create_text(x+13,y+13,text="M"+str(i+1)+":"+str(int(dist)))
    d = c.create_oval(x,y,x+4,y+4,fill="white")
    l = c.create_line(x+2,y+2,150,150)
    coord = [(x+2),(y+2)]
    coords.append(coord)

d_coords = []
for i in range(10):
    x = random.randint(5,295)
    y = random.randint(5,295)
    dist = math.sqrt((150-x)**2+(150-y)**2)
    label = c.create_text(x+13,y+13,text="D"+str(i+1)+":"+str(int(dist)))
    d = c.create_oval(x,y,x+4,y+4,fill="green")
    l = c.create_line(x+2,y+2,150,150)
    coord = [(x+2),(y+2)]
    d_coords.append(coord)


print(coords)
list_distance = []
for x in coords:
    print(x)
    dist = math.sqrt((150-int(x[0]))**2+((y+(150-int(x[1])))**2))
    list_distance.append(dist)
    print(dist)    

max_coord = list_distance.index(max(list_distance))

bold = c.create_line(coords[max_coord][0],coords[max_coord][1],150,150, fill="red")    

c.pack()
w.mainloop()