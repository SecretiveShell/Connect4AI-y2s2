from typing import Literal, TypeAlias
import numpy as np

playerType: TypeAlias = Literal["X", "O"]

class Board:
    def __init__(self, state: np.ndarray | None = None):
        """Initializes the board. If no state is provided, creates an empty 6x7 board."""
        if state is None:
            self.state: np.ndarray = np.full((6, 7), None, dtype=object)
        else:
            self.state = state

    def display(self):
        """Displays the board in a readable format."""
        for row in self.state:
            print(" | ".join(cell if cell is not None else " " for cell in row))
            print("-" * 25)

    def get_valid_moves(self) -> list[int]:
        """Returns a list of valid column indices where a move can be made."""
        return [col for col in range(7) if self.state[0, col] is None]

    def make_move(self, col: int, player: playerType) -> bool:
        """Takes an action and updates the board state. Drops a piece into the selected column.
        
        Returns True if successful, False if the column is full or out of bounds.
        """
        if col < 0 or col >= 7 or self.state[0, col] is not None:
            return False

        for row in range(5, -1, -1):
            if self.state[row, col] is None:
                self.state[row, col] = player
                return True
        return False

    def is_game_over(self) -> bool:
        """Returns True if the game is over (either a player has won or no valid moves remain)."""
        return self.is_winner("X") or self.is_winner("O") or len(self.get_valid_moves()) == 0

    def is_winner(self, player: playerType) -> bool:
        """Checks if the given player has won the game."""
        for r in range(6):
            for c in range(7):
                if (self.check_line(r, c, 1, 0, player) or  # Vertical
                    self.check_line(r, c, 0, 1, player) or  # Horizontal
                    self.check_line(r, c, 1, 1, player) or  # Diagonal down-right
                    self.check_line(r, c, 1, -1, player)):  # Diagonal down-left
                    return True
        return False

    def check_line(self, r: int, c: int, dr: int, dc: int, player: playerType) -> bool:
        """Checks if a line of length 4 is in a row."""
        count = 0
        for i in range(4):
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < 6 and 0 <= nc < 7 and self.state[nr, nc] == player:
                count += 1
            else:
                break
        return count == 4

if __name__ == "__main__":
    board = Board()
    board.display()

    print("Valid Moves:", board.get_valid_moves())
    print("Game Over:", board.is_game_over())
    print("X is Winner:", board.is_winner("X"))
    print("O is Winner:", board.is_winner("O"))
