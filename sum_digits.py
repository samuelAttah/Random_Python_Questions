"""
QUESTION FROM ALGO DAILY
https://algodaily.com/challenge_slides/sum-digits-until-one

Sum Digits Until One

We're provided a positive integer num. 
Can you write a method to repeatedly add all of its digits until the result has only one digit?

Here's an example: if the input was 49, we'd go through the following steps:

SNIPPET
// start with 49
4 + 9 = 13

// since the previous addition was 13,
// move onto summing 13's digits
1 + 3 = 4
We would then return 4.

Constraints
Input will be in the range between 0 and 1000000000
Expected time complexity : O(log n)
Expected space complexity : O(1)
"""


def sum_digits(num):
    """Note: This is a simple example of a recursive problem"""

    stringified_num = str(num)

    # Base or Terminating Case
    if len(stringified_num) == 1:
        return num

    # Recursive Case
    total = 0
    for char in stringified_num:
        total += int(char)

    return (sum_digits(total))


print(sum_digits(49))
print(sum_digits(439230))
