# Pripravte evidenciu bazénov. Evidujte nasledujúce vlastnosti bazéna: názov, šírka, výška, hĺbka, farba – tieto
# vlastnosti zadáva užívateľ. Okrem toho evidujte aj objem bazéna – vypočítajte z údajov. Vytvorte možnosť vyhľadať (zobrazte všetky vlastnosti nájdeného bazénu):
#   • Objemovo najväčší bazén
#   • Bazény podľa názvu
#   • Bazény podľa hĺbky

# nazov : [šírka, výška, hĺbka, farba]
#            0      1      2      3

dic = {"bazen1": [10, 5, 6, "modrá"],
       "bazen2": [5, 8, 10, "ružová"],
       "bazen3": [10, 3, 2, "zelená"]}
list = []

while True:
    # nazov = input("Názov: ")
    # sirka = input("Sirka: ")
    # vyska = input("Vyska: ")
    # hlbka = input("Hlbka: ")
    # farba = input("Farba: ")
    # list = [int(sirka), int(vyska), int(hlbka), str(farba)]
    # dic[nazov] : list
    koniec = input("koniec?")
    if koniec == "ano":
        break
    

print("možnosti úloh hladania su: názov / šírka / výška / hĺbka / farba")
# uloha = input("Zadaj co chceš spraviť:" )
uloha = "hladať"
counter = 0

if uloha == "hladať":
    # n = input("nazov: ")
    n = "bazen2"
    for x in dic:
        if x == n:
            print(str(n) + str(dic[n]))