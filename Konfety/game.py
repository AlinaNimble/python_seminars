import commands

def start():

    commands.set_max_total()

    commands.set_player_names()

    if commands.draw() == 1:
        commands.switch_player()

    while commands.get_total() > 0:
        commands.game_turn()

    print(f'{commands.get_cerrent_player_names()} забрал последние конфеты и победил!')

