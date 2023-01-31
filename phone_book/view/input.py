from view import output


def input_contact():
    c1 = input('Введите ФИО: ')
    c2 = input('Введите номер: ')
    c3 = input('Введите Ник: ')
    return ''.join([c1.strip(), ';', c2.strip(), ';', c3.strip(), '\n'])


def input_menu():
    try:
        num = int(input('Введите номер элемента меню телефонной книги (1-5): '))
        return num
    except:
        print('Вводите только цифры!')

def input_string(msg: str):

        string = input(msg)
        return string

def input_pause(msg: str):
    i = input(msg) 

def input_num_ab():
    try:
        num = int(input('Введите порядковый номер абонента: '))
        return num
    except:
        print('Вводите только цифры!')    