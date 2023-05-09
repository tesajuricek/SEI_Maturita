
file = open("txt.txt","r+", encoding="UTF-8")

whole_text = file.read()

text_chars = list(whole_text)

for char in text_chars:
    temp_char = char.lower()
    temp_place = text_chars.index(char)
    text_chars[temp_place] = temp_char
    if char == ".":
        temp_place = text_chars.index(char)
        text_chars[temp_place] = ""

file.write("".join(text_chars) + "\n")
