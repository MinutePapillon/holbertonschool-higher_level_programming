#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for letter in roman_string:
        for number in roman_numeral.keys():
            if letter == number:
                result += roman_numeral[number]
    return result