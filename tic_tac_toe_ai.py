
import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6] # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

def is_draw(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == ' ']

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 10 - depth
    if is_winner(brd, 'X'):
        return depth - 10
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score> best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in get_available_moves(board):
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        ai_move()
        print("AI's move:")
        print_board()
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()