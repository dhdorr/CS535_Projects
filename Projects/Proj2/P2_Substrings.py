# Derek Dorr
# CS535
# Project 2
# 11/1/2023

def string_graph_dfs(sol_dict, idx, visited=None):
    # Create a path list
    if not visited:
        visited = []

    # Initialize path
    path = [idx]
    
    # If dfs cannot go further, return the path + the current node
    if not sol_dict[idx]:
        return visited + path

    # Do not revisit nodes
    if idx in visited:
        return visited

    # Build path from current node recursively
    for c in range(len(sol_dict[idx])):
        child_path = string_graph_dfs(sol_dict, sol_dict[idx][c], visited)
        if len(child_path) + 1 > len(path):
            path = [idx] + child_path

    return path


def build_solution_graph(Strings):
    # Graph of connected strings
    temp_dict = {}
    # keep the spelling of each word
    spelling_dict = {}

    # Loop through input list
    for w in Strings:
        temp_dict[w] = []
        # Spell first word
        spelling_dict[w] = [i for i in w]

        # Find a string such that the w-string is a substring of the w2-string
        for w2 in Strings:
            if len(w2) == len(w) - 1:
                # Spell second word
                spelling_dict[w2] = [i for i in w2]
                is_valid = True

                # # Check if w2 contains all of w
                # for c in spelling_dict[w2]:
                #     if c not in spelling_dict[w]:
                #         is_valid = False
                #         # print("w2: ", w2, " w: ", w)
                #         break

                if is_valid:
                    # Check if there is only a 1-letter difference between the spelling of w and w2
                    for i, c in enumerate(spelling_dict[w]):
                        if c not in spelling_dict[w2]:
                            temp = w2[:i] + c + w2[i:]
                            if temp != w:
                                is_valid = False
                                # print("w2: ", w2, " w: ", w)
                                break

                # If w is a valid substring of w2, add w2 to the list
                if is_valid:
                    temp_dict[w].append(w2)

    return temp_dict


def longest_string_chain(Strings):
    path_dict = {}
    maxLen = 1
    answer = []

    # Build a graph where each string-node has a list of strings, from the input
    # The current string must be a substring of the next string.
    sol_dict = build_solution_graph(Strings)

    # Run a dfs on every node in the graph
    for key in sol_dict.keys():
        if not sol_dict[key]:
            continue

        # Build a list of paths from every node
        path_dict[key] = string_graph_dfs(sol_dict, key)

    # Optimize for longest path
    for k in path_dict.keys():
        if len(path_dict[k]) > maxLen:
            maxLen = len(path_dict[k])
            answer = path_dict[k]

    return {"longest_string_chain": answer, "length": maxLen}


if __name__ == '__main__':
    Strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

    answer = longest_string_chain(Strings)
    print(answer)
