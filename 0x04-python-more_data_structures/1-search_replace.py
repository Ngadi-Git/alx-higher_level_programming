#!/usr/bin/python3

def search_replace(my_list, search, replace):
    nList = my_list[:]
    for index in range(len(nList)):
        if nList[index] == search:
            nList[index] = replace
    return (nList)
