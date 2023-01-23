board = [1,2,3,4,5,6,7,8,9]

win_con = ( (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8), 
            (0,4,8), (2,4,6) )



def draw_board():
    global board

    print('-----------')

    for i in range(0,9,3):
        print(f' {board[i]} | {board[i+1]} | {board[i+2]} ')

        print('-----------')


def get_board():
    global board
    return board


def set_board(pos: int, mark: str):
    global board
    board[pos-1] = mark
    