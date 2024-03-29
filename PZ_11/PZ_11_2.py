# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое, количество букв в нижнем
# регистре. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю
# строку фразой введенной пользователем.
f1 = open('text18-9.txt', 'r', encoding='UTF-8').read()  # открываем файл на чтение

low = ' '.join([i for i in f1 if i.islower()]).split(' ')  # получаем все буквы нижнего регистра

print(f'Содержимое файла: \n\n{f1}\n\nКоличество букв в нижнем регистре: {len(low)}')

f2 = open('text18-9_2.txt', 'w', encoding='UTF-8')  # открываем файл на запись

user = input('Введите фразу: ')
f2.write(f1 + f'\n\nФраза пользователя: {user}')  # записываем в конец автора и название
f2.close()  # закрываем файл
