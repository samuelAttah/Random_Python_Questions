"""
QUESTION FROM ALGO DAILY

https://algodaily.com/challenges/max-of-min-pairs

Max of Min Pairs
We have an array of length 2 * n (even length) that consists of random integers.

[1, 3, 2, 6, 5, 4]

We are asked to create pairs out of these integers, like such:

[[1, 3], [2, 6], [5, 4]]

How can we divide up the pairs such that the sum of smaller integers in each pair is maximized?

Here's an example input: [3, 4, 2, 5]. The return value is 6 because the maximum sum of pairs is 6 = min(2, 3) + min(4, 5).

Note that negative numbers may also be included.

Constraints
Length of the array <= 100000
The values will always contain integer values between -1000 and 1000
The final answer will always fit in the integer value
Expected time complexity : O(nlogn)
Expected space complexity : O(1)
"""


def max_of_min_pairs(arr):
    if len(arr) % 2 != 0:
        return f"Perfect Pairs can't be formed from uneven arrays"

    sorted_arr = sorted(arr)

    res = sum([min(sorted_arr[index], sorted_arr[index+1])
               for index in range(0, len(sorted_arr), 2)])

    return res


print(max_of_min_pairs([3, 4, 2, 5]))
print(max_of_min_pairs([1, 9, 8, 4, 0, 5]))
print(max_of_min_pairs([1, 3, 2, 6, 5, 4]))
