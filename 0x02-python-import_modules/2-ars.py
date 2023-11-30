#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args_number = len(sys.argv) - 1

    if args_number == 0:
        print("0 arguments.")
    elif args_number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_number))
    i = 1
    while i <= args_number:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
