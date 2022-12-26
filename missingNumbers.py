"""
QUESTION FROM ALGO DAILY 

Find Missing Number in Array
We're given an array of continuous numbers that should increment sequentially by 1, 
which just means that we expect a sequence like:

[1, 2, 3, 4, 5, 6, 7]

However, we notice that there are some missing numbers in the sequence.

[1, 2, 4, 5, 7]

Can you write a method missingNumbers that takes an array of continuous numbers and returns the missing integers?

missingNumbers([1, 2, 4, 5, 7]);

//output [3, 6]
Constraints
Length of the array <= 100000
The array will always contain non negative integers (including 0)
Expected time complexity : O(n)
Expected space complexity : O(1)

"""


def missing_numbers(arr):
    res = [arr[index] +
           1 for index in range(len(arr)-1) if arr[index]+1 != arr[index+1]]

    return res


print(missing_numbers([1, 2, 4, 5, 7]))
