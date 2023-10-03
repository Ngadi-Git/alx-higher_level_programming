#!/usr/bin/python3
for index in range(ord('a'), ord('z') + 1):
    if chr(index) != 'e' and chr(index) != 'q':
        print('{:c}'.format(index), end='')
