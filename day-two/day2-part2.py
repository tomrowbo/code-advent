def get_game_points(opponent_move, outcome):
    game_points = 0
    if outcome == "X":  # Lose
        game_points += 0
        if opponent_move == "A":  # Your move = scissors vs rock
            game_points += 3
        elif opponent_move == "B":  # Your move = rock vs paper
            game_points += 1
        else:  # Your move = paper vs scissors
            game_points += 2
    elif outcome == "Y":  # Draw
        game_points += 3
        if opponent_move == "A":  # Your move = rock vs rock
            game_points += 1
        elif opponent_move == "B":  # Your move = paper vs paper
            game_points += 2
        else:  # Your move = scissors vs scissors
            game_points += 3
    else:  # Win
        game_points += 6
        if opponent_move == "A":  # Your move = paper vs rock
            game_points += 2
        elif opponent_move == "B":  # Your move = scissors vs paper
            game_points += 3
        else:  # Your move = rock vs scissors
            game_points += 1
    return game_points


with open('day2.txt') as f:
    lines = f.readlines()
    games = []
    points = 0
    for line in lines:
        game = line.strip().split(" ")
        points += get_game_points(game[0], game[1])

    print(points)
