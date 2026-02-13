import sys

args_number = len(sys.argv) - 1
number = 0

if args_number == 1:
    try:
        number = int(sys.argv[1])
        if not isinstance(number, int):
            sys.exit(1)
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
elif args_number > 1:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

if number % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")