import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)

body = canvas.create_rectangle(175, 50, 325, 450, fill="gray10")
red = canvas.create_oval(200, 75, 300, 175, fill='maroon')
orange = canvas.create_oval(200, 200, 300, 300, fill='sienna')
green = canvas.create_oval(200, 325, 300, 425, fill='darkgreen')


def toggle_green():
        canvas.itemconfigure(green, fill="green2")
        canvas.after(5000, lambda: canvas.itemconfigure(green, fill="darkgreen"))
        canvas.after(5000, lambda: canvas.after(0, toggle_orange))


def toggle_orange():
        canvas.itemconfigure(orange, fill="orange")
        canvas.after(2000, lambda: canvas.itemconfigure(orange, fill="sienna"))
        canvas.after(2000, lambda: canvas.after(0, toggle_red))


def toggle_red():
        canvas.itemconfigure(red, fill="red")
        canvas.after(5000, lambda: canvas.itemconfigure(orange, fill="orange"))
        canvas.after(7000, lambda: canvas.itemconfigure(orange, fill="sienna"))
        canvas.after(7000, lambda: canvas.itemconfigure(red, fill="maroon"))
        canvas.after(7000, lambda: canvas.after(0, toggle_green))

button_on = tk.Button(root, text="Turn On", command=toggle_red)
button_on.pack()


canvas.pack()
root.mainloop()
