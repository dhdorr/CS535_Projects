

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
                        print("discard: ", s)
                        break
    print(substr_list)

    for pair in substr_list:
        testList = [pair[0]]
        print(testList)
        visited = []
        visited.append(testList)
        i = 0
        j = 0
        while i < len(substr_list):
            # print(pair)
            # print(testList)
            # print("visited: ", visited)
            if substr_list[i][0] == testList[len(testList) - 1] and substr_list[i][1] not in testList:
                testList.append(substr_list[i][1])
                visited.append(testList)
                j += 1
                # print(testList)
                i = 0
            else:
                i += 1

    string_graph = {}
    for s in Strings:
        string_graph[s] = []

    for s in substr_list:
        string_graph[s[0]].append(s[1])
    print(string_graph)

    possible_substrings = []
    maxLen = 2
    for key in string_graph.keys():
        count = 0
        if not string_graph[key]:
            continue

        temp_list = dfs_v2(string_graph, key, 1)
        if len(temp_list) > maxLen:
            maxLen = len(temp_list)
            possible_substrings.append(temp_list)
        print(possible_substrings)
    return possible_substrings.pop()



def dfs_v2(string_graph, start, count, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    # print("count: ", count)
    # print("visited: ", visited)
    for next in string_graph[start]:
        dfs_v2(string_graph, next, count + 1, visited)
    return visited


def build_substring_dict(Strings):
    string_dict = {}
    for s in Strings:
        temp_list = [c for c in s]
        string_dict[s] = temp_list
    print(string_dict)

    return string_dict

def diff_check(A, B):

    A_dict = {}

    if len(A) + 1 == len(B):
        print(A, " ", B)
        for a in A:
            if a in A_dict:
                A_dict[a] += 1
            else:
                A_dict[a] = 1

        for b in B:
            if b in A_dict:
                A_dict[b] -= 1
        # print(A_dict)
        if sum(A_dict.values()) == 1:
            return True
    return False


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    ans = longest_substring(Strings)
    print(ans)
    print(len(ans))
