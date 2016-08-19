import argparse


# create an argument parser
parser = argparse.ArgumentParser(description="calculate the square of a number")
parser.add_argument("square", type=int,
                    help="Display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=3,
                    help="increase output verbosity")  # type=int, choices=[0, 1, 2],

# parser.add_argument("--verbose", help="increase output verbosity", action="store_true")

# start parsing arguments typed in command line, return the arguments added as a Namespace class?
args = parser.parse_args()
print(args.verbosity)
if args.verbosity >= 2:
    print("The square of {} equals {}".format(args.square, args.square**2))
elif args.verbosity >= 1:
    print("{}^2 = {}".format(args.square, args.square**2))
else:
    print(args.square**2)