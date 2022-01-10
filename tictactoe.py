'''CSE 210 - Programming with Classes
Author: Alvaro B. Godoy
Assignment: https://byui-cse.github.io/cse210-course-competency/introduction/materials/tictactoe-specification.html
'''
def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = ''
    print_board(board)
    while not (is_win(board) or is_draw(board)):
            player = who_plays(player)
            player = play(board, player)
            print_board(board)
    if is_draw(board):
        print('\n\nIt is a draw. Good luck next time!')
    else:
        print(f'\n\n{player} won!')
        print('Good game. Thanks for playing!')

def print_board(board):
    print()
    for i, v in enumerate(board):
        i += 1
        if i % 3 == 0:
            print(v, end='')
            if i != 9:
                print('\n-+-+-')
        else:
            print(f'{v}|', end='')


def who_plays(player):
    if player == '' or player == 'o':
        return 'x'
    elif player == 'x':
        return 'o'


def play(board, player):
    move = int(input(f"\n\n{player}'s turn to choose a square (1-9): ")) - 1
    if board[move] == 'o' or board[move] == 'x':
        print('Please enter a valid square!')
        if player == 'x':
            return 'o'
        elif player == 'o':
            return 'x'
    else:
        board[move] = player
        return player


def is_win(board):
    return (board[0] == board[1] == board[2] or 
            board[0] == board[3] == board[6] or
            board[6] == board[7] == board[8] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6] or
            board[3] == board[4] == board[5] or
            board[1] == board[4] == board[7])


def is_draw(board):
    for i in board:
        if i != 'x' and i != 'o':
            return False
    return True


if __name__ == '__main__':
    main()