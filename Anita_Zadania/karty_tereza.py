import random
import tkinter as tk

w = tk.Tk()
c = tk.Canvas(w, width=1200, height=300)
farby = ["red", "blue", "green", "yellow"]

for x in range(0,5):
    posun = 200*x
    cislo = random.randint(1,9)
    farba = random.choice(farby)
    rec = c.create_rectangle((50+posun),50,(210+posun),280, outline="black", fill="white")
    cir_1 = c.create_oval(60+posun,60,90+posun,90, outline="black", fill=farba)
    cir_2 = c.create_oval(170+posun,240,200+posun,270, outline="black", fill=farba)
    rec_bil = c.create_rectangle(75+posun,145,185+posun,185,outline="black", fill="black")
    label = tk.Label(w, text="BILGYM", bg=("black"),font=("Arial", 20))
    label_canvas = c.create_window(130+posun, 165, window=label)
    label2 = tk.Label(w, text=cislo, bg=(farba),font=("Arial", 10))
    label_canvas = c.create_window(75+posun, 75, window=label2)
    label2 = tk.Label(w, text=cislo, bg=(farba),font=("Arial", 10))
    label_canvas = c.create_window(185+posun, 255, window=label2)
    

c.pack()
w.mainloop()