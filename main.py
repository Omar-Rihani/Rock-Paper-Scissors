import random

# Initialize a history list to keep track of opponent's moves
opponent_history = []

def player(prev_play, opponent_history=[]):
    # Store opponent's last move
    if prev_play:
        opponent_history.append(prev_play)

    # If it's the first move, return a random choice
    if not opponent_history:
        return random.choice(['R', 'P', 'S'])

    # Analyze the opponent's last move
    last_opponent_move = opponent_history[-1]

    # Use simple counter-strategy based on opponent's last move
    if last_opponent_move == 'R':
        return 'P'  # Paper beats Rock
    elif last_opponent_move == 'P':
        return 'S'  # Scissors beats Paper
    elif last_opponent_move == 'S':
        return 'R'  # Rock beats Scissors

    # Optionally add more complex strategies here

    # For safety, return a random choice if something goes wrong
    return random.choice(['R', 'P', 'S'])

