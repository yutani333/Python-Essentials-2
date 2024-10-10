#!/usr/bin/env python3

"""making debugging easier"""

from sys import argv

debug = 0
for item in argv:
    if item == '-dbA':
        debug = 1

def bprint(msg):
    if debug:
        print(msg)

if __name__ == "__main__":
    print("Hey! I'm supposed to be a module!")
