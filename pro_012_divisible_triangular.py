# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
#
#
import math


def find_triangle_number(limit):
    n = 10
    while True:
        # sum 1..n = n * (n+1)/2
        n_triangle = n * (n + 1) / 2
        count = 0
        # Finding number of divisors
        for i in range(1, int(math.floor(math.sqrt(n_triangle)))):
            if n_triangle % i == 0:
                count += 1
        if count >= limit / 2:
            result = n_triangle
            break
        n += 1

    return result


print find_triangle_number(500)