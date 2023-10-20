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

    while True:
        for i in range(stations):
            temp = durations[start:len(durations) - (stations - i - 1)]
            start = len(durations) - (stations - i - 1)

            sol_list.append(temp)
        solutions_dict[count] = sol_list
        count += 1
        break
    print(solutions_dict)



if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3
    # ans = assembly_line(durations, stations)
    # print("answer = ", ans)

    # take2(durations, stations)
    take3(durations, stations)