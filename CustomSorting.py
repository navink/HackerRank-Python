__author__ = 'navin.kolambkar'
import sys

s = raw_input()
chars = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25,
         'A':26, 'B':27, 'C':28, 'D':29, 'E':30, 'F':31, 'G':32, 'H':33, 'I':34, 'J':35, 'K':36, 'L':37, 'M':38, 'N':39, 'O':40, 'P':41, 'Q':42, 'R':43, 'S':44, 'T':45, 'U':46, 'V':47, 'W':48, 'X':49, 'Y':50, 'Z':51,
         '1':52, '3':53, '5':54, '7':55, '9':56, '0':57, '2':58, '4':59, '6':60, '8':61}

#def char_range(start, stop):
#    for c in range(ord(start), ord(stop)):
#        yield chr(c)

def compare(s):
    return chars[s]

def print_char(c):
    sys.stdout.write(c)

map(print_char, sorted(s, key=compare))
#c = ['c', 'b', 'd', 'a', 4, 2, 1, 3]
#c = map(lambda item:([str,int].index(type(item)), item), c)
#print c


