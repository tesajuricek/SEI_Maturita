import time


num1 = input("Num1: ")
num2 = input("Num2: ")

current_time = int(time.time())
random_int = current_time % 1000
print(random_int)

my_random = None
counter = 0

while my_random == None:
    for x in range(num1,num2):
        counter += 1
        if counter == random_int:
            my_random = x
            break
        
        
print(my_random)
