from connect4ai_y2s2.gameloop import gameloop
from connect4ai_y2s2.agentPicker import get_agent_options, agentPicker

def main() -> None:
    """Main function for the game"""
    
    print(get_agent_options())
    agent1 = agentPicker(input("Enter agent 1 type: "))
    agent2 = agentPicker(input("Enter agent 2 type: "))

    gameloop(agent1, agent2)
    
    print("exiting...")
