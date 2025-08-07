# Project Development Log – `loan_analysis`

This document tracks the structured, step-by-step development of the `loan_analysis` project. It provides a clear and concise record of features implemented, design choices made, and future plans.

---

## June 24th: Environment and Project Setup

- Configured Python 3.13 locally using `pyenv` and `uv`
- Created a dedicated `.venv` virtual environment for isolation
- Initialized Git repository and connected it to GitHub
- Structured the project using `pyproject.toml` with `setuptools`
- Created initial package scaffolding under `src/loan_analysis/`

---

## June 25th: Core Functionality Development

- Implemented core loan calculation logic: monthly payments and amortization schedule
- Added a CLI entry point using `__main__.py`
- Set up a testing framework to support future unit testing with `unittest` or `pytest`

---

## August 6th: Output and Visualization

- Added improved input capabilities using `argparse` module
- Implemented formulas for calculation of separate functions
- Optimized for annuity payments option

## August 7th: 
- Added new functionality: differentiated payments
- Optimized for differentiated payments option
- Introduced user input error handling
- Checked code on gaps and exeptions
  
- Implement visualization of principal vs. interest payments using `matplotlib`
- Add export functionality for amortization schedules to CSV format
- Implement detailed error handling and input validation for CLI

---

## Future Plans

- Add a web-based interface
- Integrate external financial APIs for real-time interest rate data
- Support for variable-rate and adjustable-rate loans
- Build interactive dashboards for user-friendly analysis

---

## Notes

- All code is original and manually written for this project
- Refactoring and documentation are maintained in parallel with feature development
- Progress is logged continuously and transparently for evaluation and review
