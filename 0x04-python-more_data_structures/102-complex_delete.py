#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    ky_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            ky_del.append(key)
    for key in ky_del:
        del a_dictionary[key]
    return a_dictionary
