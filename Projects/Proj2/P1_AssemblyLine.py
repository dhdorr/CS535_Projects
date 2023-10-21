

def take3(durations, stations):
    sol_list = []
    matrix = []
    masterList = []

    # Build a matrix of possible element counts.
    # In the example, durations.len = 5 & stations = 3
    # So the max number of tasks a station can have is 3 ((5 - (3 - 1)) = 3)
    for j in range(len(durations) - (stations - 1)):
        # Any given station can have 1, 2 or 3 tasks
        sol_list.append(j + 1)

    # Build a matrix of all possible combinations of tasks per station
    # I.E. [[1],[1],[1]] ... [[3],[3],[3]] and everything in between
    for i in range(1, stations + 1):
        res = [[i, a, b] for a in range(1, stations + 1) for b in sol_list]
        for r in res:
            # Only keep station/tasks configuration if the total number of station tasks = number of tasks available
            # I.E. discard [[1],[1],[1]] & [[3],[3],[3]] because 1 + 1 + 1 = 3 < 5. And 3 + 3 + 3 = 9 > 5.
            if sum(r) == len(durations):
                # Each element in the matrix, i, represents the amount of tasks that station(i) has.
                matrix.append(r)
    # Using the precomputed tasks per station matrix, create a new matrix using the tasks available
    # Tasks are always in the order given.
    # I.E. [[1][1][3]] --> [[15],[15],[30,30,45]]
    for i, m in enumerate(matrix):
        # Track start position for the tasks to assign each station.
        itr = 0
        testList = []

        for j, n in enumerate(m):
            testList.append(durations[itr:itr + n])

            # n represents the number of tasks, so jump the start position by the number of tasks assigned
            itr += n

        # Keep all possible configurations for task/station allocation
        masterList.append(testList)

    # Get rid of configurations that are invalid
    my_list = prune_list(masterList)

    maxNo = 0
    totals_list = []

    # Get the maximum flow value of each valid station/task configuration.
    for f in my_list:
        for g in f:
            helpMe = sum(g)
            if helpMe > maxNo:
                maxNo = helpMe
        totals_list.append(maxNo)

    min_total = totals_list[0]
    min_pos = 0

    # Of all maximal flows, get the minimum flow.
    for i, t in enumerate(totals_list):
        if t < min_total:
            min_total = t
            min_pos = i

    print("optimized assembly line: ", my_list[min_pos])
    print("optimized max wait: ", min_total)


# Given a list of all possible assembly line configurations
# Prune out all bad configurations
def prune_list(master_list):
    build_list = []

    # Discard configuration tuple if:
    # 1) m[i][j] < m[i][j + 1] and sum(m[i][0:j+1]) < m[i][j+1])
    #       if next element in station(i) tasks > current element AND sum(0, current element) < next element
    # 2) sum(m[i]) < m[i + 1][0]
    #       sum of station tasks durations < the duration of the next station's first task.
    for m in master_list:
        discard_me = False
        for i in range(len(m)):
            for j in range(len(m[i])):
                if j + 1 < len(m[i]):
                    if m[i][j] < m[i][j+1] and sum(m[i][0:j+1]) < m[i][j+1]:
                        discard_me = True
                if i + 1 < len(m):
                    if sum(m[i]) < m[i + 1][0]:
                        discard_me = True
        if not discard_me:
            build_list.append(m)
    return build_list


if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3

    take3(durations, stations)