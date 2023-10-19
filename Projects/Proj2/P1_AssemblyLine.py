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


if __name__ == '__main__':
    durations = [15,15,30,30,45]
    stations = 3
    ans = assembly_line(durations, stations)
    print("answer = ", ans)