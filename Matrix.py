from __future__ import print_function
import sys
import re

N, M = map(int, raw_input().split())
data = []
for d in range(N):
    data.append(raw_input())

s = []

for j in range(M):
    for i in range(N):
        s += data[i][j]

s = ''.join(s)

#last = [m.end() for m in re.finditer(r'\w+',s)][-1]
last = [m.end() for m in re.finditer(r'\w+',s)]

def print_matrix(last):
    last = last[-1]
    s1 = s[:last]
    s2 = s[last:]

    s3 = re.split("([!,@,#,$,%,&, '', ' ']+)", s1)
    s4 = filter(lambda (i,x) : i%2==0, enumerate(s3))
    #s4 = filter(lambda i : i%2==0, range(len(s3)))
    s5 = map(lambda (x,y) : y, s4)

    sys.stdout.write(' '.join(s5) + s2)

g = [lambda: print_matrix(last), lambda: print(s)][len(last) == 0]
g()


# s1 = s[:last]
# s2 = s[last:]
#
# s3 = re.split("([!,@,#,$,%,&, '', ' ']+)", s1)
# s4 = filter(lambda (i,x) : i%2==0, enumerate(s3))
# #s4 = filter(lambda i : i%2==0, range(len(s3)))
# s5 = map(lambda (x,y) : y, s4)
#
# sys.stdout.write(' '.join(s5) + s2)