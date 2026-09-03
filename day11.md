# Day 11 – SQL Persistence

## 1. Why is category its own table?

A category is shared by many expenses. Storing categories separately avoids duplicate data and allows a budget to be associated with each category. Expenses reference categories using a foreign key.

## 2. What changed inside Tracker?

The public methods stayed the same, but the implementation changed from Python lists and dictionaries to SQLite database operations through the Database class. This allows expense data to persist after the program exits.

## 3. Why not use f-strings for SQL?

Parameterized queries using `?` placeholders are safer because user input is treated as data rather than being directly inserted into the SQL statement. This also avoids SQL injection problems.

## 4. DSA

DSA practice was continued separately alongside the database implementation.
