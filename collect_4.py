import numpy as np

def check_winner(board: np.ndarray) -> bool:
    """
    Checks for a winner in the Connect-4 game.
    Args:
        board (np.ndarray): The game board (2D array).
    Returns:
        bool: True if a winner is found, otherwise False.
    """
    rows, cols = board.shape

    # Check horizontal win
    for row in range(rows):
        for col in range(cols - 3):
            if (
                board[row, col] != 0 and
                np.all(board[row, col] == board[row, col:col + 4])
            ):
                print(f'Player {board[row, col]} wins the game!')
                return True

    # Check vertical win
    for col in range(cols):
        for row in range(rows - 3):
            if (
                board[row, col] != 0 and
                np.all(board[row, col] == board[row:row + 4, col])
            ):
                print(f'Player {board[row, col]} wins the game!')
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if (
                board[row, col] != 0 and
                board[row, col] == board[row + 1, col + 1] ==
                board[row + 2, col + 2] == board[row + 3, col + 3]
            ):
                print(f'Player {board[row, col]} wins the game!')
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if (
                board[row, col] != 0 and
                board[row, col] == board[row - 1, col + 1] ==
                board[row - 2, col + 2] == board[row - 3, col + 3]
            ):
                print(f'Player {board[row, col]} wins the game!')
                return True

    return False


def drop_disc(board: np.ndarray, col: int, player: int) -> bool:
    """
    Drops a disc for a player in the specified column.
    Args:
        board (np.ndarray): The game board (2D array).
        col (int): The column where the disc is dropped.
        player (int): The player number (1 or 2).
    Returns:
        bool: True if the disc was successfully dropped, False if the column is full.
    """
    for row in range(board.shape[0] - 1, -1, -1):
        if board[row, col] == 0:
            board[row, col] = player
            return True
    print(f"Column {col + 1} is full. Choose a different column.")
    return False


def main():
    # Initialize game
    rows, cols = 6, 7
    board = np.zeros((rows, cols), dtype=int)
    current_player = 1

    print("Welcome to Connect-4!")
    print(board)

    while True:
        try:
            # Get user input
            col = int(input(f"Player {current_player}, choose a column (1-{cols}): ")) - 1
            if col < 0 or col >= cols:
                print(f"Invalid input. Please choose a column between 1 and {cols}.")
                continue

            # Drop the disc
            if drop_disc(board, col, current_player):
                print(board)
                if check_winner(board):
                    break

                # Switch players
                current_player = 3 - current_player  # Alternates between 1 and 2

        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Game over! Thanks for playing.")


if __name__ == "__main__":
    main()
