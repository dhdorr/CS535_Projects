
def longest_substring(Strings):
    substr_list = []
    string_graph = {}
    possible_substrings = []
    maxLen = 1

    for s in Strings:
        for a in Strings:
            if len(a) == len(s) + 1:
                is_valid = True
                for t in s:
                    if t not in a:
                        is_valid = False
                        break
                if is_valid:
                    substr_list.append([a, s])

    for s in Strings:
        string_graph[s] = []

    for s in substr_list:
        string_graph[s[0]].append(s[1])

    print(string_graph)

    for key in string_graph.keys():
        if not string_graph[key]:
            continue

        temp_list = dfs_v2(string_graph, key, 1)

        if len(temp_list) > maxLen:
            maxLen = len(temp_list)
            possible_substrings.append(temp_list)
        # print(possible_substrings)
    return possible_substrings.pop()


def dfs_v2(string_graph, start, count, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for next in string_graph[start]:
        if next not in visited:
            dfs_v2(string_graph, next, count + 1, visited)
    return visited


def take2(Strings):
    path_dict = {}
    string_index_dict = {}

    for i, s in enumerate(Strings):
        string_index_dict[s] = i
    for j, s in enumerate(Strings):
        test = dfs_v3(j, Strings, string_index_dict)
        print(test)
        path_dict[j] = test

    maxLen = 1
    answer = []
    print(path_dict)
    for k in path_dict.keys():
        if len(path_dict[k]) > maxLen:
            maxLen = len(path_dict[k])
            answer = path_dict[k]
    return answer


def dfs_v3(idx, Strings, string_index_dict, chain_path_dict=None):
    if chain_path_dict is None:
        chain_path_dict = {}
    if idx in chain_path_dict:
        return chain_path_dict[idx]

    # res = 1
    res = [Strings[idx]]
    for k, s in enumerate(Strings[idx]):
        child = Strings[idx][:k] + Strings[idx][k+1:]
        if child in string_index_dict:
            # res = max(res, 1 + dfs_v3(string_index_dict[child], Strings, string_index_dict, chain_length_dict))
            child_path = dfs_v3(string_index_dict[child], Strings, string_index_dict, chain_path_dict)
            # Update our result if the new path is longer
            if len(child_path) + 1 > len(res):
                res = [Strings[idx]] + child_path
    chain_path_dict[idx] = res
    # print(chain_path_dict)
    # print(res)
    return res


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    ans = longest_substring(Strings)
    print(ans)
    print(len(ans))

    ans2 = take2(Strings)
    print("answer: ", ans2)
