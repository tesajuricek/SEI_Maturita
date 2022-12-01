import re

txt = open("txt.txt")

equations = txt.readlines()

choice = int(input("Ktorý príklad chceš vypočítať?"))
print(equations[choice-1])
kok = equations[choice-1]
x2 = re.findall(".*x\^2", kok)
print(x2)

