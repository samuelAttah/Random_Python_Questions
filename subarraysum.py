"""
QUESTION FROM ALGO DAILY 
https://algodaily.com/challenge_slides/contiguous-subarray-sum

Contiguous Subarray Sum

Given an array of numbers, return true if there is a subarray that sums up to a certain number n.

A subarray is a contiguous subset of the array. For example the subarray of [1,2,3,4,5] is [1,2,3] or [3,4,5] or [2,3,4] etc.

JAVASCRIPT
const arr = [1, 2, 3], sum = 5
subarraySum(arr, sum)
// true
// [2, 3] sum up to 5

const arr = [11, 21, 4], sum = 9
subarraySum(arr, sum)
// false
// no subarrays sums up to 9
In the above examples, [2, 3] sum up to 5 so we return true. On the other hand, no subarray in [11, 21, 4] can sum up to 9.

Can you create a function subarraySum that accomplishes this?

Constraints
Length of the array <= 100000
The values in the array will be between 0 and 1000000000
The target sum n will be between 0 and 1000000000
The array can be empty
Expected time complexity : O(n)
Expected space complexity : O(n)
"""


def subarraySum(arr, value):
    flag = False
    sub_array_list = [arr[i:j]
                      for i in range(len(arr)) for j in range(i+1, len(arr)+1)]

    for element in sub_array_list:
        if sum(element) == value:
            flag = True
            break

    return flag


print(subarraySum([1, 2, 3], 3))
