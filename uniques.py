"""
QUESTION FROM ALGO DAILY

https://algodaily.com/challenge_slides/uniqueness-of-arrays

Given an array, return another array with just the ordered unique elements from the given array. 
In other words, you're removing any duplicates.

Note: Order needs to be preserved, so no sorting should be done. 
And the order should be maintained with the first occurrence of the element in the given array.

Constraints
Length of the array <= 100000
The values in the array between -1000000000 and 1000000000
Expected time complexity: O(n)
Expected space complexity: O(n)
"""


def uniques_array(arr):
    # my_set = set()
    # my_set.update(arr)

    # return list(my_set)
    my_dict = {}
    for num in arr:
        letter = str(num)
        if letter not in my_dict:
            my_dict[letter] = 0

        my_dict[letter] += 1

    res = [int(key) for key, value in my_dict.items()]
    # print(my_dict)

    return res


print(uniques_array([3, 5, 6, 9, 9, 9, 9, 4, 3, 12]))
print(uniques_array([13, 5, 3, 5, 8, 13, 14, 5, 9]))
print(uniques_array([8, 8, 15, 6, 19, 7, 12, 6,
      6, 3, 13, 9, 15, 14, 1, 13, 4, 11, 16]))
