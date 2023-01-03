#!/usr/bin/python3
for letters in range(97, 123):
    if letters != 113 and letters != 101:
        print("{:c}".format(letters), end="")
