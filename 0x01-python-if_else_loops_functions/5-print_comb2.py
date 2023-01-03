#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{:d}".format(num))
    elif num >= 0 and num <= 9:
        print("{}".format("".zfill(1) + str(num)), end=", ")
    else:
        print("{:d}".format(num), end=", ")
