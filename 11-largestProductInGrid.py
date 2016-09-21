#!/usr/bin/python3

def valid(x,y):
    return ((x>=0)&(x<20)&(y>=0)&(y<20));

f = open("11-largestProductInGrid.txt")

dx = [-1,-1,-1,0,0,1,1,1];
dy = [-1,0,-1,-1,1,-1,0,-1];

lst = []

for line in f:
    inp = line.split(' ')
    inp = [int(x) for x in inp]
    lst.append(inp)

maks = 0

for i in range(0,20):
    for j in range(0,20):
        for k in range(0,len(dx)):
            if (valid(i+dx[k]*3, j+dy[k]*3)):
                kali = 1
                for l in range(0,4):
                    kali = kali*lst[i+dx[k]*l][j+dy[k]*l]
                if (kali>maks):
                    maks = kali

print(maks)
