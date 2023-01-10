import re
memory = 0
binary = bin(int(input("input your number: ")))[2:]
str(binary)
all = re.findall(r"[0]+[1]",binary)

for i in all:
    x = len(str(i))
    x -= 1
    if x >= memory:
        memory = x
print(binary)
print("number of zeros: ", memory) #may now work idk
