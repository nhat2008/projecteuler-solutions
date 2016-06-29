#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# we use the formula: sum(1..n) = n(n+1)/2
def get_sum_square(n):
    square_sum = (n**2) * (n+1)**2 / 4
    sum_square = n * (n+1) * (2*n+1) / 6
    diff = square_sum - sum_square
    return diff

print get_sum_square(100)