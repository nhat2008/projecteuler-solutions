# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

history_data = {}


def chain(n):
    if n in history_data:
        return history_data[n]
    if n == 1:
        history_data[1] = [1]
        return history_data[1]
    else:
        if n % 2 == 0:
            history_data[n] = [n] + chain(n / 2)
            return history_data[n]
        else:
            history_data[n] = [n] + chain(3 * n + 1)
            return history_data[n]


def longest_collatz_sequence(limit):
    start = 2
    max_length = 1
    max_num = 1
    for i in xrange(limit, start, -1):
        chain_list = chain(i)
        if len(chain_list) > max_length:
            max_length = len(chain_list)
            max_num = i

    return max_num

print longest_collatz_sequence(1000000)
