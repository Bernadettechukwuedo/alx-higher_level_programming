#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumtotal = 0
    if len(argv) > 1:
        for argc in range(1, len(argv)):
            sumtotal += int(argv[argc])
    print(sumtotal)
