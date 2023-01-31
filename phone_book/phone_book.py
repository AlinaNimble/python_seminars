from view import input, output

phone_book = []
file_pb = 'addrbook.txt'

def load_phone_book():
    global phone_book

    with open(file_pb,'r',encoding='UTF-8') as file:
        phone_book = file.readlines()
        file.close()


def add_edit_contact(index: int):
    global phone_book
    load_phone_book()

    new_contact = input.input_contact()

    if index == -1:
        with open(file_pb,'a',encoding='UTF-8') as file:
            file.write(new_contact)
            file.close()
    else:
        if 0 <= index <= len(phone_book):
            with open(file_pb,'w',encoding='UTF-8') as file:

                phone_book[index] = new_contact

                for con in phone_book:
                    file.write(con)

            file.close()


def del_contact(index: int):
    global phone_book
    load_phone_book()

    if 0 <= index <= len(phone_book):
        with open(file_pb,'w',encoding='UTF-8') as file:

                phone_book.pop(index)
                
                for con in phone_book:
                    file.write(con)

                file.close()
    else:
        input.input_pause('Абонент не найден!')


def print_all():
    global phone_book
    load_phone_book()

    print('----------------------------------------------')
    print('АДРЕСНАЯ КНИГА:')

    i=0
    for con in phone_book:  
        i+=1
        output.print_contact(f'{i}. {con}')     


def get_contact(contact_id: int):
    global phone_book

    load_phone_book()

    if 0 <= contact_id <= len(phone_book):
        return phone_book[contact_id]
    

def find_contact(name: str):
    global phone_book

    load_phone_book()
        
    for i in range(len(phone_book)):  

        con = phone_book[i].lower()
        name = name.lower()

        if con.find(name) > -1:
            return i

    return -1


