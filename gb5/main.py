# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
str_list = []
while True:
    line = input("Введите строку: ")
    if line == '':
        print(str_list)
        exit()
    else:
        newline = line + '\n'
        str_list.append(newline)

    with open("data1.txt", "w") as file_1:
        file_1.writelines(str_list)


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open("data2.txt") as file_2:
    lines = 0
    letters = 0
    for line in file_2:
        lines += 1
        letters = len(line) - line.count(' ') - 1
        if letters < 0:
            letters = 0
        print(f"{letters} букв в строчке")
    print(f"Общее кол-во строк {lines}")


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#

total = 0
count = 0
surnames = []
with open("data3.txt", "r") as file_3:
    for line in file_3:
        count += 1
        buf = line.split(' ')
        try:
            if float(buf[1]) < 20000:
                surnames.append(buf[0])
            total += float(buf[1])
        except:
            print("error in file")
    print(f"persons: {surnames}")
    print(f"average: {total / count}")


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

file_dict = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
result = []
with open("data4.txt", 'r') as file_4:
    for line in file_4:
        for ind, val in file_dict.items():
            line = line.replace(ind, val)
        result.append(line)
with open("data4_2.txt", "w") as file_4_2:
    file_4_2.writelines(result)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
try:
    with open('data_5.txt', 'w+') as file_5:
        line = input('Введите числа \n')
        file_5.writelines(line)
        my_numb = line.split()

        print(sum(map(int, my_numb)))
except:
    print("Произошла ошибка")



# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
# словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dict_subject = {}
try:
    with open('data_6.txt', 'r') as file_6:
        for line in file_6:
            buf = line.split(':')
            total = 0
            for it in buf[1].split():
                number = it.split('(')[0]
                total += int(number)
            dict_subject[buf[0]] = total
        print(dict_subject)
except:
    print("error")





# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
import json

profits = {}
av_profit = {}
try:
    with open("data_7.txt", 'r') as file_7:
        total = count = 0
        for line in file_7:
            title, type_comp, earnings, spendings = line.split()
            res = int(earnings) - int(spendings)
            if res > 0:
                count += 1
                total += res
            profits[title] = res
        av_profit["average_profit"] = total / count
        print(profits, " av ", av_profit)
    with open("data_7.txt", 'a') as file_7_write:
        profits.update(av_profit)
        json.dump(profits, file_7_write)

except:
    print("error")