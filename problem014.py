__author__ = 'amitr'


def collatz(n):
    if n == 1:
        return 1
    return 1 + collatz(n / 2) if n % 2 == 0 else 1 + collatz(3 * n + 1)


def remove_collatz(n):
    if n not in left:
        return
    else:
        left.remove(n)
        if n % 2 == 0:
            remove_collatz(n / 2)
        else:
            remove_collatz(3 * n + 1)


n = 1006
left = range(1, n)
for i in range(n, 1, -1):
    if len(left) > 1:
        remove_collatz(i)
    else:
        print left
        break

#print collatz(500)