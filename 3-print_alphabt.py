#!/usr/bin/python3

"""Print letters except q and e"""

for letter in range(97, 123):
    if chr(letter) == 'e' or chr(letter) == 'q':
        continue
    print(chr(letter), end='')
