from connect4ai_y2s2.gameloop import gameloop, headless_gameloop
from connect4ai_y2s2.agentPicker import get_agent_options, agentPicker

def main() -> None:
    """Main function for the game"""
    
    print(get_agent_options())
    agent1 = agentPicker(input("Enter agent 1 type: "))
    agent2 = agentPicker(input("Enter agent 2 type: "))

    num_games = int(input("Enter number of games to play: ") or "1")

    if num_games == 1:
        gameloop(agent1, agent2)
        return
    
    else:
        # collect results
        games = []
        print("Playing... ", end="")
        for i in range(num_games):
            games.append(headless_gameloop(agent1, agent2))
            print(f"{i+1} ", end="")
        print()

        # show analysis
        X_wins = len(list(filter(lambda x: x == "X", games)))
        O_wins = len(list(filter(lambda x: x == "O", games)))

        print(f"X wins: {X_wins}")
        print(f"O wins: {O_wins}")
