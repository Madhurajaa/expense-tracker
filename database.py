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

    def total_spend(self):
        """Return the total amount spent."""
        return self.conn.execute(
            """
            SELECT SUM(amount) AS total_spend
            FROM expenses
            """
        ).fetchone()[0]

    def spend_by_category(self):
        """Return total spending grouped by category."""
        return self.conn.execute(
            """
            SELECT categories.name,
                   SUM(expenses.amount) AS total_spend
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            GROUP BY categories.name
            ORDER BY total_spend DESC
            """
        ).fetchall()

    def monthly_spend(self, month):
        """Return total spending for a given month."""
        return self.conn.execute(
            """
            SELECT SUM(amount) AS total_spend
            FROM expenses
            WHERE date >= ?
              AND date < date(?, '+1 month')
            """,
            (month + "-01", month + "-01"),
        ).fetchone()[0]

    def monthly_spend_by_category(self, month):
        """Return spending per category for a given month."""
        return self.conn.execute(
            """
            SELECT categories.name,
                   SUM(expenses.amount) AS total_spend
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            WHERE expenses.date >= ?
              AND expenses.date < date(?, '+1 month')
            GROUP BY categories.name
            ORDER BY total_spend DESC
            """,
            (month + "-01", month + "-01"),
        ).fetchall()

    def top_expenses(self, limit=5):
        """Return the largest expenses."""
        return self.conn.execute(
            """
            SELECT expenses.amount,
                   categories.name,
                   expenses.date,
                   expenses.note
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            ORDER BY expenses.amount DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    def over_budget_categories(self):
        """Return categories whose spending exceeds their budget."""
        return self.conn.execute(
            """
            SELECT categories.name,
                   categories.budget,
                   SUM(expenses.amount) AS total_spent
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            GROUP BY categories.id
            HAVING SUM(expenses.amount) > categories.budget
            """
        ).fetchall()

    def average_spend_by_category(self):
        """Return average spending per category."""
        return self.conn.execute(
            """
            SELECT categories.name,
                   AVG(expenses.amount) AS average_spend
            FROM expenses
            JOIN categories
                ON expenses.category_id = categories.id
            GROUP BY categories.name
            """
        ).fetchall()

    def expenses_per_month(self):
        """Return the number of expenses for each month."""
        return self.conn.execute(
            """
            SELECT strftime('%Y-%m', date) AS month,
                   COUNT(*) AS expense_count
            FROM expenses
            GROUP BY strftime('%Y-%m', date)
            ORDER BY month
            """
        ).fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()
