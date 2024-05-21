def print_board(board):
    """Function to print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    """Function to check if the given player has won."""
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]

    ]
    return [player, player, player] in win_conditions
def is_board_full(board):
    """Function to check if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid move. Please enter a number between 0 and 2.")
            continue
        if board[row][col] != " ":
            print("Invalid move. The cell is already occupied.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    main()
