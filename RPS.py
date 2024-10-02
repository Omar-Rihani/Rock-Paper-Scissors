import random

def player(prev_play, opponent_history=[]):
    # Keep track of the opponent's history
    opponent_history.append(prev_play)
    
    if len(opponent_history) == 0:  # First game
        return random.choice(["R", "P", "S"])

    # Simple strategy: counter the opponent's last move
    if prev_play == "R":
        return "P"  # Paper beats Rock
    elif prev_play == "P":
        return "S"  # Scissors beat Paper
    elif prev_play == "S":
        return "R"  # Rock beats Scissors

    # Random choice if the previous move is empty or invalid
    return random.choice(["R", "P", "S"])
