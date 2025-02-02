import os
import sys
from datetime import datetime

def generate_execution_date(execution_date=None):
    if execution_date is None:
        execution_date = datetime.now().strftime("%Y-%m-%d")

    return execution_date

def main():
    if len(sys.argv) > 1:
        execution_date = generate_execution_date(sys.argv[1])
    else:
        execution_date = generate_execution_date()
    print(f"export EXECUTION_DATE='{execution_date}'")

if __name__ == "__main__":
    main()
