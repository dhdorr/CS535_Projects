

def longest_substring(Strings):
    string_dict = build_substring_dict(Strings)
    substr_list = []
    for s in Strings:
        for a in Strings:
            if len(a) == len(s) + 1:
                substr_list.append([a, s])
                for t in s:
                    if t not in string_dict[a]:
                        substr_list.pop()
                        # print("discard: ", s)
                        break
    # print(substr_list)

    string_graph = {}
    for s in Strings:
        string_graph[s] = []

    for s in substr_list:
        string_graph[s[0]].append(s[1])
    # print(string_graph)

    possible_substrings = []
    maxLen = 2
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
        dfs_v2(string_graph, next, count + 1, visited)
    return visited


def build_substring_dict(Strings):
    string_dict = {}
    for s in Strings:
        temp_list = [c for c in s]
        string_dict[s] = temp_list
    # print(string_dict)

    return string_dict


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    ans = longest_substring(Strings)
    print(ans)
    print(len(ans))
