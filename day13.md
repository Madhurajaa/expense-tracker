# Day 13 - Testing, Structural Review and Documentation

## What I Did

- Created unit tests for the Expense class.
- Created unit tests for the Tracker class.
- Used an in-memory SQLite database for isolated testing.
- Ran the complete test suite using unittest.
- Reviewed the project structure.
- Confirmed that SQL queries are kept inside database.py.
- Reviewed the responsibility of the Tracker class.
- Updated the README with project features, usage, testing, design decisions, and future improvements.
- Completed Day 13 DSA problems:
  - Two Sum II - Input Array Is Sorted
  - Move Zeroes

## Testing

Created:

- test_expense.py
- test_tracker.py

Total tests:

- 8 Expense tests
- 9 Tracker tests
- 17 tests overall

Command used:

    python3 -m unittest discover -v

Result:

    Ran 17 tests
    OK

## Structural Review

The Tracker class still has a meaningful responsibility because it handles business logic such as:

- Calculating total expenses
- Calculating totals by category
- Filtering expenses
- Checking category budgets
- Converting database rows into Expense objects
- Generating summaries

SQL queries remain inside database.py.

## What I Learned

- How to write unit tests using unittest.
- How setUp and tearDown help isolate tests.
- How to use SQLite :memory: databases for testing.
- How to test validation and edge cases.
- How to review separation of responsibilities in a project.
- How documentation helps make a project easier to understand and maintain.

## DSA

Completed:

- Two Sum II using the two-pointer approach.
- Move Zeroes using an in-place pointer approach.
