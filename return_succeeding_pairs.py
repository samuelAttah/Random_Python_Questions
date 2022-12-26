"""
Given an Array A of even length, return the pairs of succeeding values as smaller arrays.

Example: Given an Array [1,9,8,4,0,5] th output should be:

// Output [[1,9], [8,4], [0,5]]
"""


def return_pairs(arr):
    if len(arr) % 2 != 0:
        return f"Perfect Pairs can't be formed from uneven arrays"
    res = [[arr[index], arr[index+1]] for index in range(0, len(arr), 2)]

    return res


print(return_pairs([1, 2, 4, 5, 6, 7]))
print(return_pairs([1, 9, 8, 4, 0, 5]))
