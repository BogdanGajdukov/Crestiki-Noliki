import random

def draw_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print("     |     |")

def choose_player_marker():
    marker = ''
    while marker != 'Х' and marker != 'О':
        marker = input("Игрок 1, выберите Х или О: ").upper()
    if marker == '1':
        return ('Х', 'О')
    else:
        return ('О', 'Х')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # верхняя строка
    (board[4] == mark and board[5] == mark and board[6] == mark) or # средняя строка
    (board[1] == mark and board[2] == mark and board[3] == mark) or # нижняя строка
    (board[7] == mark and board[4] == mark and board[1] == mark) or # левый столбец
    (board[8] == mark and board[5] == mark and board[2] == mark) or # средний столбец
    (board[9] == mark and board[6] == mark and board[3] == mark) or # правый столбец
    (board[7] == mark and board[5] == mark and board[3] == mark) or # диагональ слева направо
    (board[9] == mark and board[5] == mark and board[1] == mark)) # диагональ справа налево

def choose_first_player():
    if random.randint(0, 1) == 0:
        return 'Игрок 2'
    else:
        return 'Игрок 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Выберите позицию: (1-9) '))
        return position

def replay():
    return input('Вы хотите сыграть еще раз? Да или Нет: ').lower().startswith('д')

print('Добро пожаловать в игру')


while True:
    # Игровое поле
    the_board = [' '] * 10
    player1_marker, player2_marker = choose_player_marker()
    turn = choose_first_player()
    print(turn + ' начинает первым.')

    play_game = input('Готовы ли вы играть? Введите "Да" или "Нет".')
    if play_game.lower()[0] == 'д':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':
            # Ход Игрока 1

            draw_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                draw_board(the_board)
                print('Поздравляем! Игрок 1 выиграл!')
                game_on = False
            else:
                if full_board_check(the_board):
                    draw_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 2'

        else:
            # Ход Игрока 2

            draw_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                draw_board(the_board)
                print('Поздравляем! Игрок 2 выиграл!')
                game_on = False
            else:
                if full_board_check(the_board):
                    draw_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 1'

    if not replay():
        break
