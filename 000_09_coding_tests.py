from itertools import combinations
from collections import Counter


x1 = "HARRY"
x2 = "SALLY"




def commonChild(s1, s2):
    list_of_s1_substrings = [''.join(l) for i in range(len(s1)) for l in combinations(s1, i+1)]
    list_of_s2_substrings = [''.join(l) for i in range(len(s2)) for l in combinations(s2, i+1)]
    max_length_of_common_child = 0

    for item in list_of_s1_substrings:
        if item in list_of_s2_substrings:
            max_length_of_common_child = max(max_length_of_common_child, len(item))
    return max_length_of_common_child


print(commonChild(x1, x2))