with open('day1.txt') as f:
    lines = f.readlines()
    calories = [0]
    for line in lines:
        number = line.strip()
        if number != "":
            calories[-1] += int(number)
        else:
            calories.append(0)
    print(max(calories))
