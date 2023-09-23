# Author: Derek Dorr
# Class: CPSC 535 - Advanced Algorithms

# Inputs
# WORLD = [
#         [0, 1, 1],
#         [0, 0, 1],
#         [1, 1, 0]
# ]

WORLD = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0]
]

visited_lands = []
WATER = 1
LAND = 0


def island_problem():
    land_max = 0
    # Loop through input and find all water locations
    for y, row in enumerate(WORLD):
        for x, tile in enumerate(row):
            if tile == WATER:
                # Weight is the sum of lands adjacent to that water
                weight = calculate_water_weight(x, y)

                # If the water has at least 1 adjacent land, test it
                if weight > 0:
                    land_size = get_new_world_best_score(x, y)

                    # Track longest continuous path size
                    if land_size > land_max:
                        land_max = land_size

    return land_max


def get_new_world_best_score(x, y):
    global visited_lands
    land_max = 0

    modified_world = []
    # Create a copy of the input that can be modified
    for ty, row in enumerate(WORLD):
        modified_world.append([])
        for tx, tile in enumerate(row):
            modified_world[ty].append(tile)
            if ty == y and tx == x:
                modified_world[ty][tx] = 0

    # Loop through elements of modified_world
    for ty, row in enumerate(modified_world):
        for tx, tile in enumerate(row):

            # If on land and haven't visited this land, reset visited_lands
            if tile == LAND and [tx, ty] not in visited_lands:
                visited_lands = [[x, y]]

                # Walk modified_world to find longest continuous path of lands
                land_count = walk_list(x, y, modified_world, 1)

                # Track longest continuous path size
                if land_count > land_max:
                    land_max = land_count

    return land_max


# Walk through the modified WORLD by looking left, right, up, and down
def walk_list(x, y, input, sum):
    global visited_lands
    # Ensure next step's coordinates are not already visited or out of bounds
    #
    # look left
    if (x - 1) >= 0 and not [x-1, y] in visited_lands:
        if input[y][x-1] == 0:
            # Keep track of visited lands
            visited_lands.append([x - 1, y])

            sum = walk_list(x-1, y, input, 1 + sum)

    # look right
    if (x + 1) < len(input[y]) and not [x + 1, y] in visited_lands:
        if input[y][x + 1] == 0:
            # Keep track of visited lands
            visited_lands.append([x + 1, y])

            sum = walk_list(x+1, y, input, 1 + sum)

    # look up
    if (y - 1) >= 0 and not [x, y-1] in visited_lands:
        if input[y-1][x] == 0:
            # Keep track of visited lands
            visited_lands.append([x, y - 1])

            sum = walk_list(x, y-1, input, 1 + sum)

    # look down
    if (y + 1) < len(input) and not [x, y+1] in visited_lands:
        if input[y+1][x] == 0:
            # Keep track of visited lands
            visited_lands.append([x, y + 1])

            sum = walk_list(x, y+1, input, 1 + sum)

    return sum


# Determine the weight of a water square by counting adjacent lands
def calculate_water_weight(x, y):
    weight = 0
    # Ensure next step's coordinates are not already visited or out of bounds

    # look left
    if (x - 1) >= 0:
        if WORLD[y][x-1] == 0:
            weight += 1

    # look right
    if (x + 1) < len(WORLD[y]):
        if WORLD[y][x + 1] == 0:
            weight += 1

    # look up
    if (y - 1) >= 0:
        if WORLD[y-1][x] == 0:
            weight += 1

    # look down
    if (y + 1) < len(WORLD):
        if WORLD[y+1][x] == 0:
            weight += 1

    return weight


if __name__ == '__main__':
    print("original input: ", WORLD)

    # Run the algorithm
    size = island_problem()
    print("Island Size = ", size)

