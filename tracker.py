from category import Category


class Tracker:
    """Manage a collection of Expense objects."""

    def __init__(self):
        """Initialize an empty expense tracker."""
        self.expenses = []
        self.categories = {}

    def add(self, expense):
        """Add an Expense object to the tracker."""
        self.expenses.append(expense)

    def list_all(self):
        """Return all expenses in the tracker."""
        return self.expenses

    def total(self):
        """Return the sum of all expense amounts."""
        return sum(expense.amount for expense in self.expenses)

    def total_by_category(self):
        """Return total spending for each expense category."""
        totals = {}

        for expense in self.expenses:
            if expense.category not in totals:
                totals[expense.category] = 0

            totals[expense.category] += expense.amount

        return totals

    def filter_by_category(self, name):
        """Return expenses that match the given category."""
        return [
            expense
            for expense in self.expenses
            if expense.category == name
        ]

    def add_category(self, category):
        """Add a Category object to the tracker."""
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
        lines = []

        lines.append(f"Total spend: ₹{self.total():.2f}")

        lines.append("Spend by category:")
        for category, amount in self.total_by_category().items():
            lines.append(f"  {category}: ₹{amount:.2f}")

        lines.append(f"Number of expenses: {len(self.expenses)}")

        if self.expenses:
            largest = max(self.expenses, key=lambda expense: expense.amount)
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