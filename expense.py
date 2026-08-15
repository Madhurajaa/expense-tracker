from datetime import datetime


class Expense:
    """Represent a single expense with validation and useful operations."""

    def __init__(self, amount, category, date, note=""):
        """Initialize an expense after validating its input."""

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Amount must be a positive number.")

        if amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must not be empty.")

        if not isinstance(date, str) or not date.strip():
            raise ValueError("Date must not be empty.")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Date must be YYYY-MM-DD format, got: {date}"
            )

        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def __str__(self):
        """Return a readable one-line description of the expense."""
        return f"{self.date} | {self.category} | ₹{self.amount:.2f} | {self.note}"

    def describe(self):
        """Return a longer formatted description of the expense."""
        return (
            f"Expense Details:\n"
            f"  Amount: ₹{self.amount:.2f}\n"
            f"  Category: {self.category}\n"
            f"  Date: {self.date}\n"
            f"  Note: {self.note}"
        )

    def to_dict(self):
        """Return the expense as a plain dictionary."""
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note": self.note,
        }
