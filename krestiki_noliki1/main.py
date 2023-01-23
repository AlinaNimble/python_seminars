import game
import play_board

game.set_player_names()

play_board.draw_board()

while True:
    if game.game_turn() == True:
        break

