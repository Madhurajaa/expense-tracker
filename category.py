class Category:
    """Represent an expense category with a monthly budget."""

    VALID_CATEGORIES = ["food", "rent", "transport", "utilities", "other"]

    def __init__(self, name, budget=None):
        """Initialize a category with a name and optional budget."""

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Category must not be empty.")

        if name not in self.VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {name}")

        self.name = name
        self.budget = budget

    def __repr__(self):
        """Return a developer-friendly representation of the category."""
        return f"Category('{self.name}', {self.budget})"
