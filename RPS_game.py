def play_round(player1, player2):
    # This function simulates a single round of the game
    p1_move = player1("")  # Player 1 moves
    p2_move = player2("")  # Player 2 moves

    if p1_move == p2_move:
        return 0  # Tie
    elif (p1_move == "R" and p2_move == "S") or \
         (p1_move == "P" and p2_move == "R") or \
         (p1_move == "S" and p2_move == "P"):
        return 1  # Player 1 wins
    else:
        return -1  # Player 2 wins

def play(player1, player2, num_games, verbose=False):
    p1_wins = 0
    p2_wins = 0
    ties = 0

    for i in range(num_games):
        result = play_round(player1, player2)
        if result == 1:
            p1_wins += 1
            if verbose:
                print(f"Game {i+1}: Player 1 wins! (P1: {player1}, P2: {player2})")
        elif result == -1:
            p2_wins += 1
            if verbose:
                print(f"Game {i+1}: Player 2 wins! (P1: {player1}, P2: {player2})")
        else:
            ties += 1
            if verbose:
                print(f"Game {i+1}: It's a tie! (P1: {player1}, P2: {player2})")

    return p1_wins, p2_wins, ties
