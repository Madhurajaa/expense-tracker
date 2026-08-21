import sqlite3


class Database:
    """Handle all database operations for the expense tracker."""

    def __init__(self, path="expenses.db"):
        """Open a database connection and enable foreign keys."""
        self.conn = sqlite3.connect(path)
        self.conn.execute("PRAGMA foreign_keys = ON")

    def add_category(self, name, budget):
        """Insert a category and return its new ID."""
        cursor = self.conn.execute(
            "INSERT INTO categories (name, budget) VALUES (?, ?)",
            (name, budget),
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_category_by_name(self, name):
        """Return a category row by name, or None if it does not exist."""
        return self.conn.execute(
            "SELECT id, name, budget FROM categories WHERE name = ?",
            (name,),
        ).fetchone()

    def get_expenses_by_category(self, category_id):
        """Return expenses belonging to a category."""
        return self.conn.execute(
            """
            SELECT id, amount, category_id, date, note
            FROM expenses
            WHERE category_id = ?
            ORDER BY id
            """,
            (category_id,),
        ).fetchall()

    def add_expense(self, amount, category_id, date, note):
        """Insert an expense and return its new ID."""
        cursor = self.conn.execute(
            """
            INSERT INTO expenses (amount, category_id, date, note)
            VALUES (?, ?, ?, ?)
            """,
            (amount, category_id, date, note),
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_all_expenses(self):
        """Return all expenses ordered by ID."""
        return self.conn.execute(
            """
            SELECT id, amount, category_id, date, note
            FROM expenses
            ORDER BY id
            """
        ).fetchall()

    def get_category_by_id(self, category_id):
        """Return a category row by ID, or None if it does not exist."""
        return self.conn.execute(
            "SELECT id, name, budget FROM categories WHERE id = ?",
            (category_id,),
        ).fetchone()

    def close(self):
        """Close the database connection."""
        self.conn.close()
