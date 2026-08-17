from expense import Expense
from tracker import Tracker
from category import Category


def main():
    """Create a tracker, add expenses and display a summary."""

    tracker = Tracker()

    expenses = [
        Expense(250, "food", "2026-08-10", "Lunch"),
        Expense(180, "food", "2026-08-11", "Breakfast"),
        Expense(1200, "rent", "2026-08-01", "Monthly rent"),
        Expense(300, "travel", "2026-08-05", "Bus tickets"),
        Expense(500, "travel", "2026-08-07", "Auto fare"),
        Expense(150, "food", "2026-08-12", "Snacks"),
    ]

    for expense in expenses:
        tracker.add(expense)

    tracker.add_category(Category("food", 500))
    tracker.add_category(Category("rent", 2000))
    tracker.add_category(Category("travel", 1000))

    print("Expenses")
    print("-" * 50)

    for expense in tracker.list_all():
        print(expense)

    print("\nSummary")
    print("-" * 50)
    print(tracker.summary())


if __name__ == "__main__":
    main()

