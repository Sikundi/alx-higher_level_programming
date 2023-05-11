#!/usr/bin/python3
for number in range(26):
    if number % 2 == 0:
        print('{:c}'.format(122 - number), end='')
    else:
        print('{:c}'.format(90 - number), end='')
