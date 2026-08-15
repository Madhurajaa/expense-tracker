from expense import Expense


def calculate_total(expenses):
    """Calculate the total amount of all expenses."""
    return sum(expense.amount for expense in expenses)


def calculate_category_totals(expenses):
    """Calculate the total amount for each expense category."""
    totals = {}

    for expense in expenses:
        if expense.category not in totals:
            totals[expense.category] = 0

        totals[expense.category] += expense.amount

    return totals


def main():
    """Create expenses and display their details and totals."""

    expenses = [
        Expense(250, "food", "2026-08-10", "Lunch"),
        Expense(180, "food", "2026-08-11", "Breakfast"),
        Expense(1200, "rent", "2026-08-01", "Monthly rent"),
        Expense(300, "travel", "2026-08-05", "Bus tickets"),
        Expense(500, "travel", "2026-08-07", "Auto fare"),
        Expense(150, "food", "2026-08-12", "Snacks"),
    ]

    print("Expenses")
    print("-" * 50)

    for expense in expenses:
        print(expense)

    total = calculate_total(expenses)

    print("\nTotal Expenses")
    print("-" * 50)
    print(f"₹{total:.2f}")

    category_totals = calculate_category_totals(expenses)

    print("\nCategory Totals")
    print("-" * 50)

    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")


if __name__ == "__main__":
    main()

