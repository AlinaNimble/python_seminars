# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
#____________________________________________________


num_day = int(input("Введите день недели: "));
if num_day >= 6 and num_day <=7:
    print("да")
else:
    print("нет") 

#-------------------------------------------------------------------------------------------------------------------------------------
# 1 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#____________________________________________________

def Predikat(X, Y, Z):
    a = not (X or Y or Z)
    b = not X and not Y and not Z
    return a == b

X = int(input("Введите X: "));
Y = int(input("Введите Y: "));
Z = int(input("Введите Z: "));

if Predikat(X,Y,Z) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")

#-------------------------------------------------------------------------------------------------------------------------------------
#  2 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#____________________________________________________

try:
    x = int(input(f"Введите x: "))
    y = int(input(f"Введите y: "))
    if x == 0 or y == 0:
        print("Координаты не должны равняться 0!")   
        quit() 
except ValueError:
    print("Вы ввели не число!")  
    quit()     

if x > 0 and y > 0:
    num_ch = 1
elif x < 0 and y > 0:
    num_ch = 2
elif x < 0 and y < 0:
    num_ch = 3
else:
    num_ch = 4

print(f'Точка находится в {num_ch}-й четверти плоскости')

#-------------------------------------------------------------------------------------------------------------------------------------
#  1 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#____________________________________________________

try:
    num_ch = int(input(f"Введите № четверти: "))
    if num_ch < 1 or num_ch > 4:
        print("Номер должен быть от 1 до 4!")    
        quit()
except ValueError:
    print("Вы ввели не число!") 
    quit()  
       
if num_ch == 1: 
    print("x > 0 AND y > 0")
elif num_ch == 2:
    print("x < 0 and y > 0")
elif num_ch == 3:
    print("x < 0 and y < 0")
else:
    print("x > 0 AND y < 0")

#-------------------------------------------------------------------------------------------------------------------------------------
#  2 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
#____________________________________________________

try:
    x1 = int(input(f"Введите x первой точки: "))
    y1 = int(input(f"Введите y первой точки: "))
    x2 = int(input(f"Введите x второй точки: "))
    y2 = int(input(f"Введите y второй точки: "))
except ValueError:
    print("Вы ввели не число!")  
    quit()  

len = ((x2 - x1)  2 + (y2 - y1)  2) ** (0.5)

print(f"Расстояние между точками: {round(len,2)}")

#—————————————————————————————————————————————— 