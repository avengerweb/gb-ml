# Переворачиваем число


# O(n*n/2) ~ O(n^2)
# 100 loops, best of 3: 135 msec per loop - 2000
# 100 loops, best of 3: 30.8 msec per loop - 1000
# 100 loops, best of 3: 7.47 msec per loop - 500
def calc(n):
    lst = []
    k = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst


# O(n log (log n))
# 100 loops, best of 3: 418 usec per loop - 2000
# 100 loops, best of 3: 202 usec per loop - 1000
# 100 loops, best of 3: 99.6 usec per loop - 500
def calc2(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
