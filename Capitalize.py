__author__ = 'navin.kolambkar'
import re
#s = raw_input()

def capitalize(s):
    if s.isalnum():
        return s[0].upper() + s[1:]
    else:
        return s

#s1 = re.split('(\W)', s)
#s1 = map(capitalize, s1)
#print ''.join(s1)

for i in range(1,int(raw_input())+1):
    print sum(map(lambda x:10**x, range(i)))**2
    #print sum([10**j for j in range(i)])**2