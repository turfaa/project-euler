#!/usr/bin/python3

berkas = open("13-largeSum.txt")

d = 0

for x in berkas:
    y = int(x)
    d += y

d = str(d)
d = d[:10]
print("{}".format(d))
