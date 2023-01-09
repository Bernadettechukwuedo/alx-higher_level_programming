#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a >= 2:
        num_a1 = tuple_a[0]
        num_a2 = tuple_a[1]
    elif len_a == 1:
        num_a1 = tuple_a[0]
        num_a2 = 0
    elif len_a == 0:
        num_a1 = 0
        num_a2 = 0

    if len_b >= 2:
        num_b1 = tuple_b[0]
        num_b2 = tuple_b[1]
    elif len_b == 1:
        num_b1 = tuple_b[0]
        num_b2 = 0
    elif len_b == 0:
        num_b1 = 0
        num_b2 = 0

    tuple_summed = (num_a1 + num_b1, num_a2 + num_b2)
    return tuple_summed
