import itertools

def take3(durations, stations):
    print("hello3")
    solutions_dict = {}
    sol_list = []
    start = 0
    count = 0
    end = 0
    dict2 = {}

    start = 0
    matrix = []
    # Build a matrix of possible element counts.
    # In the example, durations.len = 5 & stations = 3
    # So the max number of tasks a station can have is 3 ((5 - (3 - 1)) = 3)
    for j in range(len(durations) - (stations - 1)):
        sol_list.append(j + 1)
    matrix = []
    for i in range(1, stations + 1):
        res = [[i, a, b] for a in range(1, stations + 1) for b in sol_list]
        for r in res:
            if sum(r) == len(durations):
                matrix.append(r)
    print("matrix: ", matrix)

    # for s in range(1, len(sol_list) + 1):
    #     matrix.extend(itertools.product(sol_list, repeat=s))
    # while True:
    #     count = 0
    #     for i, m in enumerate(matrix):
    #         count = i
    #         if sum(m) != len(durations):
    #             matrix.remove(m)
    #             break
    #         if len(m) < stations:
    #             matrix.remove(m)
    #             break
    #     if count >= len(matrix):
    #         break
    # print(matrix)

    # for a in sol_list:
    #     for b in sol_list:
    #         for c in sol_list:
    #             if a + b + c == len(durations):
    #                 matrix.append([a,b,c])
    # print(matrix)
    masterList = []
    testDict = {}
    for i, m in enumerate(matrix):
        itr = 0
        testList = []
        for j, n in enumerate(m):
            temp = durations[itr:itr + n]

            testList.append(temp)

            itr += n
        testDict[i] = testList
        masterList.append(testList)
        print("master list: ", masterList)

    my_list = prune_list(masterList)
    # print(testDict)
    testMatrix = []
    for key in testDict:
        should_discard = False
        for k, val in enumerate(testDict[key]):
            # print(val)
            sum1 = 0
            for i in range(len(val)):
                sum1 += val[i]
                if i < len(val)-1:
                    if val[i] < val[i + 1] and sum1 < val[i + 1]:
                        # print("discard")
                        should_discard = True
        if not should_discard:
            testMatrix.append(testDict[key])

    final_temp_list = []
    for i, v in enumerate(testMatrix):
        delete_me = False
        # print(v)
        for j, w in enumerate(v):
            my_total = sum(w)
            if j < len(v) - 1:
                # print(my_total, "test: ", v[j + 1][0])
                if my_total < v[j + 1][0]:
                    # print(v[j + 1][0])
                    # print("delete me")
                    delete_me = True

            # print(w)
        if not delete_me:
            final_temp_list.append(v)

    print(final_temp_list)
    maxNo = 0
    for f in final_temp_list:
        for g in f:
            helpMe = sum(g)
            if helpMe > maxNo:
                maxNo = helpMe
    print(maxNo)

    # print(testMatrix)


def prune_list(master_list):
    build_list = []
    for m in master_list:
        print(m)
        discard_me = False
        for i in range(len(m)):
            print(m[i])
            for j in range(len(m[i])):
                if j + 1 < len(m[i]):
                    if m[i][j] < m[i][j+1]:
                        print("discard me")
                        discard_me = True
                if i + 1 < len(m):
                    if sum(m[i]) < m[i + 1][0]:
                        print("discard me2")
                        discard_me = True
        if not discard_me:
            build_list.append(m)
    print("build list: ", build_list)
    return build_list


if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3

    take3(durations, stations)