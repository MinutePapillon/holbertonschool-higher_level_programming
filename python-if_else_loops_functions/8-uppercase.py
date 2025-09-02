#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = ord(i)
        if 97 <= number <= 122:
            number -= 32
        print(chr(number), end="")
    print()
