from collections import defaultdict
from math import sqrt

__author__ = 'navin.kolambkar'
import sys



def longestIncreasingSubSeq():
    list = []
    for line in sys.stdin:
        list.append(line)

    list = list[1:]

    n = len(list)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if(list[i] > list[j]):
                if(lis[j] + 1 > lis[i]):
                    lis[i] = lis[j] + 1

    return max(lis)

def main():
    #if len(list) > 0:
    #    sys.stdout.write(str(longestIncreasingSubSeq()))
    #print fib()
    #fact()
    numWays()

def fib():
    input = sys.stdin.readline()
    data = input.split()
    a = int(data[0])
    b = int(data[1])
    b = b*b
    n = int(data[2])

    for i in range(3, n+1):
        c = a + b
        a = temp
        temp = c
        b = c*c

    return c

def fact():
    input = 25
    result = [0]*200
    result[0] = 1
    k = 0

    for i in range(1, input+1):
        carry = 0
        for j in range(k+1):
            val = result[j] * i + carry
            result[j] = val % 10
            carry = val // 10

        while (carry > 0):
            k = k+1
            result[k] = carry % 10
            carry = carry // 10

    for i in range(k, -1, -1):
        print result[i],

def numWays():
    input = []
    for line in sys.stdin:
        input.append(line)

    n = int(input[0].split()[0])
    S = [int(i) for i in input[1].split()]
    m = len(S)

    table = [[0 for x in range(m)] for x in range(n+1)]

    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

def candies():
    input = []
    for line in sys.stdin:
        input.append(line)

    ratings = [int(i) for i in input[1:]]
    candies = [1 for i in range(len(ratings))]

    # only compare against left neighbor
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # only compare against right neighbor and pick max between left and right
    for i in range(len(ratings)-1, 0, -1):
        if ratings[i-1] > ratings[i]:
            candies[i-1] = max(candies[i] + 1, candies[i-1])

    print sum(candies)

def maxprofit(input):
    sp = [int(i) for i in input.split()]
    n = len(sp)
    ltr = [0 for i in range(n)]

    max_to_right = 0
    for i in range(n-1, -1, -1):
        if sp[i] < max_to_right:
            ltr[i] = max_to_right
        max_to_right = max(max_to_right, sp[i])

    cost = 0
    count = 0
    profit = 0
    for i in range(n):
        if ltr[i] > sp[i]:
            count = count + 1
            cost = cost + sp[i]
        else:
            profit = profit + (sp[i]*count - cost)
            cost = 0
            count = 0

    print profit

def maxprofitdriver():
    input = []
    for line in sys.stdin:
        input.append(line)

    for i in range(int(input[0])):
        maxprofit(input[i*2+2])

def stringReduction(a):
    counts = defaultdict(int)

    for c in a:
        counts[c] = counts[c] + 1 if c in counts else 1

    if counts['a'] == len(a) or counts['b'] == len(a) or counts['c'] == len(a):
        answer = len(a)
    elif (counts['a']%2 == 0 and counts['b']%2 == 0 and counts['c']%2 == 0) or (counts['a']%2 == 1 and counts['b']%2 == 1 and counts['c']%2 == 1):
        answer = 2
    else:
        answer = 1

    return answer

# https://www.quora.com/Are-there-any-good-resources-or-tutorials-for-dynamic-programming-besides-the-TopCoder-tutorial/answer/Michal-Danil%C3%A1k
# http://www.iarcs.org.in/inoi/online-study-material/topics/dp-tiling.php
# https://www.hackerrank.com/challenges/grid-walking
def grid_walking():
    N = 1
    M = 287
    x1 = 44
    D1 = 78

    num_ways = [[1 for j in range(D1+1)] for i in range(M+1)]

    for i in range(1, M+1):
        num_ways[i][1] = num_ways[i-1][2]
        num_ways[i][D1] = num_ways[i-1][D1-1]
        for j in range(2, D1):
            num_ways[i][j] = num_ways[i-1][j-1] + num_ways[i-1][j+1]

    print num_ways[M][x1] % 1000000007

if __name__ == '__main__':
    grid_walking()
    #print stringReduction('bcab')