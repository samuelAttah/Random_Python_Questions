"""
QUESTION FROM ALGO DAILY
Missing Number In Unsorted
Assume we're given an unsorted array of numbers such as this:

[ 2, 5, 1, 4, 9, 6, 3, 7 ]
We are told that when this array is sorted, there is a series of n consecutive numbers. 
You are given a lower bound and an upper bound for this sequence.
There is one consecutive number missing, and we need to find it.

As an example, look at the below example. We're told that the lower bound is 1 and the upper bound is 9. 
The number that's missing in the unsorted series bounded by these two number is 8.
"""


def missing_number_in_unsorted(arr):
    upper_bound = max(arr)
    lower_bound = min(arr)

    # print(upper_bound)
    # print(lower_bound)

    for num in range(lower_bound, upper_bound+1):
        if num not in arr:
            return num


print(missing_number_in_unsorted([2, 5, 1, 4, 9, 6, 3, 7]))
