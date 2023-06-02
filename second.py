# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# import random
#
# n = int(input())
#
# array = []
# for i in range(n):
#     i = random.choice(range(2))
#     array.append(i)
#
# print(array)
#
# headCount = 0
# tailCount = 0
#
# for i in array:
#     if array[i] > 0:
#         headCount += 1
#     else:
#         tailCount += 1
#
# minCount = 0
#
# if headCount > tailCount:
#     minCount = tailCount
# else:
#     minCount = headCount
#
# print(headCount, tailCount)
# print(minCount)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

for x in range(1001):
    for y in range(1001):
        if x + y == s and x * y == p:
            print(f"Задуманные числа: x = {x}, y = {y}")
            exit()



