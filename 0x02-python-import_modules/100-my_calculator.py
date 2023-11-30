#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    args_number = len(sys.argv) - 1

    if args_number != 3:
        print("Usage: /100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1:4]
    a, b = map(int, [a, b])
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = operators[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
