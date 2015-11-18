__author__ = 'navin.kolambkar'
'''
The minimum possible sum|x_i - x_j| using K pairs (2K numbers) from N numbers
'''
import sys
def ints(): return [int(s) for s in sys.stdin.readline().split()]

N, K = ints()
num = sorted(ints())

best = {} #best[(k,n)] = minimum sum using k pairs out of 0 to n
def b(k,n):
    if best.has_key((k,n)): return best[(k,n)]
    if k==0: return 0
    return float('inf')

for n in range(1,N):
    for k in range(1,K+1):
        best[(k,n)] = min([b(k,n-1),                      #Not using num[n]
                           b(k-1,n-2) + num[n]-num[n-1]]) #Using num[n]

print best[(K,N-1)]