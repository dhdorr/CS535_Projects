# Author: Derek Dorr
# Class: CPSC 535 - Advanced Algorithms
# Project 1
# Problem 1 - Island Problem

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

            # If the water has at least 1 adjacent land, test it
            if tile == WATER and water_has_adjacent_land(x, y):
                land_size = get_new_world_best_score(x, y)

                # Track longest continuous path size
                if land_size > land_max:
                    land_max = land_size

    return land_max


def get_new_world_best_score(x, y):
    global visited_lands
    land_max = 0

    modified_world = []
    # Create a copy of the WORLD that can be modified
    for ty, row in enumerate(WORLD):
        modified_world.append([])
        for tx, tile in enumerate(row):
            modified_world[ty].append(tile)

            # If current indices == input WATER indices, set WATER to LAND
            if ty == y and tx == x:
                modified_world[ty][tx] = LAND

    # Loop through elements of modified_world
    for ty, row in enumerate(modified_world):
        for tx, tile in enumerate(row):

            # If on land and haven't visited this land, reset visited_lands
            if tile == LAND and [tx, ty] not in visited_lands:
                visited_lands = [[x, y]]

                # Walk modified_world to find longest continuous path of lands
                land_count = walk_list(x, y, modified_world, 1)

                # Track maximum path size
                if land_count > land_max:
                    land_max = land_count

    return land_max


# Walk through the modified WORLD by looking left, right, up, and down
def walk_list(x, y, modified_world, land_count):
    global visited_lands
    # Ensure next step's coordinates are not already visited or out of bounds
    # If able, move to next tile

    # look left
    if (x - 1) >= 0 and not [x-1, y] in visited_lands:
        if modified_world[y][x-1] == 0:
            # Keep track of visited lands
            visited_lands.append([x - 1, y])

            land_count = walk_list(x-1, y, modified_world, 1 + land_count)

    # look right
    if (x + 1) < len(modified_world[y]) and not [x + 1, y] in visited_lands:
        if modified_world[y][x + 1] == 0:
            # Keep track of visited lands
            visited_lands.append([x + 1, y])

            land_count = walk_list(x+1, y, modified_world, 1 + land_count)

    # look up
    if (y - 1) >= 0 and not [x, y-1] in visited_lands:
        if modified_world[y-1][x] == 0:
            # Keep track of visited lands
            visited_lands.append([x, y - 1])

            land_count = walk_list(x, y-1, modified_world, 1 + land_count)

    # look down
    if (y + 1) < len(modified_world) and not [x, y+1] in visited_lands:
        if modified_world[y+1][x] == 0:
            # Keep track of visited lands
            visited_lands.append([x, y + 1])

            land_count = walk_list(x, y+1, modified_world, 1 + land_count)

    return land_count


# Determine if water has adjacent lands
def water_has_adjacent_land(x, y):
    # Ensure next step's coordinates are not already visited or out of bounds
    # Immediately return if a land is found

    # look left
    if (x - 1) >= 0:
        if WORLD[y][x-1] == 0:
            return True

    # look right
    if (x + 1) < len(WORLD[y]):
        if WORLD[y][x + 1] == 0:
            return True

    # look up
    if (y - 1) >= 0:
        if WORLD[y-1][x] == 0:
            return True

    # look down
    if (y + 1) < len(WORLD):
        if WORLD[y+1][x] == 0:
            return True

    return False


if __name__ == '__main__':
    print("original input: ", WORLD)

    # Run the algorithm
    size = island_problem()
    print("Best Island Size = ", size)

