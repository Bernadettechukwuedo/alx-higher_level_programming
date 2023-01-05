#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 1:
        if len(argv) == 2:
            print('1 argument:')
        else:
            print('{} arguments:'.format(len(argv) - 1))
        for argc in range(1, len(argv)):
            print('{}: {}'.format(argc, argv[argc]))
    else:
        print('0 arguments.')
