#!/usr/bin/python3

for i in range(99):
    if i % 10 < i /10:
        continue
    if i == 89:
        print("{:02}".format(i))
    else:
        print("{:02}".format(i), end=', ')
