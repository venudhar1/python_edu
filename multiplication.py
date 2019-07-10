#!/usr/bin/python


table_size = int(input("Enter the multiplication table size: "))
x = table_size

def multiplier(n):
    i = 1
    while i <= x:
        print(n*i),
        i += 1
    print

#MAIN


i = 1
while i <= x:
    multiplier(i)
    i += 1
