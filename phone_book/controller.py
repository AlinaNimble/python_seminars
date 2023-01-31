from view import input, output
import phone_book

import os

os.system('clear')                            # очистка экрана

while True:

        os.system('clear')

        phone_book.print_all()                      # вывод всех контактов

        output.print_menu()                         # вывод меню

        num_menu = input.input_menu()

        if num_menu == 1:
                phone_book.add_edit_contact(-1)                # добавить контакт (пар =- 1) или изменить (пар = индекс)    

        elif num_menu == 2:
                con_name = input.input_string('Введите часть имени или номера абонента: ')
                con_id = phone_book.find_contact(con_name)            # поиск по имени, возвращает id или -1
                if con_id > -1:
                        con = phone_book.get_contact(con_id)                     # чтение контакта по его ID
                        output.print_contact(con) 
                        input.input_pause('Абонент найден! Его порядковый № = ' + str(con_id+1) + '     ')
                else:
                        input.input_pause('Абонент не найден!     ')
 
        elif num_menu == 3:
                num_ab = input.input_num_ab()
                phone_book.add_edit_contact(num_ab - 1)

        elif num_menu == 4:
                num_ab = input.input_num_ab()

                phone_book.del_contact(num_ab - 1)                          # удалить контакт (параметр = индекс с 0) 

        elif num_menu == 5:
                exit()

        else:
                input.input_pause('Выберите от 1 до 4')                
