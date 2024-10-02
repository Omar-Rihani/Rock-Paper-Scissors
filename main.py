from RPS import player
from RPS_game import play

# Example bot strategy
def bot1(prev_play, opponent_history=[]):
    return "R"  # Always plays Rock

def bot2(prev_play, opponent_history=[]):
    return "P"  # Always plays Paper

def bot3(prev_play, opponent_history=[]):
    return "S"  # Always plays Scissors

def bot4(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])  # Random bot

if __name__ == "__main__":
    # Play against different bots
    for bot in [bot1, bot2, bot3, bot4]:
        print(f"\nPlaying against {bot.__name__}:")
        wins, losses, ties = play(player, bot, 1000, verbose=True)
        print(f"Results: Player Wins: {wins}, Bot Wins: {losses}, Ties: {ties}")
