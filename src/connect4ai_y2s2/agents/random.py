from connect4ai_y2s2.agents.generic import genericAgent
from random import choice
from connect4ai_y2s2.board import Board, playerType

class randomAgent(genericAgent):
    """Random agent"""

    def __init__(self):
        pass
    
    def get_action(self, board: Board, player: playerType) -> int:
        """Returns the column index of the action to take"""
        return choice(board.get_valid_moves())