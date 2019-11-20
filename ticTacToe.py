board = [' '] * 10
game_state = True
announce = ''


### Resete board
#########################
def reset_board():
    
    global board, game_state
    board = [' '] * 10
    game_state = True


### Display the board
#########################
def display_board():

    '''
    This function prints out the board
    '''
    
    print('\n'*100)
    print("  " + board[1] + ' |' + board[2] + ' | ' + board[3] + ' ')
    print("------------")
    print("  " + board[4] + ' |' + board[5] + ' | ' + board[6] + ' ')
    print("------------")
    print("  " + board[7] + ' |' + board[8] + ' | ' + board[9] + ' ')


### Win_check
########################
def win_check(board, player):

    '''
    Check horizontals, Verticals and diagonals for a win
    '''

    if(board[7] == board[8] == board[9] == player) or \
      (board[4] == board[5] == board[6] == player) or \
      (board[1] == board[2] == board[3] == player) or \
      (board[7] == board[4] == board[1] == player) or \
      (board[8] == board[5] == board[2] == player) or \
      (board[9] == board[6] == board[3] == player) or \
      (board[1] == board[5] == board[9] == player) or \
      (board[3] == board[5] == board[7] == player):

        return True
    else:
        return False


### Full board check
########################
def full_board_check(board):

    '''
    Check if any remaining blanks are in the board
    '''

    if ' ' in board[1:]:
        return False
    else:
        return True


### Where to place the mark
########################
def ask_player(mark):

    '''
    Ask player where to place X or O mark
    '''

    global board

    req = 'Choose where to place your: ' + mark + ' '

    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Input a number betweeb 1-9.")
            continue
    
        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print("That space isn't empty!")


### player choice
########################
def player_choice(mark):

    global board, game_state, announce

    announce = ''
    mark = str(mark)
    ask_player(mark)

    if win_check(board, mark):
        display_board()
        reset_board()
        announce = mark + " wins!!"
        game_state = False

    display_board()

    if full_board_check(board):
        announce = 'Tie!'
        game_state = False

    return game_state, announce


### Run the game
########################
def play_game():

    reset_board()
    global announce

    X = 'X'
    O = 'O'

    while True:
        display_board()

        game_state, announce = player_choice(X)
        print(announce)

        if game_state == False:
            break

        game_state, announce = player_choice(O)
        print(announce)

        if game_state == False:
            break

    rematch = input("Would you like to play again? y/n: ")

    if rematch == 'y':
        play_game()
    else:
        print("See u")


play_game()