import tkinter as tk
import random


root = tk.Tk()
canvas = tk.Canvas(width=1200, height=1200)
canvas.pack()

rectangle_width = 3
circle_size = 57 + rectangle_width
border = 5
colors = ["red", "green", "blue", "yellow"]
user_color = None
mode = int(input("choose 1 for random, 2 for custom: "))
if mode == 1:
    for x in range(5):
        color = random.choice(colors)
        number = str(random.randint(1, 9))
        canvas.create_rectangle((x * 200) + rectangle_width, rectangle_width, (x * 200) + 200 + rectangle_width,
                            300 + rectangle_width,
                            width=rectangle_width)
        canvas.create_oval((x * 200) + 5 + rectangle_width, 5 + rectangle_width, (x * 200) + 5 + circle_size,
                       5 + circle_size, fill=color)
        canvas.create_oval((x * 200)+ 200 - circle_size - border + rectangle_width, 300 - circle_size - border + rectangle_width,
                       (x * 200)+ 200 + rectangle_width - border, 300 + rectangle_width - border, fill=color)
        canvas.create_rectangle((x * 200) + 25 + rectangle_width, 115 + rectangle_width,(x * 200) + 175 + rectangle_width, 185 + rectangle_width,
                            fill="black")
        canvas.create_text((x * 200)+103, 152, text='BILGYM', fill=color, font=("Comic Sans", "18", "bold"))
        canvas.create_text((x * 200) + 36, 36, text=number, fill='black', font=("Comic Sans", "18", "bold"))
        canvas.create_text((x * 200) + 200 - 33, 300 - 33, text=number, fill='black', font=("Comic Sans", "18", "bold"))
elif mode == 2:
    user_color = str(input("Type a chosen color (red, green, blue, yellow): "))
    user_num = int(input("Type a number between 1 and 9: "))
    canvas.create_rectangle(rectangle_width, rectangle_width, 200 + rectangle_width, 300 + rectangle_width, width=rectangle_width)
    canvas.create_oval(5 + rectangle_width, 5 + rectangle_width, 5 + circle_size, 5 + circle_size, fill=user_color)
    canvas.create_oval(200 - circle_size - border + rectangle_width, 300 - circle_size - border + rectangle_width, 200 + rectangle_width - border, 300 + rectangle_width - border, fill=user_color)
    canvas.create_rectangle(25 + rectangle_width, 115 + rectangle_width, 175 + rectangle_width, 185 + rectangle_width, fill="black")
    canvas.create_text(103, 152, text='BILGYM', fill=user_color, font=("Comic Sans", "18", "bold"))
    canvas.create_text(36, 36, text=user_num, fill='black', font=("Comic Sans", "18", "bold"))
    canvas.create_text( 200 - 33, 300 - 33, text=user_num, fill='black', font=("Comic Sans", "18", "bold"))


root.mainloop()
