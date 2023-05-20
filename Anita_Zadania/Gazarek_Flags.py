import tkinter as tk
import random
import math


def italy():
    for dot in range(dotnum):
        x, y = random.randint(0, 500), random.randint(0, 500)
        if x < 167:
            canvas.create_oval(x, y, x + 2, y + 2, fill="green", outline="green")
            canvas.update()
        elif 334 > x > 167:
            canvas.create_oval(x, y, x + 2, y + 2, fill="white", outline="white")
            canvas.update()
        elif x >= 334:
            canvas.create_oval(x, y, x + 2, y + 2, fill="red", outline="red")
            canvas.update()

def australia():
    for dot in range(dotnum):
        x, y = random.randint(0, 500), random.randint(0, 500)
        vector = [x-250,y-250]
        vector_length = math.sqrt(vector[0]**2 + vector[1]**2)

        if vector_length <= 88:
            canvas.create_oval(x, y, x + 2, y + 2, fill="yellow", outline="yellow")
            canvas.update()
        elif y > 250:
            canvas.create_oval(x, y, x + 2, y + 2, fill="red", outline="red")
            canvas.update()
        elif y < 250:
            canvas.create_oval(x, y, x + 2, y + 2, fill="black", outline="black")
            canvas.update()

def sweden():
    for dot in range(dotnum):
        x, y = random.randint(0, 500), random.randint(0, 500)
        if x < 175 and y < 225:
            canvas.create_oval(x, y, x + 2, y + 2, fill="blue", outline="blue")
            canvas.update()
        elif x < 175 and y > 275:
            canvas.create_oval(x, y, x + 2, y + 2, fill="blue", outline="blue")
            canvas.update()
        elif x > 225 and y < 225:
            canvas.create_oval(x, y, x + 2, y + 2, fill="blue", outline="blue")
            canvas.update()
        elif x > 225 and y > 275:
            canvas.create_oval(x, y, x + 2, y + 2, fill="blue", outline="blue")
            canvas.update()
        else:
            canvas.create_oval(x, y, x + 2, y + 2, fill="yellow", outline="yellow")
            canvas.update()

def czech():
        for dot in range(dotnum):
            x, y = random.randint(0, 500), random.randint(0, 500)
            perm_vector = [0,-250]
            temp_vector = [x-200,y-250]
            if x < 200:
                cos = (perm_vector[0]*temp_vector[0] + perm_vector[1] * temp_vector[1])/(math.sqrt(perm_vector[0]**2 + perm_vector[1]**2)*math.sqrt(temp_vector[0]**2 + temp_vector[1]**2))
                print(cos)
                if -1 <= cos <= 1:
                    angle = math.acos(cos) * (180/math.pi)
                print(angle)
                if 40 < angle < 140 :
                    canvas.create_oval(x, y, x + 2, y + 2, fill="blue", outline="blue")
                    canvas.update()
                elif y > 250:
                    canvas.create_oval(x, y, x + 2, y + 2, fill="red", outline="red")
                    canvas.update()
            elif y > 250:
                canvas.create_oval(x, y, x + 2, y + 2, fill="red", outline="red")
                canvas.update()

                
                    
window = tk.Tk()
canvas = tk.Canvas(width = 500, height = 500)
canvas.pack()

choice = int(input("Akú vlajku chceš?\n1.Taliánsko\n2.Stará Austrália\n3.Švédsko\n4.Česko\n"))
dotnum = int(input("Koľko chceš mať bodiek? "))


if choice == 1:
    italy()
elif choice == 2:
    australia()
elif choice == 3:
    sweden()
elif choice == 4:
    czech()



window.mainloop()