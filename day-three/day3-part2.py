ITEMS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]

with open('day3.txt') as f:
    lines = f.readlines()
    compartments = []
    sum = 0
    for line in lines:
        bag = line.strip()
        compartments.append(bag)
    for i in range(0, len(compartments), 3):
        compartment1 = compartments[i]
        compartment2 = compartments[i + 1]
        compartment3 = compartments[i+2]
        commonLetters = set()
        for j in range(len(compartment1)):
            if compartment1[j] in compartment2 and compartment1[j] in compartment3:
                commonLetters.add(compartment1[j])
        value = ITEMS.index(commonLetters.pop()) + 1
        print(value)
        sum += value
    print(sum)
