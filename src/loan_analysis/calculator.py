from math import ceil, log
import argparse

para = ["type", "principal", "payment", "periods", "interest"]

def args_parse():
    while True:
        try:
            parser.add_argument("--type", 
                                choices=["annuity", "diff"], 
                                help='Choose between "annuity" and "diff" payments.',
                                required=True)
            parser.add_argument("--principal", type=float, default=0, help="Introduce a positive rational number.")
            parser.add_argument("--payment", type=float, default=0, help="Introduce a positive rational number.")
            parser.add_argument("--periods", type=int, default=0, help="Introduce a positive integer.")
            parser.add_argument("--interest", type=float, required=True)
            break
        except ValueError or TypeError:
            print("Incorrect parameters!")

# use args.interest instead of args_dict["interest"]

def lock_type(type):
    if args_dict["principal"] < 0 or args_dict["payment"] < 0 or args_dict["periods"] < 0 or args_dict["interest"] < 0:
        print("Incorrect parameters!")
    elif type == "diff" and args_dict["payment"]:
        print("Incorrect parameters!")
    elif args_values.count(0) >= 2:
        print("Must enter 4 parameters!")
    else:
        return True


# def ArgParse():
#     while True:
#         try:
#             for par in parameters:
#                 parser.add_argument(par)
#             break
#         except ValueError:
#             print("Incorrect parameters!")

def case_general():
    type = args_dict[para[0]]
    P = args_dict.get(para[1], 0)
    A = args_dict.get(para[2], 0)
    n = args_dict.get(para[3], 0)
    i = args_dict[para[4]] / (12 * 100)
    case_annuity(P, A, n, i) if type == "annuity" else case_diff(P, n, i)
    print(f"Overpayment = {overpayment}")

def case_annuity(P, A, n, i):
    index = args_check()
    if index == 1: # "principle" is None
        formula = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
        P = int(A / formula)
        print(f"Your loan principal = {P}!")
    elif index == 2: # "payment" is None
        formula = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
        A = ceil(P * formula)
        print(f"Your monthly payment = {A}!")
    elif index == 3: # "periods" is None
        x = A / (A - i * P)
        n = ceil(log(x, 1 + i))
        time_str = f"{n} months" if 0 < n < 12 else "1 year" if n == 12 else f"{n // 12} years" if n % 12 == 0 else f"{n // 12} years and {n % 12} months"
        print(f"It will take {time_str} to repay this loan!")
    global overpayment
    overpayment = int(A * n - P)

def case_diff(P, n, i):
    S = 0
    for m in range(1, n+1):
        Dm = ceil(P / n + i * (P - P * (m - 1) / n))
        S += Dm
        print(f"Month {m}: payment is {Dm}")
    global overpayment
    overpayment = int(S - P)


def args_check():
    for i in range(1, 5):
        if args_values[i] == 0:
            return i

parser = argparse.ArgumentParser(description = "")
args_parse()
args = parser.parse_args()
args_dict = vars(args)
args_values = list(args_dict.values())
bool = False
bool = lock_type(args_dict["type"])
if bool is True:
    case_general()

# EX 8: python src/loan_analysis/calculator.py --type=diff --principal=1000000 --periods=10 --interest=-10

# EX 2: python src/loan_analysis/calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
# EX 4: python src/loan_analysis/calculator.py --type=diff --principal=500000 --periods=8 --interest=7.8
# EX 5: python src/loan_analysis/calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# EX 6: python src/loan_analysis/calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8


# print("Enter the loan principal:")
# loan = int(input())
# print(">", loan)

# print("""What do you want to calculate?
# type "m" for number of monthly payments,
# type "p" for the monthly payment:""")

# choice = input()
# print(">", choice)


# if choice == "m":
#     print("Enter the monthly payment:")
#     monthly = int(input())
#     print(">", monthly)
#     print(f"\nIt will take {ceil(loan / monthly)} months to repay the loan")

# else:
#     print("Enter the number of months:")
#     months = int(input())
#     print(">", months)
#     payment = ceil(loan / months)
#     last_payment = loan - (months - 1) * payment
#     if payment == last_payment:
#         print(f"Your monthly payment = {payment}")
#     else:
#         print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
