import unittest
from expense import Expense


class TestExpense(unittest.TestCase):

    def test_valid_expense(self):
        expense = Expense(250, "food", "2026-08-15", "Lunch")

        self.assertEqual(expense.amount, 250)
        self.assertEqual(expense.category, "food")
        self.assertEqual(expense.date, "2026-08-15")
        self.assertEqual(expense.note, "Lunch")

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            Expense(-100, "food", "2026-08-15", "Lunch")

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            Expense(0, "food", "2026-08-15", "Lunch")

    def test_boolean_amount(self):
        with self.assertRaises(ValueError):
            Expense(True, "food", "2026-08-15", "Lunch")

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            Expense(100, "travel", "2026-08-15", "Travel")

    def test_wrong_date_format(self):
        with self.assertRaises(ValueError):
            Expense(100, "food", "15-08-2026", "Lunch")

    def test_impossible_date(self):
        with self.assertRaises(ValueError):
            Expense(100, "food", "2026-02-30", "Lunch")

    def test_to_dict(self):
        expense = Expense(250, "food", "2026-08-15", "Lunch")

        result = expense.to_dict()

        self.assertEqual(
            result,
            {
                "amount": 250,
                "category": "food",
                "date": "2026-08-15",
                "note": "Lunch",
            },
        )


if __name__ == "__main__":
    unittest.main()
