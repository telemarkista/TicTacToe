"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Robert Zunt
email: robert.zunt@gmail.com
discord: telemarkista#2523
"""
splitter = 42*"="

print(splitter)
print("Let´s start the game!")
print(splitter)
board = [' ' for x in range(9)] #definition of board list empty


def insert_letter(letter, position):    #letter = x/y, position on board
    board[position] = letter

def space_is_free(position):
    return board[position] == ' '

def print_board(board): #print playing board nicely
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def print_board_help():     #print position numbering for better orientation
    print("Position numbering:")
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('-----------')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('-----------')
    print('7' + ' | ' + '8' + ' | ' + '9')

def is_board_full(board):       #checks number of 'empty' positions
    return board.count(' ') == 0

def is_winner(board, letter):
    return (board[0] == letter and board[1] == letter and board[2] == letter) or \
           (board[3] == letter and board[4] == letter and board[5] == letter) or \
           (board[6] == letter and board[7] == letter and board[8] == letter) or \
           (board[0] == letter and board[3] == letter and board[6] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[0] == letter and board[4] == letter and board[8] == letter) or \
           (board[2] == letter and board[4] == letter and board[6] == letter)

def player_move(player):
    run = True
    while run:
        move = input(f"Player {player}, please select a position to place your mark (1-9): ")
        try:
            move = int(move) - 1        #numbering positions starts from 1, int check if is whole number
            if move >= 0 and move < 9:
                if space_is_free(move):
                    insert_letter(player, move)
                    run = False #end of cycle, next player
                else:
                    print("Sorry, this space is already occupied!")
            else:
                print("Please type a number within the range!")
        except:
            print("Please type a number!")
def game():
    print(f"Welcome to Tic Tac Toe")
    print(splitter)
    print(f"GAME RULES:"
          f"\nEach player can place one mark (or stone)"
          f"\nper turn on the 3x3 grid. The WINNER is"
          f"\nwho succeeds in placing three of their"
          f"\nmarks in a:"
          f"\n* horizontal,"
          f"\n* vertical or"
          f"\n* diagonal row")
    print(splitter)
    player1 = "X"
    player2 = "O"
    print(f"Player one is  {player1}, player two is {player2}")
    print(splitter)
    print_board_help()
    current_player = player1
    while not is_board_full(board):
        player_move(current_player)
        print_board(board)
        if is_winner(board, current_player):
            print(f"{current_player} is winner!")
            exit()
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    print(f"Its a tie!")

game()


