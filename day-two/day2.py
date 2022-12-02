def get_game_points(your_move, opponent_move):
    points = 0
    if your_move == "X":
        points += 1
        if opponent_move == "A":
            points += 3
        elif opponent_move == "C":
            points += 6
    elif your_move == "Y":
        points += 2
        if opponent_move == "B":
            points += 3
        elif opponent_move == "A":
            points += 6
    else:
        points += 3
        if opponent_move == "C":
            points += 3
        elif opponent_move == "B":
            points += 6
    return points


with open('day2.txt') as f:
    lines = f.readlines()
    games = []
    points = 0
    for line in lines:
        game = line.strip().split(" ")
        points += get_game_points(game[1], game[0])

    print(points)


