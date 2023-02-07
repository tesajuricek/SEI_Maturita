print("Input num: ")
dec = int(input())
binary = bin(dec)[2:]
print(binary)
res = [int(x) for x in str(binary)]
res.reverse()
print(res)
count = 0
mem = 0
check = 0
for i in res:
    if i == 1:
        check = 1
    if check == 1:
        if i == 0:
            count += 1
        else:
            if count >= mem:
                mem = count
                count = 0
if count >= mem:
    print("answer:\n", count)
else:
    print("answer:\n", mem)