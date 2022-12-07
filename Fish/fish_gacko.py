A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

con = True
while con:
    to_delete = []
    key = 0
    while key < len(B) - 1:
        if B[key] == 1 and B[key + 1] == 0:
            if A[key] > A[key + 1]:
                to_delete.append(key + 1)
            else:
                to_delete.append(key)
        key += 1
    if to_delete:
        to_delete.sort(reverse=True)
        for index in to_delete:
            A.pop(index)
            B.pop(index)
    else:
        con = False

print(A)
print(B)
