__author__ = 'navin.kolambkar'

def primesLessThan(n):
    nums = [True] * (n+1)
    nums[0] = nums[1] = False
    total = 0

    for i in range(2, n+1):
        if nums[i] == True:
            total = total + 1
            k = 0

            for j in xrange(i*i, n+1, i):
                nums[j] = False
                k = k + 1

    return total

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def tiling(N):
    #N = 7
    T = [1 for i in range(N+1)]

    for i in range(4, N+1):
        T[i] = T[i-1] + T[i-4]

    print primesLessThan(T[N])

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    tiling(n)

