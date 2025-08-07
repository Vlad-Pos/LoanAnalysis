# Loan Analysis Tool

A command-line utility designed to perform accurate loan calculations, supporting both annuity and differentiated payment types. The tool computes monthly payments, loan principal, duration, and overpayment with clear feedback and strong input validation.

---

## Features

- Calculate monthly payments, principal, or loan duration for annuity loans  
- Support differentiated payments with detailed monthly breakdown  
- Automatically identify and compute missing parameters where possible  
- Provide clear overpayment summaries based on inputs and loan type  
- User-friendly CLI leveraging Python’s `argparse` for flexible input handling  

---

## Usage

Run the tool from your project root using this command format:

```bash
python -m src.loan_analysis --type=<annuity|diff> --principal=<amount> --payment=<amount> --periods=<months> --interest=<annual_rate>
