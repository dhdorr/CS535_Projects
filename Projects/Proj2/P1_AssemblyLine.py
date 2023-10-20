

def take3(durations, stations):
    sol_list = []
    matrix = []
    masterList = []

    # Build a matrix of possible element counts.
    # In the example, durations.len = 5 & stations = 3
    # So the max number of tasks a station can have is 3 ((5 - (3 - 1)) = 3)
    for j in range(len(durations) - (stations - 1)):
        sol_list.append(j + 1)

    for i in range(1, stations + 1):
        res = [[i, a, b] for a in range(1, stations + 1) for b in sol_list]
        for r in res:
            if sum(r) == len(durations):
                matrix.append(r)

    for i, m in enumerate(matrix):
        itr = 0
        testList = []
        for j, n in enumerate(m):
            temp = durations[itr:itr + n]

            testList.append(temp)

            itr += n
        masterList.append(testList)

    my_list = prune_list(masterList)

    maxNo = 0
    totals_list = []
    for f in my_list:
        for g in f:
            helpMe = sum(g)
            if helpMe > maxNo:
                maxNo = helpMe
        totals_list.append(maxNo)

    min_total = totals_list[0]
    min_pos = 0
    for i, t in enumerate(totals_list):
        if t < min_total:
            min_total = t
            min_pos = i

    print("optimized assembly line: ", my_list[min_pos])
    print("optimized max wait: ", min_total)


# Given a list of all possible assembly line configurations
# Prune out all bad configurations (
def prune_list(master_list):
    build_list = []
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