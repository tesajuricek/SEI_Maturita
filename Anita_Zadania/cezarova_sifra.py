list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
veta = "PETER MA SIKANUJE"
nova_v = []
pousn = 4
for letter in veta:
    if letter != " ":
        idx = list.index(letter)
        idx_posun = idx + pousn
        if idx_posun > 26:
            idx_posun -= 26
        nova_v.append(list[idx_posun])
    else:
        nova_v.append(" ")

print(nova_v)
print(* nova_v)
    
    
 