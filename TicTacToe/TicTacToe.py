from re import X


def print_board(board):
    print('\n')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('\n')

def play_game(player1, player2, board): 
    current_player = player1
    game_finished,winner = game_state(board)
    while not game_finished:
        move = 0
        while move not in range(1,10) or board[move] != ' ':
            move = int(input(f'Player ({current_player}), make a move: '))
        board[move] = current_player
        game_finished,winner = game_state(board)
        print_board(board)
        if game_finished:
            break
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    if game_finished:
        if winner == 'X' or winner == 'O':
            print(f'\nWell done {winner}!')
        else:
            print('\nDraw!')

def game_state(board):
    #rows
    if board[1]+board[2]+board[3] == 'XXX': return True,'X'
    if board[4]+board[5]+board[6] == 'XXX': return True,'X'
    if board[7]+board[8]+board[9] == 'XXX': return True,'X'
    if board[1]+board[2]+board[3] == 'OOO': return True,'O'
    if board[4]+board[5]+board[6] == 'OOO': return True,'O'
    if board[7]+board[8]+board[9] == 'OOO': return True,'O'

    #columns
    if board[1]+board[4]+board[7] == 'XXX': return True,'X'
    if board[2]+board[5]+board[8] == 'XXX': return True,'X'
    if board[3]+board[6]+board[9] == 'XXX': return True,'X'
    if board[1]+board[4]+board[7] == 'OOO': return True,'O'
    if board[2]+board[5]+board[8] == 'OOO': return True,'O'
    if board[3]+board[6]+board[9] == 'OOO': return True,'O'

    #diagonals
    if board[1]+board[5]+board[9] == 'XXX': return True,'X'
    if board[7]+board[5]+board[3] == 'XXX': return True,'X'
    if board[1]+board[5]+board[9] == 'OOO': return True,'O'
    if board[7]+board[5]+board[3] == 'OOO': return True,'O'

    #board still contains empty slot
    if ' ' in board:
        return False,''
    else:
        return True,''

def set_player_markers():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def main():
    board = [' '] * 10
    board[0] = '#'
    player1,player2 = set_player_markers()
    play_game(player1, player2, board)
    response = input("\nPlay again? (Y/N):").upper()
    if response == 'Y':
        main()
    else:
        exit

if __name__ == "__main__":
    main()