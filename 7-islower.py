#!/usr/bin/python3

lower_case = []
upper_case = []
def islower(c):
    for i in range(65, 91):
        upper_case.append(chr(i))

    for j in range(97, 123):
        lower_case.append(chr(j))

    if c in upper_case:
        return False

    if c in lower_case:
        return True
