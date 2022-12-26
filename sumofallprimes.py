"""
QUESTION FROM ALGO DAILY

Sum All Primes
You're given a number n. Can you write a method sumOfAllPrimes that finds all prime numbers smaller than or equal to n,
 and returns a sum of them?
For example, we're given the number 15. All prime numbers smaller than 15 are:
2, 3, 5, 7, 11, 13
They sum up to 41, so sumOfAllPrimes(15) would return 41.

 """


def sumofAllPrimes(A):
    final_array = []

    while A > 1:

        res = [val for val in range(1, A+1) if A % val == 0]

        if len(res) == 2:
            final_array.append(A)

        A -= 1

    print(f"the final array is {list(reversed(final_array))}")
    return sum(final_array)


print(sumofAllPrimes(4))
