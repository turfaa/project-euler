#!/usr/bin/python3

def dig(x):
    x = str(x)
    return sum([int(y) for y in x])

def fac(x):
    if (x==0):
        return 1
    else:
        return x*fac(x-1)

print(dig(fac(100)))
