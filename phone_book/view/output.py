

def print_contact(contact: str):

    if contact == None:
        return

    contact_l = contact.strip().split(';')
    
    print (f'{contact_l[0]:30} {contact_l[1]:10} {contact_l[2]:20}')


def print_menu():
    print('______________________________________________')
    print('МЕНЮ:')
    print('1 - создание нового контакта')
    print('2 - поиск контакта')
    print('3 - редактирование контакта')
    print('4 - удаление контакта')
    print('5 - выход из программы')
    print('----------------------------------------------')