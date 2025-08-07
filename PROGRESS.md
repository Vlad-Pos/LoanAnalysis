# Project Development Log – `loan_analysis`

This file documents the progress and rationale behind the development of the `loan_analysis` project. Each entry reflects a real and transparent account of functionality built, technical decisions made, and upcoming goals.

---

## June 24 – Initial Setup

- Installed and configured Python 3.13 using `pyenv`
- Created an isolated virtual environment using `uv` and `.venv`
- Initialized the project repository and connected it to GitHub
- Set up `pyproject.toml` using `setuptools` for modern Python packaging
- Defined the base package structure under `src/loan_analysis/`

---

## June 25 – Core Loan Logic

- Implemented functions for annuity and differentiated loan calculations
- Added input validation to handle incorrect or insufficient parameters
- Created a command-line interface with argument parsing via `argparse`
- Set up a basic testing structure with `unittest` in mind for later test writing

---

## August 6 – CLI and Modularity

- Restructured the logic into clearly separated functions for maintainability
- Improved CLI support with error handling and flexibility
- Added support for calculating annuity payments, loan principals, and duration

---

## August 7 – Differentiated Payment Support

- Implemented differentiated payment calculations
- Enhanced robustness with input validation and usage errors
- Refined function call routing based on loan type
- Reviewed code for edge cases and logical completeness

---

## Next Steps

- Add web-based interaction with a lightweight frontend
- Integrate real-time financial data through external APIs
- Expand to support adjustable-rate and variable-rate loans
- Visualize loan payoff schedules through interactive charts

---

## Notes

- All code is original and developed from scratch
- Refactoring and documentation are updated regularly alongside features
- Project structure and code clarity are prioritized to ease maintenance and extendability
