

def take2(Strings):
    path_dict = {}
    string_index_dict = {}
    maxLen = 1
    answer = []

    for i, s in enumerate(Strings):
        string_index_dict[s] = i
    for j, s in enumerate(Strings):
        test = dfs_v3(j, Strings, string_index_dict)
        print(test)
        path_dict[j] = test


    print(path_dict)
    for k in path_dict.keys():
        if len(path_dict[k]) > maxLen:
            maxLen = len(path_dict[k])
            answer = path_dict[k]
    return answer


def dfs_v3(s_idx, Strings, string_index_dict, chain_path_dict=None):
    if chain_path_dict is None:
        chain_path_dict = {}

    if s_idx in chain_path_dict:
        return chain_path_dict[s_idx]

    res = [Strings[s_idx]]

    for c_idx in range(len(Strings[s_idx])):
        # Remove a character from the String at index k
        child = Strings[s_idx][:c_idx] + Strings[s_idx][c_idx+1:]
        if child in string_index_dict:
            child_path = dfs_v3(string_index_dict[child], Strings, string_index_dict, chain_path_dict)
            # Update our result if the new path is longer
            if len(child_path) + 1 > len(res):
                res = [Strings[s_idx]] + child_path

    chain_path_dict[s_idx] = res

    return res


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    ans2 = take2(Strings)
    print("answer: ", ans2)
