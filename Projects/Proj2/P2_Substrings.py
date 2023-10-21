def dfs_v4(sol_dict, idx, myPath=None):
    if not myPath:
        myPath = []

    res = [idx]
    if not sol_dict[idx]:
        return myPath + res

    if idx in myPath:
        return myPath

    child_path = dfs_v4(sol_dict, sol_dict[idx][0], myPath)
    res = [idx] + child_path

    return res


def build_solution_graph(Strings):
    temp_dict = {}
    for w in Strings:
        temp_dict[w] = []
        for w2 in Strings:
            if len(w2) == len(w) + 1:
                is_valid = True
                for a in w:
                    if not a in w2:
                        is_valid = False
                        break
                if is_valid:
                    temp_dict[w].append(w2)
    return temp_dict


def longest_string_chain(Strings):
    path_dict = {}
    maxLen = 1
    answer = []

    sol_dict = build_solution_graph(Strings)

    for key in sol_dict.keys():
        idx = key
        if not sol_dict[key]:
            continue

        path_dict[key] = dfs_v4(sol_dict, idx)

    for k in path_dict.keys():
        if len(path_dict[k]) > maxLen:
            maxLen = len(path_dict[k])
            answer = path_dict[k]

    return {"longest_string_chain": answer, "length": maxLen}


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    answer = longest_string_chain(Strings)
    print(answer)
