# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re  # библиотека регулярных выражений

def remake(equation):   # убирает лишнее из строки из файла и записывает это в словарь
    dictEquation = {}

    result = re.search(" [0-9]+ ", equation)
    if result:
        equation = equation.replace(result.group(0), str(result.group(0)).replace(' ', '') + 'x**0 ')  # используем 're'

    equation = equation.replace(' - ', ' -').replace(' + ', ' +').replace('+x**', '+1x**').replace('-x**', '-1x**')
    equation = equation.split()
    equation = equation[:-2]

    for i in range(len(equation)):
        equation[i] = equation[i].replace('+','').split('x**')
        dictEquation[int(equation[i][1])] = int(equation[i][0])

    return dictEquation

def sumEquation(dict1, dict2):   # суммирует два словаря, которые создали из прочитанных строк файлов
    dictFinal = {}
    maximum = (max( max(dict1), max(dict2) ))
    for i in range(maximum, -1, -1):
        fierst = dict1.get(i)
        second = dict2.get(i)

        if fierst != None or second != None:
            if fierst == None:
                fierst = 0
            if second == None:
                second = 0                
            dictFinal[i] = fierst + second

    return dictFinal

def cefResult(dictFinal): # создаем строку из словаря (суммированного) и дописываем нужное
    result = ""
    for i in dictFinal.items():
        if i [1] < 0:
            result += ' - ' + str( abs(i[1]) ) + 'x^' + str( abs(i[0]) )
        elif i [1] > 0:

            if result == "":
                result += str( abs(i[1]) ) + 'x^' + str( abs(i[0]) )
            else:
                result += ' + ' + str( abs(i[1]) ) + 'x^' + str( abs(i[0]) )

    result = result.replace('x^1','x').replace('x^0','').replace('1x^','x^')

    return result + ' = 0'


with open('file1.txt','r',encoding='utf-8') as text:
    equation = text.readline()

with open('file2.txt','r',encoding='utf-8') as text:
    equation2 = text.readline()

print((equation))
print((equation2))
# print(remake(equation))
# print(remake(equation2))

dictFinal = sumEquation(remake(equation), remake(equation2))

# print(dictFinal)

res = cefResult(dictFinal)

print (res)

with open('file3.txt','w',encoding='utf-8') as text:   # записываем в файл file3.txt
    text.writelines(res)

print(f'Сумма многочленов записана в файл "file3.txt"')