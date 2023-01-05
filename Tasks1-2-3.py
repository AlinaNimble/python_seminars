# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

A = float(input("Введите вещественное число: "))

while (A % 1) > 0:
   A = A * 10   

sum = 0

while A > 0:
   A = A / 10     
   sum += (A % 1) * 10
   A = A // 1

print (round(sum))
#------------------------------------------------------------------------------------------------


# Задача 2 
# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input("Введите n: "))

s = []
sum = 0

for i in range(1, n+1):
    item = round( (1+1/i)**i , 2)
    sum += item
    s.append(item)

print (s)
print (round(sum,2))
#------------------------------------------------------------------------------------------------

# Задача 3 
# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

import random

s = []
s2 = []
n = 10 

for i in range(n):
    s.append(random.randint(10,100))

for i in range(n):
    j = random.randint(0,n+1)
    s2.insert(j,s[i])

print (s)
print (s2)
#------------------------------------------------------------------------------------------------
