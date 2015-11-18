from __future__ import print_function

s = raw_input()

def validate(s):
    count = 0
    n = len(s)

    for i in range(2, n-2):
        count += [0, 1][s[i] == s[i-2] or s[i] == s[i+2]]

    count += [0, 1][s[1] == s[3] or s[n-2] == s[n-4]]

    return count <= 1


g = [lambda: print(validate(s)), lambda: print(False)][not s.isdigit() or int(s) < 100000 or int(s) > 999999]
g()
