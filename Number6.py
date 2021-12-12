'''The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def sum_of_squares(a, b):
    squares = []
    for i in range(a, b):
        sqr = i ** 2
        squares.append(sqr)
    return(sum(squares))

def square_of_sums(a, b):
    sums = []
    for i in range(a, b):
        sums.append(i)
    squared = sum(sums)**2
    return(squared)


c = 1
d = 101
dif = square_of_sums(c, d) - sum_of_squares(c, d)

print("Sum of squares is", sum_of_squares(c, d), "Square of the sums", square_of_sums(c, d), "the difference is", dif)




