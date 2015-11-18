__author__ = 'navin.kolambkar'

N, M, K = map(int, raw_input().split())
b = [list(raw_input()) for n in xrange(N)]
F = {}
def f(n,m,k):
    if k<0 or n<0 or n>=N or m<0 or m>=M: return K+1
    if b[n][m]=='*': return 0
    if (n,m,k) not in F:
        F[n,m,k] = min(f(n-1,m,k-1) + (b[n][m]!='U'),
                       f(n,m-1,k-1) + (b[n][m]!='L'),
                       f(n+1,m,k-1) + (b[n][m]!='D'),
                       f(n,m+1,k-1) + (b[n][m]!='R'))
    return F[n,m,k]
x = f(0,0,K)
print x if x <= K else -1