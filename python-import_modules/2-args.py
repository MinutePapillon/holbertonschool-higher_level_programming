#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    length = len(sys.argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))

    while i < length + 1:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
