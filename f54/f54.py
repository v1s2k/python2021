import math


def f54(n):
    if n == 0:
        return 3
    else:
        return 1 / 92 * ((f54(n - 1)) ** 2) + math.cos(f54(n - 1)) 
print('%.2e' % f54(5))
print('%.2e' % f54(15))
