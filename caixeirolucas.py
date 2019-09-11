#!/usr/bin/env python3

from itertools import combinations

cidades = ['a','b','c','d','e','f']

distancias = [
   [0,   4,   5,   6,   11,  13],
   [4,   0,   3,   6,   7,   11],
   [5,   3,   0,   3,   8,   8],
   [6,   6,   3,   0,   11,  9],
   [11,  7,   8,   11,  0,   4],
   [13,  11,  8,   9,   4,   0]]


print (len(distancias))
i=0
for i in range(len(distancias)):
    print(i)
    print(distancias)
    print(distancias[i])

"""
    a   b   c   d   e   f   
a   0   4   5   6   11  13
b   4   0   3   6   7   11
c   5   3   0   3   8   8
d   6   6   3   0   11  9
e   11  7   8   11  0   4
f   13  11  8   9   4   0 
"""

