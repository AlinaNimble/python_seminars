import play_board
import random

player1_name = ''
player2_name = ''

game_bot_mode = False

current_player = 'player1_name'
mark = 'X'

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

def switch_player():
    global mark
    global current_player
    global player1_name
    global player2_name

    if mark == 'X':
        current_player = player1_name
        mark = '0'
    else:
        current_player = player2_name
        mark = 'X'


def game_turn():
    global mark
    global current_player
    global player1_name
    global player2_name

    switch_player()

    position = ''

    if current_player == player2_name and game_bot_mode:
        pos = bot_turn()
    else:
        pos = player_turn()

    play_board.set_board(pos,mark)

 
    # уже победа?:
    board = play_board.get_board()
    
    play_board.draw_board()

    for pos2 in play_board.win_con:
        if board[pos2[0]] == board[pos2[1]] == board[pos2[2]]:
            print(f'Помеждают {mark}-ки под управлением {current_player}')
            return True
            

        
def player_turn():
    global current_player

    while True:
        try:
            pos = int(input(f'{current_player}, введите позицию: '))
            if pos in play_board.get_board():
                return pos
            else:
                print('Эта позиция занята!')
        except:
            print('Вводить можно только цифры!')

def bot_turn():
    pass
            