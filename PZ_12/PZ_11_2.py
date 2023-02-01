# Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string.
# Строка'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
from string import ascii_lowercase

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'  # ввод
text_lower = ''.join([str(i) for i in text if i in ascii_lowercase])  # поиск нижнего регистра
print(text_lower)  # вывод
