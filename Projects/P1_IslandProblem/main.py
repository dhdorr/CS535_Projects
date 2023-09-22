land_locations = []


def island_problem(input):
    water_locations = []
    # Loop through input and find all water locations
    for y, i in enumerate(input):
        for x, j in enumerate(i):
            if j == 1:
                # Get the x and y coordinates of the water and determine its weight
                # Weight is the sum of lands adjacent to that water
                water_temp = {"x": x, "y": y, "weight": calculate_water_weight(x, y, input)}

                # If water has at least 1 adjacent land, add to list
                if water_temp["weight"] > 0:
                    water_locations.append(water_temp)

    # Loop through all saved water locations, try turning them into land
    land_max = 0
    for w in water_locations:
        test_input = []

        # Create a copy of the input that can be modified
        for y, i in enumerate(input):
            test_input.append([])
            for j in i:
                test_input[y].append(j)

        # Turn water into land
        test_input[w["y"]][w["x"]] = 0

        # Loop through the modified test input
        for y, i in enumerate(test_input):
            for x, j in enumerate(i):

                # If on land, find longest sequence of land
                if j == 0:
                    global land_locations
                    land_locations = [[x, y]]

                    # Walk the 2-D Matrix to find longest continuous path
                    land_count = walk_list(x, y, test_input, 1)

                    # Track longest continuous path size
                    if land_count > land_max:
                        land_max = land_count

    return land_max


# Recursively walk through the 2-D Matrix by looking left, right, up, and down
def walk_list(x, y, input, sum):
    global land_locations
    # Ensure next step's coordinates are not already visited or out of bounds

    # look left
    if (x - 1) >= 0 and not [x-1, y] in land_locations:
        if input[y][x-1] == 0:
            # Keep track of visited lands
            land_locations.append([x - 1, y])

            sum = walk_list(x-1, y, input, 1 + sum)

    # look right
    if (x + 1) < len(input[y]) and not [x + 1, y] in land_locations:
        if input[y][x + 1] == 0:
            # Keep track of visited lands
            land_locations.append([x + 1, y])

            sum = walk_list(x+1, y, input, 1 + sum)

    # look up
    if (y - 1) >= 0 and not [x, y-1] in land_locations:
        if input[y-1][x] == 0:
            # Keep track of visited lands
            land_locations.append([x, y - 1])

            sum = walk_list(x, y-1, input, 1 + sum)

    # look down
    if (y + 1) < len(input) and not [x, y+1] in land_locations:
        if input[y+1][x] == 0:
            # Keep track of visited lands
            land_locations.append([x, y + 1])

            sum = walk_list(x, y+1, input, 1 + sum)

    return sum


# Determine the weight of a water square by counting adjacent lands
def calculate_water_weight(x, y, input):
    weight = 0
    # Ensure next step's coordinates are not already visited or out of bounds

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
    # Inputs #
    algo_1_input_1 = [
        [0, 1, 1],
        [0, 0, 1],
        [1, 1, 0]
    ]

    algo_1_input_2 = [
        [1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0]
    ]

    print("original input: ", algo_1_input_1)
    size = island_problem(algo_1_input_1)
    print("Island Size = ", size)

