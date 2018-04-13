__author__ = 'amitr'


def fib(n):
    a, b = 1, 2
    for i in range(n-1):
        a, b = b, a+b
    return a

print fib(32)

sum = 0
for i in range(1, 33, 1):
    if (i % 3 == 2):
        sum += fib(i)

print sum