# 31 dní. začiatok: utorok 
# tvar: 1. deň Utorok: -2

dni = {0:"Utorok",
           1:"Streda",
           2:"Štvrtok",
           3:"Piatok",
           4:"Sobota",
           5:"Nedela",
           6:"Pondelok",}

teplota = [-2, 2, 4, 2, -3, 1, 9, 0, 9, 5, -5, 8, 2]
len_tep = len(teplota)
print(len_tep)

for x in range(len_tep):
    if x > 6:
        y = x - 7
        print(str(x+1)+". " + str(dni[y]) + ": " + str(teplota[x]))
    else:
        print(str(x+1)+". " + str(dni[x]) + ": " + str(teplota[x]))

avg = sum(teplota)/len_tep
print(avg)

above_avg = 0

counter = 0

for tep in teplota:
    if tep > avg:
        above_avg += 1
        counter_2 = counter
        while counter_2 > 6:
            counter_2 = counter_2 - 7
        print(str(counter+1)+ ". " + str(dni[counter_2]) + ": " + str(tep))

            
        
print(above_avg)

from tkinter import *

win=Tk()

# Set the size of the tkinter window
win.geometry("1000x1000")

# Create a canvas widget
canvas=Canvas(win, width=1000, height=1000)
canvas.pack()

# Add a line in canvas widget
counter = 10

os = 250
os_tep = []

for tep in teplota:
    if tep < 0:
        x = abs(tep) * 25
        os_tep.append(os + x)
    elif tep == 0:
        os_tep.append(os)
    else: 
        x = abs(tep) * 25
        os_tep.append(os - x)
print(os_tep)
        
        


for tep in teplota:
    canvas.create_line(0,250,1000,250, fill="green", width=5)
    canvas.create_line(x,y,200,250, fill="green", width=5)
    counter =+ 10
    

win.mainloop()