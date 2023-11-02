# Derek Dorr
# CS535
# Project 2
# 11/1/2023

def optimize_assembly_line(durations, stations):
    sol_list = []
    matrix = []
    masterList = []
    max_durations_dict = {}

    # Create a list of the number of tasks any given station can have
    sol_list = [j+1 for j in range(len(durations) - (stations - 1))]

    # Build a matrix of all possible combinations of tasks per station
    # I.E. [[1],[1],[1]] ... [[3],[3],[3]] and everything in between
    for i in range(1, stations + 1):
        matrix += [[i, a, b] for a in range(1, stations + 1) for b in sol_list if (i + a + b) == len(durations)]

    # Using the precomputed tasks per station configuration matrix, apply the tasks available
    # I.E. [[1][1][3]] --> [[15],[15],[30,30,45]]
    for m in matrix:
        # Track start position for the tasks to assign each station.
        itr = 0
        temp_list = []

        # For every station, apply the list of task durations
        for n in m:
            temp_list.append(durations[itr:itr + n])
            # n is the number of tasks at the ith station, so jump the start position by n
            itr += n

        # Keep all possible configurations for task/station allocation
        masterList.append(temp_list)

    # Discard invalid configurations
    master_dict = build_pruned_dict(masterList)

    # Get the maximum duration value of each station configuration.
    for f in master_dict.keys():
        max_durations_dict[f] = max([sum(g) for g in master_dict[f]])
        print(max_durations_dict[f])

    # Of all the longest configurations, optimize for minimum duration
    min_duration = min(max_durations_dict.values())

    # Get the key for the minimum duration
    pos = [k for k in max_durations_dict.keys() if max_durations_dict[k] == min_duration]

    return {"stations_config": master_dict[pos[0]], "longest_duration": min_duration}

def build_pruned_dict(master_list):
    build_dict = {}

    # Discard configuration if:
    # 1) if next element in station(i) tasks > current element AND sum(0, current element) < next element
    # 2) sum of station tasks durations < the duration of the next station's first task.
    for idx, m in enumerate(master_list):
        discard_me = False
        # for i in range(len(m)):
        #     for j in range(len(m[i])):
        #         if j + 1 < len(m[i]):
        #             if m[i][j] < m[i][j+1] and sum(m[i][0:j+1]) < m[i][j+1]:
        #                 discard_me = True
        #         if i + 1 < len(m):
        #             if sum(m[i]) < m[i + 1][0]:
        #                 discard_me = True
        if not discard_me:
            build_dict[idx] = m
    return build_dict


if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3

    answer = optimize_assembly_line(durations, stations)
    print(answer)
