import math


def assembly_line(durations, stations):
    maxNum = 0
    cutElement = 0
    for i in range(len(durations)):
        if durations[i] > maxNum:
            maxNum = durations[i]
            cutElement = i
    goal_duration = durations[cutElement]
    cut_durations = durations[:cutElement]
    stations -= 1

    total = 0
    for j in range(len(cut_durations)-1, -1, -1):
        if total >= goal_duration:
            return total
        total += cut_durations[j]


def take2(durations, stations):
    print("hellow")
    station_list = [0] * stations
    start = 0
    print(station_list)
    for i in range(stations-1):
        for j in range(start, len(durations)):
            print(durations[j]," ? ", durations[j+1])
            if durations[j] >= durations[j+1]:
                station_list[i] += durations[j]
                print("if: ", station_list)

            else:
                station_list[i-1] += durations[j]
                station_list[i] += durations[j+1]
                print("else: ", station_list)

            start += 1
            break
    start += 1
    if durations[start] < durations[start + 1]:
        station_list[stations - 2] += durations[start]
        station_list[stations - 1] += durations[start + 1]
    # station_list[stations-1] = durations[len(durations)-1]
    print(station_list)


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
    for j in range(len(durations) - (stations - 1)):
        sol_list.append(j + 1)

    for a in sol_list:
        for b in sol_list:
            for c in sol_list:
                if a + b + c == len(durations):
                    matrix.append([a,b,c])
    # print(matrix)
    testDict = {}
    for i, m in enumerate(matrix):
        itr = 0
        testList = []
        for j, n in enumerate(m):
            temp = durations[itr:itr + n]

            testList.append(temp)

            itr += n
        testDict[i] = testList
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

    # print(testMatrix)




if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3
    # ans = assembly_line(durations, stations)
    # print("answer = ", ans)

    # take2(durations, stations)
    take3(durations, stations)