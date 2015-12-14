#!/usr/bin/python

import funniest
import sys


def main():
    if len(sys.argv) == 1:
        funniest.joke()
    else:
        output = ' '.join(sys.argv[1:])
        print output
