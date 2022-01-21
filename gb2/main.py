# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
# для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

newList = [1, 'hello', True]
for nl in newList:
    print("type of ", nl, " is: ", type(nl))

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

n = int(input("Enter number of values"))
secList = []

for i in range(0, n):
    val = input("enter value: ")
    secList.append(val)

secListLen = len(secList)
i = 0
while i < secListLen -1:
    if i + 1 <= secListLen:
        buf = secList[i]
        secList[i] = secList[i + 1]
        secList[i + 1] = buf
    i += 2
print(secList)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# через list
monthInt = int(input("Enter month number"))
seasonList = ['зима', 'зима',
              'весна', 'весна', 'весна',
              'лето', 'лето', 'лето',
              'осень', 'осень', 'осень',
              'зима']
if monthInt >= 1 and monthInt <= 12:
    print("сезон этого месяца: ", seasonList[monthInt - 1])
else:
    print("такого месяца нет")

# через dict
monthInt = int(input("Enter month number"))
seasonDict = {1: 'зима', 2: 'зима',
              3: 'весна', 4: 'весна', 5: 'весна',
              6: 'лето', 7: 'лето', 8: 'лето',
              9: 'осень', 10: 'осень', 11: 'осень',
              12: 'зима'}
if monthInt >= 1 and monthInt <= 12:
    print("сезон этого месяца: ", seasonDict.get(monthInt))
else:
    print("такого месяца нет")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
str = input("Enter your string")
splittedString = str.split(' ')
i = 1
for val in splittedString:
    print(i, ":", val[:10])
    i += 1


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
rating = [7, 5, 3, 3, 2]
while True:
    val = input("Enter your value, for exit print 'stop'")
    try:
        if val == 'stop':
            break
        else:
            intVal = int(val)
    except:
        print("invalid value")
    rating.append(intVal)
    rating.sort(reverse=True)
    print("\nРезультат: ", rating)