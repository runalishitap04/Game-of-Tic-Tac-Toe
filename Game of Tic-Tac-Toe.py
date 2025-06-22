import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, diagonals for a win
    win_conditions = [
        # rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That spot is already taken, choose another.")
        except ValueError:
            print("Please enter a valid number.")

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = "O"
    print(f"Computer placed an O in position {move[0]*3 + move[1] + 1}")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, computer is O.")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
