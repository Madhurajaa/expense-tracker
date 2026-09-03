# Expense Tracker

A command-line expense tracker built with Python and SQLite.

The project allows users to add and list expenses, generate spending reports, manage categories and budgets, and store expense data persistently in a SQLite database.

## Features

- Add expenses with amount, category, date, and note
- List all recorded expenses
- Generate spending reports
- View total spending
- View spending by category
- View monthly spending
- View monthly spending by category
- View top expenses
- View average spending by category
- Check categories that exceed their budget
- Store data persistently using SQLite
- Validate expense input
- Unit tests for Expense and Tracker functionality
- Command-line interface using argparse

## Demo

Example command:

    python3 cli.py add --amount 250 --category food --date 2026-08-15 --note "Lunch"

Example list command:

    python3 cli.py list

Example report command:

    python3 cli.py report

## Installation

Clone the repository and move into the project directory:

    git clone <repository-url>
    cd expense-tracker

The project uses Python 3 and SQLite. No external Python packages are required.

## Usage

### Add an expense

    python3 cli.py add --amount 250 --category food --date 2026-08-15 --note "Lunch"

### List expenses

    python3 cli.py list

### Generate a report

    python3 cli.py report

### Run tests

    python3 -m unittest discover -v

## Project Structure

    expense-tracker/
    ├── category.py
    ├── database.py
    ├── expense.py
    ├── tracker.py
    ├── cli.py
    ├── main.py
    ├── schema.sql
    ├── reports.sql
    ├── test_expense.py
    ├── test_tracker.py
    ├── day10.md
    ├── day11.md
    ├── day12.md
    └── README.md

## Design Decisions

### Database layer

All SQL queries are kept inside database.py. This keeps database operations separate from the application's business logic.

### Tracker layer

The Tracker class handles application-level operations such as calculating totals, filtering expenses, checking budgets, converting database rows into Expense objects, and generating summaries. Therefore, it still has a meaningful responsibility.

### Testing

Tests use an isolated SQLite in-memory database so test data does not modify the persistent expenses.db database.

## Testing

The project currently contains 17 unit tests:

- 8 tests for the Expense class
- 9 tests for the Tracker class

Run all tests with:

    python3 -m unittest discover -v

All 17 tests currently pass.

## Next Additions

Possible future improvements include:

- Edit or delete expenses
- Add more advanced reporting
- Improve CLI error messages
- Add more comprehensive test coverage
- Add a graphical or web interface
- Add support for exporting reports
