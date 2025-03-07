from typing import Literal, TypeAlias
import numpy as np

playerType: TypeAlias = Literal["X", "O"]

class Board:
    def __init__(self, state: np.ndarray | None = None):
        if state is None:
            self.state: np.ndarray = np.full((8, 8), None, dtype=object)
        else:
            self.state = state

    def display(self):
        """Displays the board in a readable format."""
        for row in self.state:
            print(" | ".join(cell if cell is not None else " " for cell in row))
            print("-" * 31)

    def get_valid_moves(self) -> tuple[int, ...]:
        """list rows you can go in"""
        rows = []
        for index, row in enumerate(self.state):
            if None in row.tolist():
                rows.append(index)
        return tuple(rows)
    

if __name__ == "__main__":
    board = Board()
    board.display()
    print(board.get_valid_moves())