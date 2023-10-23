#!/usr/bin/python3
# 4-list_division.py

ef list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(0, list_length):
        try:
            quotnt = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            quotnt = 0
        except ZeroDivisionError:
            print("division by 0")
            quotnt = 0
        except IndexError:
            print("out of range")
            quotnt = 0
        finally:
            new_list.append(quotnt)
    return (new_list)
