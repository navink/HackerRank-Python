from __future__ import division
import sys
import re
import itertools

N = int(raw_input())
data = raw_input().split()
K = int(raw_input())

#ind = [d+1 if data[d] == 'a' else None for d in range(len(data))]
ind = [i for i, x in enumerate(data) if x == 'a']

iter = itertools.combinations(range(1,N+1), K)
count = 0
total = 0
for i in iter:
    total += 1
    for j in i:
        if j in ind:
            count += 1
            break

print count/total