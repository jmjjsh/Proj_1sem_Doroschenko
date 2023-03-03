import re

f = open("Dostoevsky.txt.", "r", encoding="utf-8").read()
x = re.findall(r'Достоев\w+', f)
print(x)



