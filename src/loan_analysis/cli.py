import argparse
import sys

def parse_and_validate():
    parser = argparse.ArgumentParser(description = "Loan Calculator CLI")
    parser.add_argument("--type", 
                        choices=["annuity", "diff"], 
                        help='Choose between "annuity" and "diff" payments.',
                        required=True)
    parser.add_argument("--principal", type=float, default=0, help="Introduce a positive rational number.")
    parser.add_argument("--payment", type=float, default=0, help="Introduce a positive rational number.")
    parser.add_argument("--periods", type=int, default=0, help="Introduce a positive integer.")
    parser.add_argument("--interest", type=float, required=True)

    args = parser.parse_args()

    validate(args)

    return args


def validate(args):
    if args.principal < 0 or args.payment < 0 or args.periods < 0:
        print("Incorrect parameters!")
        sys.exit(1)
    elif args.interest <= 0:
        print("Incorrect parameters!")
        sys.exit(1)
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters!")
        sys.exit(1)
    elif [args.principal, args.payment, args.periods].count(0) >= 2:
        print("Must enter 4 parameters!")
        sys.exit(1)