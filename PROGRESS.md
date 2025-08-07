# Project Development Log – `loan_analysis`

This document captures the journey of developing the `loan_analysis` project. Each entry shares what was accomplished, the reasoning behind technical choices, and plans moving forward.

---

## June 24 – Getting Started

- Set up Python 3.13 environment using `pyenv`
- Created an isolated virtual environment with `uv` and `.venv`
- Initialized the Git repository and linked it to GitHub
- Configured project packaging with `pyproject.toml` and `setuptools`
- Established the initial package structure inside `src/loan_analysis/`

---

## June 25 – Building Core Loan Logic

- Developed key functions for annuity and differentiated loan calculations
- Added input validation to ensure correct and complete parameters
- Built a command-line interface using `argparse` for user interaction
- Prepared the foundation for unit testing using `unittest`

---

## August 6 – Improving Modularity and CLI

- Refined code by separating logic into well-defined functions for easier maintenance
- Enhanced CLI with better error handling and more flexible input support
- Supported calculations for annuity payments, loan principals, and loan duration

---

## August 7 – Adding Advanced Features and Validation

- Implemented differentiated payment calculations
- Strengthened input validation and improved error messages
- Enabled dynamic function selection based on loan type
- Conducted thorough code reviews to catch edge cases and ensure robustness

---

## Current State

- A fully functional CLI loan calculator handling both annuity and differentiated payments
- Clean, maintainable, and PEP 8-compliant code designed for future growth
- Original and well-tested algorithms covering all key loan parameters

---

## What’s Next

- Develop a web-based interface for easier access and usability
- Integrate with external APIs to retrieve real-time financial data
- Expand support for adjustable and variable-rate loans
- Create interactive visualizations to better illustrate loan repayment schedules

---

## Additional Notes

- All code is written from scratch with attention to quality and structure
- Continuous refactoring and documentation ensure ongoing improvements
- The project structure focuses on maintainability and scalability for future needs
