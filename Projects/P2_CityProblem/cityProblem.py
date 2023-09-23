# Author: Derek Dorr
# Class: CPSC 535 - Advanced Algorithms

# Inputs
city_distances = [5, 25, 15, 10, 15]
city_fuel = [1, 2, 1, 0, 3]
mpg = 10

FAILED_TO_FIND = -1


def city_problem():

    # Test each city for possible best starting city
    for x, i in enumerate(city_distances):

        # Check if current city has enough fuel to get us to the next city
        if mpg * city_fuel[x] >= i:
            print(f"Able to drive from {x} to {(x + 1) % len(city_distances)}")

            # Start driving from current city
            preferred_city = drive_cities(x, 0, x)

            # If preferred city is found, return immediately
            if preferred_city:
                return x

        # Not enough gas to leave current city
        else:
            print(f"not enough gas at {x}")

    # In case of failure
    return FAILED_TO_FIND


def drive_cities(current_city, gas_reserves, starting_city):

    print("Arrived at: ", current_city)
    # Fuel up upon reaching each city
    fuel_up = gas_reserves + (mpg * city_fuel[current_city])

    # If you have enough fuel to get to the next city, then drive
    if fuel_up >= city_distances[current_city]:

        # Loop around if currently at the last city
        if (current_city + 1) % len(city_distances) != starting_city:

            # Determine how much gas will be used driving to next city
            drive_cost = fuel_up - city_distances[current_city]
            next_city = (current_city + 1) % len(city_distances)

            # Drive to next city
            return drive_cities(next_city, drive_cost, starting_city)

        # Next city will make a full loop! End the search
        else:
            return True

    # Not enough gas to drive to next city
    else:
        return False


if __name__ == '__main__':

    # Run the algorithm
    preferred_starting_city = city_problem()

    # Check for algorithm failure
    if preferred_starting_city != FAILED_TO_FIND:
        print(f"{preferred_starting_city} is the preferred starting city!")
    else:
        print("failed to find a good starting city :(")