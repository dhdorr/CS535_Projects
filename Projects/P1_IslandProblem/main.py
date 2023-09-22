ogX = 0
ogY = 0
land_copy = []

def island_problem(input):
    input_copy = input
    copy_2 = input
    water_locations = []
    land_locations = []
    land_count = 0
    weight_max = 0

    for y, i in enumerate(input_copy):
        for x, j in enumerate(i):
            if j == 1:
                water_temp = {"x": x, "y": y, "weight": calculate_water_weight(x, y, input_copy)}
                if water_temp["weight"] > 0:
                    # weight_max = water_temp["weight"]
                    water_locations.append(water_temp)
                    print(water_locations)

    land_max = 0
    for w in water_locations:
        test = []

        for y, i in enumerate(input):
            test.append([])
            for j in i:
                test[y].append(j)

        test[w["y"]][w["x"]] = 0
        # print("test: ", test)

        for y, i in enumerate(test):
            for x, j in enumerate(i):
                if j == 0:
                    global land_copy
                    land_copy = [[x, y]]
                    land_count = walk_list([[x, y]], x, y, test, 1)
                    if land_count > land_max:
                        land_max = land_count
                        print("hit max at: ", w, " ", j)

        # land_count = walk_list([], w["x"], w["y"], copy_2, 0)

    print("water stats: ", water_locations)
    return land_max


def walk_list(land, x, y, input, sum):
    # land_copy = land.copy()
    global land_copy
    #land_copy = []
    # for help, i in enumerate(land):
    #     land_copy.append([])
    #     for j in i:
    #         land_copy[help].append(j)
    # print("land list: ", land_copy)

    # look left
    if (x - 1) >= 0 and not [x-1, y] in land_copy:
        # print("x: ", x - 1)
        if input[y][x-1] == 0:
            # print("left ", [x-1, y])
            land_copy.append([x-1, y])
            # print("post append land: ", land_copy)
            # return sum + walk_list(land_copy, x-1, y, input, 1)
            sum = walk_list(land_copy, x-1, y, input, 1 + sum)
    # look right
    if (x + 1) < len(input[y]) and not [x + 1, y] in land_copy:
        if input[y][x + 1] == 0:
            # print("right ", [x + 1, y])
            land_copy.append([x + 1, y])
            # print("post append land: ", land_copy)
            # return sum + walk_list(land_copy, x+1, y, input, 1)
            sum = walk_list(land_copy, x+1, y, input, 1 + sum)

    # look up
    if (y - 1) >= 0 and not [x, y-1] in land_copy:
        if input[y-1][x] == 0:
            # print("up ", [x, y-1])
            land_copy.append([x, y-1])
            # print("post append land: ", land_copy)
            # return sum + walk_list(land_copy, x, y-1, input, 1)
            sum = walk_list(land_copy, x, y-1, input, 1 + sum)
    # look down
    if (y + 1) < len(input) and not [x, y+1] in land_copy:
        if input[y+1][x] == 0:
            # print("down ", [x, y+1])
            land_copy.append([x, y+1])
            # print("post append land: ", land_copy)
            # return sum + walk_list(land_copy, x, y+1, input, 1)
            sum = walk_list(land_copy, x, y+1, input, 1 + sum)

    return sum


def calculate_water_weight(x, y, input):
    weight = 0
    # look left
    if (x - 1) >= 0:
        if input[y][x-1] == 0:
            weight += 1

    # look right
    if (x + 1) < len(input[y]):
        if input[y][x + 1] == 0:
            weight += 1

    # look up
    if (y - 1) >= 0:
        if input[y-1][x] == 0:
            weight += 1

    # look down
    if (y + 1) < len(input):
        if input[y+1][x] == 0:
            weight += 1

    return weight


if __name__ == '__main__':
    algo_1_input_1 = [
        [0,1,1],
        [0,0,1],
        [1,1,0]
    ]

    algo_1_input_2 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    algo_1_input_3 = [
        [1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0]
    ]

    print("original input: ", algo_1_input_1)
    size = island_problem(algo_1_input_1)
    print(size)

