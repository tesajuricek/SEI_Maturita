# Každá šifra skrýva obrázok nejakého dopravného prostriedku
# Postupne sa im podarilo dopracovať sa k nejakým pravidlám ohľadom údajov v tomto súbore a zistili, že:
#  zápis K 100 100 50 znamená kružnicu so stredom na [100, 100] s polomerom 50
#  zápis S 100 100 50 znamená štvorec (ľavý horný roh) na pozícii [100, 100] so stranou dĺžky 50,
#  zápis U 100 100 200 200 znamená úsečku medzi bodmi [100, 100] a [200, 200].
# Pomôžte Inke a Jurkovi rozlúštiť šifru (graficky znázorniť) a teda zistiť, o akom dopravnom prostriedku majú napísať príbeh.

import tkinter as tk
w = tk.Tk()
c = tk.Canvas(w, width=400, height=400)

f = open("subor15.txt")

data = f.read()
list = data.split("\n")
sifry_list = []

for sifra in list:
    sifra = sifra.split(" ")
    sifry_list.append(sifra)

for sifra in sifry_list:
    if sifra[0] == "K":
        x = int(sifra[1])
        y = int(sifra[2])
        z = int(sifra[3])
        print("Kružnicu so stredom na [{}, {}] s polomerom {}".format(x, y, z))
        k = c.create_oval(x-z,y-z,x+z,y+z)

    elif sifra[0] == "S":
        x = int(sifra[1])
        y = int(sifra[2])
        z = int(sifra[3])
        print("Štvorec so ľavým horným rohom na [{}, {}] so stranou dĺžky {}".format(x, y, z))
        k = c.create_rectangle(x,y,x+z,y+z)
    
    elif sifra[0] == "U":
        x = int(sifra[1])
        y = int(sifra[2])
        z = int(sifra[3])
        a = int(sifra[4])
        print("Usečka medzi bodmi [{}, {}] a [{}, {}]".format(x, y, z, a))
        k = c.create_line(x,y,z,a)
    
    



print(sifry_list)


c.pack()
w.mainloop()
