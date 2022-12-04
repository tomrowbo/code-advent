ITEMS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


with open('day3.txt') as f:
    lines = f.readlines()
    games = []
    sum = 0
    for line in lines:
        bag = line.strip()
        compartment1, compartment2 = split_list(bag)
        commonLetters = set()
        for i in range(len(compartment1)):
            if compartment1[i] in compartment2:
                commonLetters.add(compartment1[i])
        value = ITEMS.index(commonLetters.pop())+1
        print(value)
        sum += value
    print(sum)

