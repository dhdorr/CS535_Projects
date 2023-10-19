# Author: Derek Dorr
# Class: CPSC 535 - Advanced Algorithms
# Project 1
# Problem 1 - Island Problem


# EXAMPLE INPUTS
#
# WORLD = [
#         [0, 1, 1],
#         [0, 0, 1],
#         [1, 1, 0]
# ]
#
# WORLD = [
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 1, 1, 1, 1],
#     [1, 0, 1, 0, 0]
# ]
#
# WORLD = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]
#
# WORLD = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# CONSTANTS
WATER = 1
LAND = 0


def island_problem(world):
    # Problem will always have at least 1 LAND
    land_max = 1

    # Loop through input and find all water locations
    for y, row in enumerate(world):
        for x, tile in enumerate(row):

            # If the water has at least 1 adjacent land, change WATER tile to LAND
            if tile == WATER and water_has_adjacent_land(x, y):
                # Modify world
                world[y][x] = LAND

                # Find adjacent LAND size
                land_max = get_new_world_best_score(x, y, world, land_max)

                # Reset world
                world[y][x] = WATER

    # Return greatest possible Island Size for the input
    return land_max


def get_new_world_best_score(x, y, modified_world, land_max):
    # Loop through elements of modified_world
    for ty, row in enumerate(modified_world):
        for tx, tile in enumerate(row):
            visited_lands = []

            # If on land and haven't visited this land, reset visited_lands
            if tile == LAND and [tx, ty] not in visited_lands:
                visited_lands.append([x, y])

                # Walk modified_world to find longest continuous path of lands
                land_count = walk_list(x, y, modified_world, 1, visited_lands)

                # Track maximum path size
                if land_count > land_max:
                    land_max = land_count

    # Return greatest Island Size in modified WORLD
    return land_max


# Walk through the modified WORLD by looking left, right, up, and down
def walk_list(x, y, modified_world, land_count, visited_lands):
    # Ensure next step's coordinates are not already visited or out of bounds
    # If able, move to next tile

    # look left
    if (x - 1) >= 0 and not [x-1, y] in visited_lands:
        if modified_world[y][x-1] == 0:
            # Keep track of visited lands
            visited_lands.append([x - 1, y])

            land_count = walk_list(x-1, y, modified_world, 1 + land_count, visited_lands)

    # look right
    if (x + 1) < len(modified_world[y]) and not [x + 1, y] in visited_lands:
        if modified_world[y][x + 1] == 0:
            # Keep track of visited lands
            visited_lands.append([x + 1, y])

            land_count = walk_list(x+1, y, modified_world, 1 + land_count, visited_lands)

    # look up
    if (y - 1) >= 0 and not [x, y-1] in visited_lands:
        if modified_world[y-1][x] == 0:
            # Keep track of visited lands
            visited_lands.append([x, y - 1])

            land_count = walk_list(x, y-1, modified_world, 1 + land_count, visited_lands)

    # look down
    if (y + 1) < len(modified_world) and not [x, y+1] in visited_lands:
        if modified_world[y+1][x] == 0:
            # Keep track of visited lands
            visited_lands.append([x, y + 1])

            land_count = walk_list(x, y+1, modified_world, 1 + land_count, visited_lands)

    # Return length of Island Path
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
    # INPUT
    WORLD = [
        [1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0]
    ]
    print("original input: ", WORLD)

    # Run the algorithm
    size = island_problem(WORLD)
    print("Best Island Size = ", size)

