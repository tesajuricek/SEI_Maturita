import tkinter as tk
import random

w = tk.Tk()
c = tk.Canvas(w, width=800, height=800)

rozmery = [20,30,40,50]
random.shuffle(rozmery)
print(rozmery)

counter = 1
for i in rozmery:
    rec = c.create_rectangle((150*counter)-i,(100)-i,(150*counter)+i,(100)+i, fill = "green")
    counter += 1

random.shuffle(rozmery)
counter = 1 
for i in rozmery:
    oval = c.create_oval((150*counter)-i,(250)-i,(150*counter)+i,(250)+i, fill = "blue")
    counter += 1

c.pack()

found_pairs = 0
oval_selected = None
rec_selected = None
list_o =[]
list_r =[]

# Define a function to get the oval's parameters
def get_oval_params(oval_item):
    global oval_selected
    global list_o
    # "global" makes oval editable inside a function
    if oval_item is not None:
        c.itemconfig(oval_item, outline="red") 
    x1, y1, x2, y2 = c.coords(oval_item)
    width = x2 - x1
    color = c.itemcget(oval_item, "fill")
    print("Width:", width)
    print("Color:", color)
    oval_selected = width
    print(oval_selected)
    list_o = [width,x1, y1, x2, y2]
    if oval_selected == rec_selected:
        print("Jupi")
        vyhra(list_o, list_r)
        

# Define a function to get the rectangle's parameters
def get_rect_params(rect_item):
    global rec_selected
    global list_r

    # "global" makes oval editable inside a function
    if rect_item is not None:
        c.itemconfig(rect_item, outline="red") 
    x1, y1, x2, y2 = c.coords(rect_item)
    width = x2 - x1
    color = c.itemcget(rect_item, "fill")
    print("Width:", width)
    print("Color:", color)
    rec_selected = width
    print(rec_selected)
    list_r = [width,x1, y1, x2, y2]
    if oval_selected == rec_selected:
        print("Jupi")
        vyhra(list_o, list_r)

# Bind the oval and rectangle to a mouse click event
oval = None
rectangle = None

def bind_shape(event):
    global oval
    global rectangle
    
    # finds the item that is currently under the mouse and assigns it to the variable "item"
    item = c.find_withtag("current")[0]
    
    if c.type(item) == "oval":
        
        # if the global variable "oval" was previously assigned a value
        # the values are set in the get_oval_params function and thus has a value only after at least one click on an oval
        # ex. we first click on an oval, so it doesnt change border to black because it hasnt reached the function where it actually happens
        if oval is not None:
            c.itemconfig(oval, outline="black")
        
        oval = item
        get_oval_params(item)
    elif c.type(item) == "rectangle":
        if rectangle is not None:
            c.itemconfig(rectangle, outline="black")
        rectangle = item
        get_rect_params(item)
    else:
        if oval is not None:
            c.itemconfig(oval, outline="black")
        oval = None
        if rectangle is not None:
            c.itemconfig(rectangle, outline="black")
        rectangle = None

def vyhra(oval, rec):
    global found_pairs
    if oval[0] == rec[0]:
        grey_r = c.create_rectangle(rec[1],rec[2],rec[3],rec[4], fill="grey")
        grey_o = c.create_oval(oval[1],oval[2],oval[3],oval[4], fill="grey")
        found_pairs += 1
    if found_pairs == 4:
        print("You won")
        c.destroy()
        w2 = tk.Tk()
        c2 = tk.Canvas(w2, width=800, height=800)
        c2.pack()
        c2.create_text(400,200,text="YOU WON", font=('Helvetica','50','bold'))
        w2.mainloop()
        
        

c.bind("<Button-1>", bind_shape)

w.mainloop()