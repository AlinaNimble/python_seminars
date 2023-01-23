import random

total = 150

player1_name = ''
player2_name = ''

game_bot_mode = False

current_player = ''

def set_max_total():
    global total   

    while True:
        try:
            total_konfet = int(input("Введите общее количество конфет: "))

            if total_konfet <= 0:
                print('Введите положительное число больше 0!')
            else:
                break
        except:
            print('Введите число!')


    total = total_konfet

def set_total(take: int):
    global total
    total = total - take


def get_total():
    global total
    return total

def set_player_names():
    global player1_name
    global player2_name
    global game_bot_mode
    global current_player

    player1_name = input('Введите имя игрока 1: ')
    player2_name = input('Введите имя игрока 1 (пусто - игра с ботом): ')

    current_player = player1_name

    if (player2_name == ''):
        player2_name = "Бот"
        game_bot_mode = True


def get_cerrent_player_names():
    global current_player
    return current_player
     

def draw():
    return random.randint(0,1)

def game_turn():
    global total
    global current_player
    # global player2_name
    # global game_bot_mode

    switch_player()
   
    if current_player == player2_name and game_bot_mode:

        take = bot_turn()

    else:

        take = player_turn()

    set_total(take)

    print(f'{current_player} взял {take} конфет. На столе осталось {total}')

    

def player_turn():
    global total
    global current_player
    take = 0

    while True:
        try:

            if get_total() < 28:
                take_do = get_total()
            else:
                take_do = 28

            take = int(input(f'{current_player}, сколько конфет возьмешь (от 0 до {take_do})? '))
        except:
            print(f'Вводи цифрами!')

        if 0 < take <= take_do:
            break
        elif take > take_do:
            print(f'{current_player}, надо брать не более {take_do}!')
        else:
            print(f'{current_player}, надо что то взять!')

    return take


def bot_turn():
    global total
    take = 0

    if total <= 28:
        take = total
    else:
        take = (total - 29)%28
        if take == 0:
            take = random.randint(1,28)

    return take


def switch_player():
    global current_player
    global player1_name
    global player2_name

    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player = player1_name

