#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args_number = len(sys.argv) - 1
    sum = 0
    if args_number == 0:
        print("{}".format(sum))
    else:
        for i in range(args_number):
            sum = sum + int(sys.argv[i + 1])
        print("{}".format(sum))
