import argparse

from database import Database
from expense import Expense


def main():
    """Run the expense tracker command-line interface."""

    parser = argparse.ArgumentParser(description="Expense tracker")

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--note", default="")

    # List command
    list_parser = subparsers.add_parser("list", help="List expenses")
    list_parser.add_argument("--category", help="Filter by category")

    # Report command
    report_parser = subparsers.add_parser(
        "report",
        help="Show spending reports",
    )
    report_parser.add_argument("--month", help="Month as YYYY-MM")

    args = parser.parse_args()
    db = Database()

    try:
        if args.command == "add":
            expense = Expense(
                args.amount,
                args.category,
                args.date,
                args.note,
            )

            category = db.get_category_by_name(expense.category)

            if category is None:
                raise ValueError(
                    f"Category '{expense.category}' does not exist."
                )

            db.add_expense(
                expense.amount,
                category[0],
                expense.date,
                expense.note,
            )

            print("Expense added successfully.")

        elif args.command == "list":
            if args.category:
                category = db.get_category_by_name(args.category)

                if category is None:
                    raise ValueError(
                        f"Invalid category: {args.category}"
                    )

                expenses = db.get_expenses_by_category(category[0])
            else:
                expenses = db.get_all_expenses()

            print("ID | Amount | Category ID | Date | Note")
            print("-" * 60)

            for expense in expenses:
                print(
                    f"{expense[0]} | "
                    f"₹{expense[1]:.2f} | "
                    f"{expense[2]} | "
                    f"{expense[3]} | "
                    f"{expense[4] or ''}"
                )

        elif args.command == "report":
            print("Total spend:")
            print(f"₹{db.total_spend():.2f}")

            print("\nSpend by category:")
            for category, amount in db.spend_by_category():
                print(f"  {category}: ₹{amount:.2f}")

            if args.month:
                print(f"\nSpend for {args.month}:")
                print(f"₹{db.monthly_spend(args.month):.2f}")

                print(f"\nSpend by category for {args.month}:")
                for category, amount in db.monthly_spend_by_category(
                    args.month
                ):
                    print(f"  {category}: ₹{amount:.2f}")

            print("\nTop 5 expenses:")
            for amount, category, date, note in db.top_expenses():
                print(
                    f"  ₹{amount:.2f} | "
                    f"{category} | "
                    f"{date} | "
                    f"{note or ''}"
                )

            print("\nOver-budget categories:")
            over_budget = db.over_budget_categories()

            if over_budget:
                for category, budget, spent in over_budget:
                    print(
                        f"  {category}: "
                        f"budget ₹{budget:.2f}, "
                        f"spent ₹{spent:.2f}"
                    )
            else:
                print("  None")

            print("\nAverage spend by category:")
            for category, average in db.average_spend_by_category():
                print(f"  {category}: ₹{average:.2f}")

            print("\nExpenses per month:")
            for month, count in db.expenses_per_month():
                print(f"  {month}: {count}")

    except ValueError as error:
        print(f"Error: {error}")
        return 1

    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
