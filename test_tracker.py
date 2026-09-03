import unittest

from database import Database
from tracker import Tracker
from expense import Expense
from category import Category


class TestTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = Tracker()

        self.tracker.db.close()
        self.tracker.db = Database(":memory:")

        with open("schema.sql", "r") as file:
            self.tracker.db.conn.executescript(file.read())

        self.tracker.add_category(Category("food", 1000))
        self.tracker.add_category(Category("transport", 500))

    def tearDown(self):
        self.tracker.db.close()

    def test_empty_total(self):
        self.assertEqual(self.tracker.total(), 0)

    def test_one_expense_total(self):
        expense = Expense(250, "food", "2026-08-15", "Lunch")
        self.tracker.add(expense)

        self.assertEqual(self.tracker.total(), 250)

    def test_several_expenses_total(self):
        self.tracker.add(
            Expense(250, "food", "2026-08-15", "Lunch")
        )
        self.tracker.add(
            Expense(300, "transport", "2026-08-16", "Bus")
        )
        self.tracker.add(
            Expense(150, "food", "2026-08-17", "Snacks")
        )

        self.assertEqual(self.tracker.total(), 700)

    def test_total_by_category(self):
        self.tracker.add(
            Expense(250, "food", "2026-08-15", "Lunch")
        )
        self.tracker.add(
            Expense(300, "transport", "2026-08-16", "Bus")
        )
        self.tracker.add(
            Expense(150, "food", "2026-08-17", "Snacks")
        )

        self.assertEqual(
            self.tracker.total_by_category(),
            {
                "food": 400,
                "transport": 300,
            },
        )

    def test_filter_by_category(self):
        self.tracker.add(
            Expense(250, "food", "2026-08-15", "Lunch")
        )
        self.tracker.add(
            Expense(300, "transport", "2026-08-16", "Bus")
        )

        expenses = self.tracker.filter_by_category("food")

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].category, "food")
        self.assertEqual(expenses[0].amount, 250)

    def test_filter_missing_category(self):
        expenses = self.tracker.filter_by_category("rent")

        self.assertEqual(expenses, [])

    def test_over_budget(self):
        self.tracker.add(
            Expense(600, "food", "2026-08-15", "Groceries")
        )
        self.tracker.add(
            Expense(500, "food", "2026-08-16", "Dinner")
        )

        result = self.tracker.over_budget()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "food")

    def test_under_budget(self):
        self.tracker.add(
            Expense(400, "food", "2026-08-15", "Groceries")
        )

        result = self.tracker.over_budget()

        self.assertEqual(result, [])

    def test_budget_exactly_equal(self):
        self.tracker.add(
            Expense(1000, "food", "2026-08-15", "Groceries")
        )

        result = self.tracker.over_budget()

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
