import re

file = open("task.txt",'r')

text = file.read()
date_format = "\d{2}[.]\d{2}[.]\d{4}"
dates = re.findall(date_format,text)
duartion_format = "\d{2}.\d{2}\s\D\s\d{2}.\d{2}"
duration = re.findall(duartion_format,text)
time = re.findall("\d{1,2}:\d{1,2}",text)
tel = re.findall("\d{4}\s\d{3}\s\d{3}",text)
eur = re.findall("\d+[,]\d+ Eur",text)
email = re.findall("[\w.+]+@[\w]+\.[\w.]+",text)
name = re.findall("[–]\s\w+\s\w+\s[–]",text)
question = re.findall("[.]\s\D+[?]",text)

for date in dates:
    print(date)
print(time)
print(duration)
print(tel)
print(eur)
print(email)
print(name)
print(question)
file.close()


# Special Characters in Regex:
# \s – A space character
# \S – Any character except for a space character
# \d – Any digit from 0 to 9
# \D – And any character except for a digit
# \w – Any word of characters or digits [a-zA-Z0-9]
# \W – Any non-word characters