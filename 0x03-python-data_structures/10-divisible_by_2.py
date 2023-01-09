#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) != 0:
        new_list = []
        for integer in my_list:
            if integer % 2 == 0:
                new_list += [True]
            else:
                new_list += [False]
        return new_list
