binary_list = [] # for decimal function
decimal_list = [] # for binary function

x = int(input("Insert number: "))

number_type = (input("Is the nuber decimal or binary? "))



if number_type == "decimal":
    while x > 0:
        zvysok = x % 2
        binary_list.insert(0,int(zvysok))
        x = ((x - zvysok) / 2)

elif number_type == "binary":
    final = 0
    list_x = []
    str_x = str(x)
    int_x = int(len(str_x))
    for z in str_x:
        list_x.insert(0,int(z))
    for y in range(0, int_x):
        a = (int(list_x[y]) * (2 ** y))
        final = final + a
    print(final)


else:
    print("Invalid input!!!!")
print(binary_list)
