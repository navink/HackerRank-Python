import string

modulus = 1000000007

# function for computing binomial coefficients 
# input: n
# output: 2D array where output[n][k] = n choose k % modulus
def binomcoeffs(n):
    if n == 1:
        return [[1],[1,1]]
    else:
        recanswer = binomcoeffs(n-1)
        last = list(recanswer[n-1])
        last = [0] + last + [0]
        out = [0]*(n+1)
        for i in xrange(n+1):
            out[i] = (last[i] + last[i+1]) % modulus
        recanswer.append(out)
        return recanswer

# function for solving the 1-dimensional problem
# input: d=len of grid, x=start point, reps = num of steps
# output: array of length reps+1 where out[i] = number of paths of length i
def solve1dproblem(d,x,reps):
    grid = [0]*(d+2)
    grid[x] = 1
    out = [1] + [0]*reps
    for i in xrange(reps):
        tempgrid = [0]*(d+2)
        for j in xrange(1,d+1):
            tempgrid[j] = (grid[j-1] + grid[j+1]) % modulus
        grid = tempgrid
        out[i+1] = reduce(lambda x,y: (x+y)%modulus, grid)
    return out



[t] = map(int,string.split(raw_input()))

for i in xrange(t):
    n,m = map(int,string.split(raw_input()))
    x = map(int,string.split(raw_input()))
    d = map(int,string.split(raw_input()))

    binoms = binomcoeffs(m)

    #totals[i][j] will store number of ways to take j steps using only first i dimensions
    totals = [0]*n
    
    for i in xrange(n):
        totals[i] = [0]*(m+1)
    totals[0] = solve1dproblem(d[0],x[0],m)

    for i in xrange(1,n):
        onedanswer = solve1dproblem(d[i],x[i],m)
        for j in xrange(m+1):
            for k in xrange(j+1):
                totals[i][j] = (totals[i][j] + (totals[i-1][j-k])*(onedanswer[k])*(binoms[j][k])) % modulus

    print totals[n-1][m]

