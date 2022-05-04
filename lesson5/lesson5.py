#############################################################################################################
# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
#############################################################################################################
import os


f = open('king.txt', "w+")
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()


#############################################################################################################
# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
#############################################################################################################
import os

f = open('Mum.txt')
lines = 0
words = 0
for line in f:
    lines += 1
    words += len(line.split())
print("Lines:", lines)
print("Words:", words)


#############################################################################################################
# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#############################################################################################################

with open('salary.txt', 'r', encoding='UTF-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key} got less than 20k')





#############################################################################################################
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#############################################################################################################

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

f = open("task4.txt", "r")
list1 = f.readlines()
print(list1)
list2 = []
for i in list1:
    i = i.split(' ', 1)
    list2.append(rus[i[0]] + ' ' + i[1])
    print(list2)
f.close()

f2 = open('task4_rus.txt', 'w')
f2.writelines(list2)
f2.close()


#############################################################################################################
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
#############################################################################################################

with open('king5.txt', 'w+') as file_obj:
    line = input('Введите цифры через пробел \n')
    file_obj.writelines(line)
    my_numb = line.split()

    print(sum(map(int, my_numb)))


#############################################################################################################
# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#############################################################################################################
import json
import codecs

study = {}

with open('task6.txt', 'r') as init_f:

    for line in init_f:
        subject, lecture, practice, lab = line.split()
        study[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету - \n {study}')



#############################################################################################################
# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#############################################################################################################
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('task7.txt', 'r') as file:
    for line in file:
        name, firm, earning, expenses = line.split()
        profit[name] = int(earning) - int(expenses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver}')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open("task7.json", "w") as write_f:
    json.dump(prof_aver, write_f)