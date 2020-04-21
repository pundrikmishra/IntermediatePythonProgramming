import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='What is first number?')
    parser.add_argument('--y', type=float, default=1.0, help='What is second number?')
    parser.add_argument('--operation', type=str, default='add', help='What operation? (add, sub, mul or div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()

# def calc(x,y, operation):
#     if operation == 'add':
#         return x+y
#     elif operation == 'sub':
#         return x-y
#     elif operation == 'mul':
#         return x*y
#     elif operation == 'div':
#         return x/y

# operation = calc(7,3,'div')
# print(operation)