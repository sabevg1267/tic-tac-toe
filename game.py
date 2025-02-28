import random

def print_board(board):
    for i in range(0, len(board), 3):
        print(board[i], board[i+1], board[i+2])


def open_spots(list):
    newList = []
    for i in range(len(list)):
        if list[i] == "-":
            newList.append(i)
    
    return newList

def random_move(board, symbol):
    openList = open_spots(board) #["-","-"]
    board[random.choice(openList)] = symbol
    #print_board(board)
    return board


def check_three(board, indx1, indx2, indx3):
    if board[indx1] == "X" and board[indx2] == "X" and board[indx3] == "X":
        return("X")
    elif board[indx1] == "O" and board[indx2] == "O" and board[indx3] == "O":
        return("O")
    else:
        return("-")


def winner(board):

    if check_three(board, 0, 1, 2) == "X":
        return "X"
    elif check_three(board, 0, 1, 2) == "O":
        return "0"
    
    if check_three(board, 3, 4, 5) == "X":
        return "X"
    elif check_three(board, 3, 4, 5) == "O":
        return "0"

    if check_three(board, 6, 7, 8) == "X":
        return "X"
    elif check_three(board, 6, 7, 8) == "O":
        return "0"

    if check_three(board, 0, 3, 6) == "X":
        return "X"
    elif check_three(board, 0, 3, 6) == "O":
        return "0"
    
    if check_three(board, 1, 4, 7) == "X":
        return "X"
    elif check_three(board, 1, 4, 7) == "O":
        return "0"
    
    if check_three(board, 2, 5, 8) == "X":
        return "X"
    elif check_three(board, 2, 5, 8) == "O":
        return "O"
     
    if check_three(board, 2, 4, 6) == "X":
        return "X"
    elif check_three(board, 2, 4, 6) == "O":
        return "O"
    
    if check_three(board, 0, 4, 8) == "X":
        return "X"
    elif check_three(board, 0, 4, 8) == "O":
        return "O"
    
    if (open_spots(board)):
        return "-"
    else:
        return "D"
    

def tic_tac_toe():
    choice = "X"
    turn = 0 
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    while winner(board) == "-":
        random_move(board, choice)
        turn += 1
        if turn % 2 == 0:
            choice = "X"
        else:
            choice = "O"

    if winner(board) == "X":
        return "X"
    elif winner(board) == "O":
        return "O"
    else:
        return "D"


def play100():
    xWins = 0
    oWins = 0
    Draws = 0
    for i in range (101):
        result = tic_tac_toe()
        if result == "X":
            xWins += 1
        elif result == "O":
            oWins += 1
        else:
            Draws += 1
    
    print(f'X Wins: {xWins}')
    print(f'O Wins: {oWins}')
    print(f'Draws: {Draws}')


if __name__ == '__main__':
    play100()
 


