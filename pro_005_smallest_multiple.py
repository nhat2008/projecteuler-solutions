# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def get_smallest_multiple(min, max):
    numbers = range(min, max)
    x = 0
    while x < len(numbers):
        y = x + 1
        while y < len(numbers):
            if numbers[y] % numbers[x] == 0:
                numbers[y] = numbers[y] / numbers[x]
            y += 1
        x += 1
    result = reduce(lambda a, b: a * b, numbers)
    return result

print get_smallest_multiple(1,10)


