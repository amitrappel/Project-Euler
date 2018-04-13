__author__ = 'amitr'

sum_of_squares = reduce(lambda x, y: x + y, [n ** 2 for n in range(101)])
square_of_sum = (reduce(lambda x, y: x + y, range(101))) ** 2

print sum_of_squares - square_of_sum
