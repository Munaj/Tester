board = [" " for i in range(9)]

def print_board():
    row1 = f"|{board[0]}|{board[1]}|{board[2]}|"
    row2 = f"|{board[3]}|{board[4]}|{board[5]}|"
    row3 = f"|{board[6]}|{board[7]}|{board[8]}|"
    print(row1)
    print(row2)
    print(row3)

print_board()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print(f"Your turn player {number}.")
    choice = int(input("Enter your move(1-9): ").strip())
    if board[choice -1 ] == " ":
        board[choice-1] = icon
    else:
        print("!!!This place is taken!!!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[5] == icon):
       return True
    else:
       return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False


while True:
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins!")
        break
    elif is_draw():
        print("is draw")
        break
    player_move("O")
    print_board()
    if is_victory("O"):
        print("O Wins!")
        break
