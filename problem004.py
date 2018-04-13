__author__ = 'amitr'


def is3by3(n):
    for i in range(101, 999, 1):
        if (n % i == 0) and (n / i > 100) and (n / i < 1000):
            return True
    return False


def main():
    num = 999
    while True:
        palindrome = 1000 * num + \
                     100 * (num % 10) + \
                     10 * ((num % 100) / 10) + \
                     1 * num / 100
        if is3by3(palindrome):
            break
        num -= 1
    print num

if __name__ == '__main__':
    main()