#!/usr/bin/python3

number = 2**1000
string = str(number)

jumlah = 0

for x in string:
    jumlah += ord(x)-ord('0')

print(jumlah)
