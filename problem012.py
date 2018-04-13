__author__ = 'amitr'

import itertools

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


def triangulars():
    for i in itertools.count(1):
        yield i * (i+1) / 2


def find_num_of_divisors(n):
    n0 = n
    primes = gen_primes()
    divisors_exps = []
    p = primes.next()
    while True:
        divisors_exps.append(1)
        while n % p == 0:
            divisors_exps[-1] += 1
            n = n / p
        p = primes.next()
        if p > n0:
            break
    return reduce(lambda x, y: x * y, divisors_exps)

def find_num_of_divisors_of_nth_triangular_number(n):
    if n % 2 == 0:
        return find_num_of_divisors(n / 2) * find_num_of_divisors(n + 1)
    else:
        return find_num_of_divisors(n) * find_num_of_divisors((n+1) / 2)

'''
tris = triangulars()

while True:
    num = tris.next()
    if find_num_of_divisors(num) > 100:
        print num
        break
'''

for i in itertools.count(1):
    if find_num_of_divisors_of_nth_triangular_number(i) > 500:
        print i * (i + 1) / 2
        break