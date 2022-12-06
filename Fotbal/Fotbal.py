import re

print("Prosím zadávajte výsledky vo formáte KRAJINA VÝSLEDOK - KRAJINA VÝSLEDOK. :)")
print("1.Vypíše všetky zápasy\n2.Vyhľadá zápasy konkrétnej krajiny\nq.Vypne program")
fotbal = []
x = 0
results = open("fotbal.txt","r+")

while "q" not in fotbal:
    fotbal.insert(x,(input("Zadaj zápas: ")))
    if fotbal[x] == "1":
        print(fotbal)
    elif fotbal[x] == "2":
        #Zatvorim otvorim lebo python
        results.close()
        results = open("fotbal.txt","r+")
        #Vypytam si krajinu ktoru hladam
        country = input("Aku krajinu chceš zobraziť? ")
        #Spravim si string z listu
        lines = results.readlines()
        strlines = "".join([str(item) for item in lines])
        #Čierna mágia
        match = re.findall("[A-Z]+ [0-9]+ - "+country+" [0-9]+|"+country+" [0-9]+ - [A-Z]+ [0-9]+", strlines)
        print(match)
    results.write(fotbal[x] + "\n")
    x+=1


print("Ok ahoj")