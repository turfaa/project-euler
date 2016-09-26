#!/usr/bin/python3

def sumDiv(num):
    tmp = num
    jum = 1
    now = 2
    while(num>1):
        pembagi = 0
        while (num%now==0):
            pembagi += 1
            num /= now

        jum *= sum([now**x for x in range(0,pembagi+1)])

        now+=1
    return jum-tmp


jum = 0
for i in range(2,10001):
    fori = sumDiv(i)
    if (i==sumDiv(fori)):
        if ((i>fori) & (i<=10000)):
            jum+=i+fori

print(jum)
