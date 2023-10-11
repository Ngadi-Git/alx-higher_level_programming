#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    sumed = 0
    roman_dic = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
            }
    for r in reversed(roman_string):
        ar_L = roman_dic[r]
        sumed += ar_L if sumed < ar_L * 5 else -ar_L
    return (sumed)
