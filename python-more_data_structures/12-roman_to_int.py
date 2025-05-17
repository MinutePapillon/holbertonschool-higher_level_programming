#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif not isinstance(roman_string, str):
        return 0

    result = 0
    num = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for letter in roman_string:
        if roman[letter] > num:
            result -= num
            num = roman[letter] - num
        else:
            num = roman[letter]
        result += num

    return result