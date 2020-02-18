#!/usr/bin/env python3
import sys

def minutestohours(m):
    h, m = divmod(int(m), 60)
    return "{} H, {} M".format(h, m)

def main(m):
    if m.isdigit():
        print(minutestohours(m))
    else:
        print("You have a wrong minutes.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
