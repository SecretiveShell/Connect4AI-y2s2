from abc import ABC, abstractmethod

class genericAgent(ABC):
    """Generic agent class"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_action(self, board) -> int:
        """Returns the column index of the action to take"""
        pass

