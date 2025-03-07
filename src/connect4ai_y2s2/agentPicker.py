from textwrap import dedent
from connect4ai_y2s2.agents.generic import genericAgent
from connect4ai_y2s2.agents.random import randomAgent
from connect4ai_y2s2.agents.rules import rulesAgent

def get_agent_options() -> str:
    """Returns a list of available agent types"""

    return dedent("""
    Available agent types:
    r - Random agent
    s - Rules agent
""").strip()

def agentPicker(str) -> genericAgent:
    """Returns an agent based on the given string"""

    if str == "r":
        return randomAgent()
    if str == "s":
        return rulesAgent()
    else:
        raise ValueError("Invalid agent type")