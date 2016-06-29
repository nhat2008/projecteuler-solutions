# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_1():
    result = 0
    max_number = 10000
    # xrange: generator or lazy
    for x in xrange(1, max_number):
        if x % 3 == 0 or x % 5 == 0:
            result = result + x
    return result

print sum_1()
# 233168





