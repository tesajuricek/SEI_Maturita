import re
import random


def scan(x):
    numbers = []
    for i in range(len(birth_nums[x])):
        numbers.append(birth_nums[x][i])
    if int(numbers[0]) >= 2:
        if int(numbers[1]) > 3:
            birth_year = int("19" +numbers[0]+numbers[1])
        else:
            birth_year = int("20" +numbers[0]+numbers[1])
    if int(numbers[2]) > 1:
        birth_month = int(numbers[2] + numbers[3])-50
        gender = "Žena"
    else:
        birth_month = int(numbers[2]+numbers[3])
        gender = "Muž"
    birth_day = int(numbers[4] + numbers[5])
    print("Tento človek sa narodil " + str(birth_day) + "." + str(birth_month) + "." + str(birth_year) + " a je " + gender)
    file.close()

def generate(x):
    date = re.findall("[0-9]+.[0-9]+.[0-9]+",x)
    gender = re.findall("[A-Z]",x)
    print(date,gender)
    date_list = [w for w in date[0]]

    birth_year = date_list[8] + date_list[9]
    if gender[0] == "M":
        birth_month = date_list[3] + date_list[4]
    elif gender[0] == "F":
        birth_month = str(int(date_list[3])+5) + date_list[4]
    else:
        print("Invalid Gender")
        quit()


    birth_day = date_list[0] + date_list[1]

    id_number = ""
    for x in range(4):
        id_number = id_number + str(random.randint(0,9))

    birth_num = birth_year + birth_month + birth_day + "/" + id_number
    file.write(birth_num+"\n")

file = open("txt.txt","r+")

all_lines = file.readlines()
format_lines = [item.strip() for item in all_lines]
str_list =" ".join(format_lines)

birth_nums = re.findall("[0-9]+/[0-9]+",str_list)


choice = input("Čo chceš urobiť?\n1.Zistiť veci z r.n.\n2.Vygenerovať r.n.\n")

if choice == "1":
    x = int(input("Ktoré rodné číslo chceš oskenovať?"))
    scan(x-1)
elif choice == "2":
    x = input("Zadaj dátum narodenia a Pohlavie vo formáte DD.MM.RRRR G: ")
    generate(x)
