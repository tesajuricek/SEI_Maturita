import random
rounds = int(input("Počet kôl: "))
list = ["r", "p", "s"]
loses_to = {
    "r": "s",
    "p": "r",
    "s": "p",
}
counter = 0
while rounds > counter:
    counter += 1
    player = str(input("Enter your move: "))
    comp = random.choice(list)
    print(comp)
    if comp == loses_to[player]:
        print(" you win")
    elif player == loses_to[comp]:
        print(" you loose")
    else:
        print(" it is a tie")