#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    compute = len(sys.argv) - 1
    if compute == 0:
        print("0 arguments.")
    elif compute == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(compute))
    for i in range(compute):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
