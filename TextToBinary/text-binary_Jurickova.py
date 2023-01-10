# Doteraz sme prekladali čísla do binárnej podoby. 
# Vieme však preložiť aj písmená do binárnej podoby podľa ASCII tabuľky. 
# Vytvorte aplikáciu, ktorá namodeluje preklad zadaného textu do binárnej podoby. 
# Každé písmeno má byť zapísané veľkosti jedného bajtu a má byť zobrazený v osobitnom riadku pri výpise. 
# Text načítajte z textového súboru a výsledok takisto zapíšte do textového súboru.

text = "sdf asdf"

byte_array = text.encode()

binary_int = int.from_bytes(byte_array, "big")

binary_string = bin(binary_int)

print(binary_string)
