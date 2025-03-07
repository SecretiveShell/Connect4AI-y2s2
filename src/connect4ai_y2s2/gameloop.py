from connect4ai_y2s2.board import Board
from connect4ai_y2s2.agents.generic import genericAgent

def gameloop(agent1: genericAgent, agent2: genericAgent) -> None:
    """Game loop for the game"""

    board = Board()

    while not board.is_game_over():
        print("Player 1's turn")
        action = agent1.get_action(board)
        board.make_move(action, "X")
        board.display()
        input("Press Enter to continue...")

        print("Player 2's turn")
        action = agent2.get_action(board)
        board.make_move(action, "O")
        board.display()
        input("Press Enter to continue...")

    if board.is_winner("X"):
        print("Player 1 wins!")
    elif board.is_winner("O"):
        print("Player 2 wins!")
    else:
        print("It's a tie!")
