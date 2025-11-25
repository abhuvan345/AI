import math

board=[['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

def print_board():
    for row in board:
        print(' '.join(row))

def check_winner():
    for row in board:
        if row[0]==row[1]==row[2]!='-':
            return row[0]
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]!='-':
            return board[0][col]
    if board[0][0]==board[1][1]==board[2][2]!='-':
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!='-':
        return board[0][2]
    return None

def is_full():
    return all(board[r][c]!='-' for r in range(3) for c in range(3))

def evaluate():
    winner=check_winner()
    if winner=='O':
        return 1
    elif winner=='X':
        return -1
    return 0

def minimax(maximizing):
    score=evaluate()
    if score!=0:
        return score
    if is_full():
        return 0
    
    if maximizing:
        best=-math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col]=='-':
                    board[row][col]='O'
                    value=minimax(False)
                    board[row][col]='-'
                    best=max(best,value)
        return best
    else :
        best=math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col]=='-':
                    board[row][col]='X'
                    value=minimax(True)
                    board[row][col]='-'
                    best=min(best,value)
        return best


def computer_move():
    best_score=-math.inf
    best_move=None
    for r in range(3):
        for c in range(3):
            if board[r][c]=='-':
                board[r][c]='O'
                score=minimax(False)
                board[r][c]='-'
                if score>best_score:
                    best_score=score
                    best_move=(r,c)
    if best_move:
        r,c=best_move
        board[r][c]='O'

def player_move():
    while True:
        try:
            move=int(input("Enter your move (0-8):"))
            if move<0 or move>8 :
                print("Invalid move. Try again")
                continue
            row=move//3
            col=move%3
            if board[row][col]!='-':
                print("Cell already taken. Try again")
                continue
            board[row][col]='X'
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8")


while True:
    print_board()
    player_move()
    winner=check_winner()
    if winner:
        print_board()
        print("You win!")
        break
    if is_full():
        print_board()
        print("It's a draw!")
        break
    computer_move()
    winner=check_winner()
    if winner:
        print_board()
        print("Computer wins!")
        break
    if is_full():
        print_board()
        print("It's a draw!")
        break