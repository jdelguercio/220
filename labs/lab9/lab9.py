"""
Name: <Joey Del Guercio>
<ProgramName>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if board[position-1] == 'x' or board[position-1] == 'o':
        return False
    else:
        return True


def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position-1] = character


def winning_game(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False

def game_over(board):
    xCount = 0
    oCount = 0

    for position in board:
        if position == 'x':
            xCount += 1
        elif position == 'o':
            oCount += 1

    if winning_game(board) == True:
        return True
    elif xCount + oCount == 9:
        return True
    else:
        return False

def get_winner(board):
    if winning_game(board):
        xCount = 0
        oCount = 0

        for position in board:
            if position == 'x':
                xCount += 1
            elif position == 'o':
                oCount += 1

        if xCount == oCount:
            return 'o'
        else:
            return 'x'

    else:
        return None


def play(board):
    xCount, oCount = 0, 0
    print_board(board)

    while not winning_game(board):

        while xCount == 0 or oCount - xCount == 0:
            position = eval(input("x's, choose a position:"))
            if is_legal(board, position) == True:
                fill_spot(board, position, 'x')
                xCount += 1
                print_board(board)
            else:
                print('invalid move')
                print_board(board)

        if winning_game(board):
            break

        while oCount == 0 and xCount == 1 or oCount < xCount:
            position = eval(input("o's, choose a position:"))
            if is_legal(board, position) == True:
                fill_spot(board, position, 'o')
                oCount += 1
                print_board(board)
            else:
                print('invalid move')
                print_board(board)

    while winning_game(board):
        winner = get_winner(board)
        print("{}'s win".format(winner))
        answer = input("play again?")
        if answer[0] == 'y' or answer[0] == 'Y':
            play(build_board())
        else:
            exit()





test_board = build_board()
play(test_board)

def main():
    pass


if __name__ == '__main__':
    main()
