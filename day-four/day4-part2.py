def is_overlapped(pair1, pair2):
    if (pair2[0] <= pair1[0] <= pair2[1] or pair2[0] <= pair1[1] <= pair2[1]) or (
            pair1[0] <= pair2[0] <= pair1[1] or pair1[0] <= pair2[1] <= pair1[1]):
        return True
    return False


with open('day4.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        pair = line.strip()
        #     count += solve_riddle(pair)
        # #
        # print(count)
        shift = pair.split(",")
        shifts = [shift[0].split("-"), shift[1].split("-")]
        pair1 = [int(shifts[0][0]),int(shifts[0][1])]
        pair2 = [int(shifts[1][0]), int(shifts[1][1])]
        containedInRange = (is_overlapped(pair1, pair2))
        if containedInRange:
            count += 1
    print(count)

