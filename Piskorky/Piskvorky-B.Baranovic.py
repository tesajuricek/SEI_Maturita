import tkinter

window = tkinter.Tk()

desktop = tkinter.Canvas(width=900, height=900)
desktop.pack()

grid = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    grid.append(row)


def check_x():
    if grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        print("X wins")
        return desktop.create_line(0, 0, 900, 900, width=6, fill="red")
    elif grid[2][0] == "X" and grid[1][1] == "X" and grid[0][2] == "X":
        print("X wins")
        return desktop.create_line(0, 900, 900, 0, width=6, fill="red")
    elif grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        print("X wins")
        return desktop.create_line(0, 150, 900, 150, width=6, fill="red")
    elif grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        print("X wins")
        return desktop.create_line(0, 450, 900, 450, width=6, fill="red")
    elif grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        print("X wins")
        return desktop.create_line(0, 750, 900, 750, width=6, fill="red")
    elif grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        print("X wins")
        return desktop.create_line(150, 0, 150, 900, width=6, fill="red")
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        print("X wins")
        return desktop.create_line(450, 0, 450, 900, width=6, fill="red")
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        print("X wins")
        return desktop.create_line(750, 0, 750, 900, width=6, fill="red")


def check_o():
    if grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        print("O wins")
        return desktop.create_line(0, 0, 900, 900, width=6, fill="green")
    elif grid[2][0] == "O" and grid[1][1] == "O" and grid[0][2] == "O":
        print("O wins")
        return desktop.create_line(0, 900, 900, 0, width=6, fill="green")
    elif grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        print("O wins")
        return desktop.create_line(0, 150, 900, 150, width=6, fill="green")
    elif grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        print("O wins")
        return desktop.create_line(0, 450, 900, 450, width=6, fill="green")
    elif grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        print("O wins")
        return desktop.create_line(0, 750, 900, 750, width=6, fill="green")
    elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        print("O wins")
        return desktop.create_line(150, 0, 150, 900, width=6, fill="green")
    elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        print("O wins")
        return desktop.create_line(450, 0, 450, 900, width=6, fill="green")
    elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        print("O wins")
        return desktop.create_line(750, 0, 750, 900, width=6, fill="green")


for i in range(3):
    desktop.create_line(i * 300, 0, i * 300, 900)
    desktop.create_line(0, i * 300, 900, i * 300)


def klik1(event):
    x = event.x // 300 * 300
    y = event.y // 300 * 300
    if grid[y // 300][x // 300] == " ":
        grid[y // 300][x // 300] = "O"
        desktop.create_oval(x + 75, y + 75, x + 225, y + 225, width=6, outline="green")
        print(grid)
        check_o()


def klik2(event):
    x = event.x // 300 * 300
    y = event.y // 300 * 300
    if grid[y // 300][x // 300] == " ":
        grid[y // 300][x // 300] = "X"
        desktop.create_line(x + 75, y + 75, x + 225, y + 225, width=6, fill="red")
        desktop.create_line(x + 225, y + 75, x + 75, y + 225, width=6, fill="red")
        print(grid)
        check_x()


desktop.bind("<Button-1>", klik1)  # 1-lave, 2-koliecko, 3-prave
desktop.bind("<Button-3>", klik2)

window.mainloop()