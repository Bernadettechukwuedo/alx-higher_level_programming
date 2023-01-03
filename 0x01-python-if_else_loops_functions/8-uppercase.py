#!/usr/bin/python3
def uppercase(str):
    for alph in str:
        z = ord(alph)
        if z >= 97 and z <= 122:
            z -= 32
        print("{:c}".format(z), end="")
    print()
