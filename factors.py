#!/usr/bin/env python3

import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return (i, n // i)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            n = int(line.strip())
            factors = factorize(n)
            if factors:
                p, q = factors
                print("{}={}*{}".format(n, p, q))

