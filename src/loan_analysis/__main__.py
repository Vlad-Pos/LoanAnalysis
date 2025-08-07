from loan_analysis.cli import parse_and_validate
from loan_analysis.core import run_calculation

def main():
    args = parse_and_validate()
    run_calculation(args)

if __name__ == "__main__":
    main()

# Run code:
# python -m src.loan_analysis