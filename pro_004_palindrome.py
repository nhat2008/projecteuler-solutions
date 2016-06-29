# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_largest_palindrome(n):
    results = []
    # xrange for generators or lazy => i like this so much
    for x in xrange(n, 100, -1):
        for y in xrange(x, 100, -1):
            multi = x * y
            # check palindrome or not
            multi_str = str(multi)
            if multi_str == multi_str[::-1]:
                results.append(multi)
    return max(results)

print get_largest_palindrome(999)
