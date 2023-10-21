

def take3(durations, stations):
    sol_list = []
    matrix = []
    masterList = []

    # Build a matrix of possible element counts.
    for j in range(len(durations) - (stations - 1)):
        # Any given station can have 1, 2 or 3 tasks
        sol_list.append(j + 1)

    # Build a matrix of all possible combinations of tasks per station
    # I.E. [[1],[1],[1]] ... [[3],[3],[3]] and everything in between
    for i in range(1, stations + 1):
        matrix += [[i, a, b] for a in range(1, stations + 1) for b in sol_list if (i + a + b) == len(durations)]

    # Using the precomputed tasks per station matrix, create a new matrix using the tasks available
    # I.E. [[1][1][3]] --> [[15],[15],[30,30,45]]
    for i, m in enumerate(matrix):
        # Track start position for the tasks to assign each station.
        itr = 0
        temp_list = []

        for j, n in enumerate(m):
            temp_list.append(durations[itr:itr + n])
            # n represents the number of tasks, so jump the start position by the number of tasks assigned
            itr += n
        # Keep all possible configurations for task/station allocation
        masterList.append(temp_list)

    master_dict = build_pruned_dict(masterList)

    maxNo = 0
    totals_dict = {}

    # Get the maximum flow value of each valid station/task configuration.
    for f in master_dict.keys():
        for g in master_dict[f]:
            helpMe = sum(g)
            if helpMe > maxNo:
                maxNo = helpMe
        totals_dict[f] = maxNo

    min_pos = 0

    a = min(totals_dict.values())

    for k in totals_dict.keys():
        if totals_dict[k] == a:
            min_pos = k

    return {"station_config": master_dict[min_pos], "longest_duration": a}

def build_pruned_dict(master_list):
    build_dict = {}

    # Discard configuration if:
    # 1) if next element in station(i) tasks > current element AND sum(0, current element) < next element
    # 2) sum of station tasks durations < the duration of the next station's first task.
    for idx, m in enumerate(master_list):
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
            build_dict[idx] = m
    return build_dict


if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3

    answer = take3(durations, stations)
    print(answer)