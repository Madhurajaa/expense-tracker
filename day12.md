# Day 12 - Reports CLI

## What I learned

Today I extended the Expense Tracker with SQLite reports and a command-line interface.

### 1. SQL Reporting

I learned how to use SQL aggregate functions such as:

- `SUM()` - calculates total spending
- `AVG()` - calculates average spending
- `COUNT()` - counts rows
- `GROUP BY` - groups results by category or month
- `ORDER BY` - sorts report results
- `HAVING` - filters grouped results
- `strftime()` - extracts year and month from a date

I created eight reports:

1. Total spend
2. Spend per category
3. Monthly spend
4. Monthly spend per category
5. Top 5 expenses
6. Over-budget categories
7. Average spend per category
8. Expenses per month

### 2. Parameterized SQL

I learned that user-provided values should not be directly inserted into SQL queries.

For example:

```python
WHERE date >= ?
AND date < date(?, '+1 month')

The values are passed separately:

(month + "-01", month + "-01")

This makes the SQL safer and avoids SQL injection.

3. SQLite and Python

I learned how Python's sqlite3 module connects the application to the database.

The Database class is responsible for database operations, while the CLI handles user input.

This keeps database logic separate from the command-line interface.

4. argparse

I learned how to create a CLI using Python's argparse module.

The application now supports:

python3 cli.py add
python3 cli.py list
python3 cli.py list --category food
python3 cli.py report
python3 cli.py report --month 2026-08

I also learned how subcommands work using add_subparsers().

5. Error Handling

I tested invalid inputs:

Negative amount
Invalid category
Invalid date

The program displays an error instead of crashing.

Example:

Error: Amount must be a positive number.
6. Git

I created a separate branch for Day 12:

feature/day12-reports-cli

I learned to review changes using git diff, stage files using git add, and commit the completed work together.
