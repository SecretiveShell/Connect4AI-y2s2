from random import choice
from connect4ai_y2s2.agents.generic import genericAgent
from connect4ai_y2s2.board import Board, playerType

class rulesAgent(genericAgent):
    """Rules agent"""

    def __init__(self):
        pass
    
    def get_action(self, board: Board, player: playerType) -> int:
        """Returns the column index of the action to take"""
        valid_moves = board.get_valid_moves()
        
        # if a move wins then take it
        for col in valid_moves:
            temp = board.copy()
            temp.make_move(col, player)
            if temp.is_winner(player):
                return col

        # take middle column if possible
        if 3 in valid_moves:
            return 3
        
        # fallback to random
        return choice(valid_moves)