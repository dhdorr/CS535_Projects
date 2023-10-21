def dfs_v4(test_dict, idx, myPath=None):
    if not myPath:
        myPath = []

    res = [idx]
    if not test_dict[idx]:
        return myPath + res

    if idx in myPath:
        return myPath

    child_path = dfs_v4(test_dict, test_dict[idx][0], myPath)
    res = [idx] + child_path

    return res


def longest_string_chain(Strings):
    path_dict = {}
    string_index_dict = {}
    maxLen = 1
    answer = []

    test_dict = {}
    for w in Strings:
        test_dict[w] = []
        for w2 in Strings:
            if len(w2) == len(w) + 1:
                is_valid = True
                for a in w:
                    if not a in w2:
                        is_valid = False
                        break
                if is_valid:
                    test_dict[w].append(w2)
    # print(test_dict)

    path_list = {}
    for key in test_dict.keys():
        idx = key
        if not test_dict[key]:
            continue

        path_dict[key] = dfs_v4(test_dict, idx)
        # while True:
        #     if not test_dict[idx]:
        #         break
        #     idx = test_dict[idx][0]
        #     myPath.append(idx)


    # for i, s in enumerate(Strings):
    #     string_index_dict[s] = i
    # for j, s in enumerate(Strings):
    #     test = substring_dfs(j, Strings, string_index_dict)
    #     path_dict[j] = test

    for k in path_dict.keys():
        if len(path_dict[k]) > maxLen:
            maxLen = len(path_dict[k])
            answer = path_dict[k]
    return {"longest_string_chain": answer, "length": len(answer)}


# def substring_dfs(s_idx, Strings, string_index_dict, chain_path_dict=None):
#     if chain_path_dict is None:
#         chain_path_dict = {}
#
#     if s_idx in chain_path_dict:
#         return chain_path_dict[s_idx]
#
#     res = [Strings[s_idx]]
#
#     for c_idx in range(len(Strings[s_idx])):
#         # Remove a character from the String at index k
#         child = Strings[s_idx][:c_idx] + Strings[s_idx][c_idx+1:]
#         if child in string_index_dict:
#             child_path = substring_dfs(string_index_dict[child], Strings, string_index_dict, chain_path_dict)
#             # Update our result if the new path is longer
#             if len(child_path) + 1 > len(res):
#                 res = [Strings[s_idx]] + child_path
#
#     chain_path_dict[s_idx] = res
#
#     return res


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    ans2 = longest_string_chain(Strings)
    print(ans2)
