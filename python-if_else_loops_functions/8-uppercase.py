#!/usr/bin/python3
def uppercase(str):
    result = ""
    i = 0
    while i < len(str):
        char = str[i]
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
        i += 1
    print("{}".format(result))
