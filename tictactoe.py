import itertools
from colorama import Style, Fore, init

init()


def play_game(game_table, player=0, row=0, column=0, just_display=False):
    try:
        if game_table[row][column] != 0:
            print("This position is occupado! Please, choose another")
            return game_table, False
        print("   "+"  ".join(str(i) for i in range(len(game_table))))
        if not just_display:
            game_table[row][column] = player
        for count, row in enumerate(game_table):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN+" X " + Style.RESET_ALL
                else:
                    colored_row += Fore.MAGENTA+" O "+Style.RESET_ALL
            print(count, colored_row)
        return game_table, True
    except IndexError as e:
        print(
            f"You should provide an input under { {range(len(game_table)-1)} }", e)
        return game_table, False
    except Exception as e:
        print("Something wrong occurs", e)
        return game_table, False


def win_horz(current_game):
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True
    return False


def win_vert(current_game):
    check = []
    for item in range(len(current_game)):
        for row in current_game:
            check.append(row[item])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True
    return False


def win_diag_left(current_game):
    diags = []
    for item in range(len(current_game)):
        diags.append(current_game[item][item])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally! (\\)")
        return True
    return False


def win_diag_right(current_game):
    diags = []
    rows = range(len(current_game))
    cols = reversed(rows)
    for row, col in zip(rows, cols):
        diags.append(current_game[row][col])

    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally! (/)")
        return True
    return False


def win(current_game):
    return win_horz(current_game) or win_vert(current_game) or win_diag_left(current_game) or win_diag_right(current_game)


def all_same(my_list):
    return my_list.count(my_list[0]) == len(my_list) and my_list[0] != 0


play = True
while play:
    game_size = int(input("What game size do you want to play? "))
    game = [[0 for i in range(game_size)]
            for i in range(game_size)]  # iterable
    players = itertools.cycle([1, 2])  # iterator
    play_game(game, just_display=True)
    won_game = False
    while not won_game:
        current_player = next(players)
        played = False
        while not played:
            print(f"Player {current_player}: ")
            current_row = int(
                input(f"What row do you want to play? {range(game_size-1)} "))
            current_column = int(
                input(f"What column do you want to play?  {range(game_size-1)}  "))
            game, played = play_game(game, current_player,
                                     current_row, current_column)
        if win(game):
            won_game = True
            again = input("Do you want to play again?(y/n) ")
            if again.lower() == "y":
                print("resarting...")
            elif again.lower() == "n":
                print("Byeeeeeee!")
                play = False
            else:
                print("bad choise, bye aligator")
                play = False
