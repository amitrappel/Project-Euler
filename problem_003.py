__author__ = 'amitr'


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def largest1(n, i):
    p = primes[i]
    if  n == p:
        return n
    elif n % p == 0:
        return largest1(n / p, i)
    else:
        return largest1(n, i + 1)


def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


'''
# Option 1
primes = filter(is_prime, range(1, 10000))
print largest1(600851475143 , 0)
'''

# Option 2
n = 600851475143
primes = gen_primes()
divisor = primes.next()
largest_divisor = 1
while divisor <= n:
    if n % divisor == 0:
        largest_divisor = divisor
        n /= divisor
    divisor = primes.next()
print largest_divisor
