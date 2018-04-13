__author__ = 'amitr'

for n in range(30):
    for m in range(n, 30):
        for k in range(10):
            a = k * (m**2 - n**2)
            b = k * 2 * m * n
            c = k * (m**2 + n**2)
            if a + b + c == 1000:
                print a, b, c, a * b * c