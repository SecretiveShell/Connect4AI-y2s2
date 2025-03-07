from abc import ABC, abstractmethod
from connect4ai_y2s2.board import playerType

class genericAgent(ABC):
    """Generic agent class"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_action(self, board, player: playerType) -> int:
        """Returns the column index of the action to take"""
        pass

