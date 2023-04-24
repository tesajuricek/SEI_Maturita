sentence = input("Zadaj vetu na zašifrovanie: ")
key = int(input("O koľko sa má posunúť celá abeceda?"))

chars = list(sentence)
encoded_sentence = []

for elem in chars:
    if ord(elem) == 32:
        encoded_sentence.append(elem)
        continue
    elif ord(elem)+key >= 122:
        new_elem_code = 65 + (ord(elem)+key-122)
        new_elem = chr(new_elem_code)
        encoded_sentence.append(new_elem)
        continue
    elif 90 < ord(elem)+key < 97:
        new_elem_code = 97 + (ord(elem)+key-ord(elem))
        new_elem = chr(new_elem_code)
        encoded_sentence.append(new_elem)
        continue
    new_elem_code = ord(elem)+key
    new_elem = chr(new_elem_code)
    encoded_sentence.append(new_elem)

print("".join(encoded_sentence))



