#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{:d}".format(num))
    else:
        print("{}".format(str(num).zfill(2)), end=", ")
