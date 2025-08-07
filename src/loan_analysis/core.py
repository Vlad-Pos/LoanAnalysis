from math import ceil, log


def run_calculation(args):
    args_dict = vars(args)
    para = ["type", "principal", "payment", "periods", "interest"]
    P = args_dict.get(para[1], 0)  # principle
    A = args_dict.get(para[2], 0)  # annuity payment
    n = args_dict.get(para[3], 0)  # periods
    i = args_dict[para[4]] / (12 * 100)
    case_annuity(P, A, n, i) if args.type == "annuity" else case_diff(P, n, i)

def case_annuity(P, A, n, i):
    if P == 0: # "principle" is None
        formula = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
        P = int(A / formula)
        print(f"Your loan principal = {P}!")

    elif A == 0: # "payment" is None
        formula = ((1 + i) ** n * i) / ((1 + i) ** n - 1)
        A = ceil(P * formula)
        print(f"Your monthly payment = {A}!")

    elif n == 0: # "periods" is None
        x = A / (A - i * P)
        n = ceil(log(x, 1 + i))
        time_str = f"{n} months" if 0 < n < 12 else "1 year" if n == 12 else f"{n // 12} years" if n % 12 == 0 else f"{n // 12} years and {n % 12} months"
        print(f"It will take {time_str} to repay this loan!")

    overpayment = int(A * n - P)
    print(f"Overpayment = {overpayment}")

def case_diff(P, n, i):
    S = 0
    for m in range(1, n+1):
        Dm = ceil(P / n + i * (P - P * (m - 1) / n))
        S += Dm
        print(f"Month {m}: payment is {Dm}")
    overpayment = int(S - P)
    print(f"Overpayment = {overpayment}")