list = [10,30,4,55,89,34,21,74]

max_cislo = list[0]

for x in list:
    if x > max_cislo:
        max_cislo = x     
        
print(max_cislo)

min_cislo = list[0]

for x in list:
    if x < min_cislo:
        min_cislo = x     
        
print(min_cislo)