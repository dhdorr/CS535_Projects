

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



if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    ans = longest_substring(Strings)
    print(ans)
    print(len(ans))
