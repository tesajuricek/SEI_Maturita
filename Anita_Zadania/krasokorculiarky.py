# V krasokorčuliarskej súťaži sa zúčastní niekoľko osôb – podľa prihlásenia. 
# Každá súťažiaca dostane body od 4 porotcov v rozsahu 5-10.
# • Vytvorte prostredie, kde sa zadá meno a priezvisko súťažiacej 
#   a náhodne sa jej vygenerujú získané body od porotcov – na kliknutie tlačidla.
# • Na ďalšie tlačidlo aplikácia vypíše zoznam aktuálnych súťažiacich, ich body od jednotlivých porotcov 
#   a celkovo získané body a zároveň vyhodnotí, ktorá bola najlepšia súťažiaca do aktuálneho stavu.

# from tkinter import *   
# root = Tk()             
# root.geometry('1000x1000')

# def take_input():
#     INPUT = inputtxt.get("1.0", "end-1c")
#     score = Label(root, text = "Name")

# inputtxt = Text(root, height = 10,
#                 width = 25,
#                 bg = "light yellow")

# T = Text(root, height = 5, width = 52)
# l = Label(root, text = "Name")
# l.config(font =("Courier", 14))

# btn = Button(root, text = 'Vygeneruj skóre', bd = '5',command = lambda:take_input())

# # Set the position of button on the top of window.    

# l.pack()
# T.pack()
# btn.pack(side = 'top') 

# root.mainloop()

import random

dic = {}
score = []

meno = input("Zadaj Meno: ")
print(meno)

for x in range(0, 4):
    x = random.randint(5,10)
    score.append(x)

dic[meno] = score

print (score)
