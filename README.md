# Loan Analysis Tool

This command-line utility allows users to perform detailed calculations for annuity and differentiated loans. It supports estimating monthly payments, total overpayment, loan duration, and more — with robust error handling and flexible input combinations.

---

## Features

- Calculates monthly payments, principal, or loan duration for annuity-type loans
- Supports differentiated payments with detailed monthly breakdown
- Automatically detects missing parameters and computes them where possible
- Informs users of overpayment based on selected loan type and inputs
- Full command-line interface using Python’s `argparse` module

---

## How to Use

To run the tool, use the following command structure:

```bash
python src/loan_analysis/calculator.py --type=<annuity|diff> --principal=<amount> --payment=<amount> --periods=<months> --interest=<annual_rate>
