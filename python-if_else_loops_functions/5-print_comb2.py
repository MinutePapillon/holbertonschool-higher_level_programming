#!/usr/bin/python3

for i in range(1, 100):
    print("0{}".format(i) if i < 10 else "{}".format(i), end="" if i < 99 else "\n")
    if i < 99:
        print(", ", end="")
