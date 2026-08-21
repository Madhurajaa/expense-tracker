from database import Database
from expense import Expense
from category import Category


class Tracker:
    """Manage expenses and categories using persistent database storage."""

    def __init__(self):
        """Initialize the tracker with a database connection."""
        self.db = Database()
        self.categories = {}

    def add(self, expense):
        """Add an Expense object to the database."""
        category = self.db.get_category_by_name(expense.category)

        if category is None:
            raise ValueError(
                f"Category '{expense.category}' does not exist."
            )

        category_id = category[0]

        self.db.add_expense(
            expense.amount,
            category_id,
            expense.date,
            expense.note,
        )

    def _expense_from_row(self, row):
        """Convert a database expense row into an Expense object."""
        expense_id, amount, category_id, date, note = row
        
        category = self.db.get_category_by_id(category_id)

        if category is None:
            raise ValueError(
                f"Category ID {category_id} does not exist."
            )

        return Expense(
            amount,
            category[1],
            date,
            note or "",
        )

    def list_all(self):
        """Return all expenses from the database."""
        rows = self.db.get_all_expenses()
        return [self._expense_from_row(row) for row in rows]

    def total(self):
        """Return the sum of all expense amounts."""
        return sum(expense.amount for expense in self.list_all())

    def total_by_category(self):
        """Return total spending for each expense category."""
        totals = {}

        for expense in self.list_all():
            if expense.category not in totals:
                totals[expense.category] = 0

            totals[expense.category] += expense.amount

        return totals

    def filter_by_category(self, name):
        """Return expenses that match the given category."""
        category = self.db.get_category_by_name(name)

        if category is None:
            return []

        rows = self.db.get_expenses_by_category(category[0])
        return [self._expense_from_row(row) for row in rows]

    def add_category(self, category):
        """Add a Category object to the database."""
        self.db.add_category(category.name, category.budget)
        self.categories[category.name] = category

    def over_budget(self):
        """Return categories where spending exceeds the monthly budget."""
        over_budget_categories = []

        totals = self.total_by_category()

        for name, category in self.categories.items():
            if category.budget is not None:
                if totals.get(name, 0) > category.budget:
                    over_budget_categories.append(category)

        return over_budget_categories

    def summary(self):
        """Return a formatted summary of all tracked expenses."""
        expenses = self.list_all()
        lines = []

        lines.append(f"Total spend: ₹{self.total():.2f}")

        lines.append("Spend by category:")
        for category, amount in self.total_by_category().items():
            lines.append(f"  {category}: ₹{amount:.2f}")

        lines.append(f"Number of expenses: {len(expenses)}")

        if expenses:
            largest = max(expenses, key=lambda expense: expense.amount)
            lines.append(f"Largest expense: {largest}")
        else:
            lines.append("Largest expense: None")

        over_budget = self.over_budget()

        lines.append("Over budget:")
        if over_budget:
            for category in over_budget:
                lines.append(f"  {category.name}")
        else:
            lines.append("  None")

        return "\n".join(lines)
