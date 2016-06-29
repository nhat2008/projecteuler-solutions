# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def compute_pythagorean(n):
    numbers = [x for x in xrange(2, n)]
    result = 0

    for x in numbers:
        for y in numbers:
            z = n - (x + y)
            if x*x + y*y - z*z == 0:
                result = x * y * z
    return result


print compute_pythagorean(1000)