import random
statistics_sum={
"1":0,
"2":0,
"3":0,
"4":0,
"5":0,
"6":0,
}

counter = 0
while counter < 1000:
    roll = (random.randrange(1, 7))
    statistics_sum[(str(roll))] += 1
    counter += int(roll)
print(statistics_sum)


# print(int(statistics_sum["2"])*2)

counter = 1
for x in (statistics_sum.values()):
    print(x)
    print((x*counter))
    counter += 1