class Category:
    """Represent an expense category with a monthly budget."""

    def __init__(self, name, budget=None):
        """Initialize a category with a name and optional budget."""
        self.name = name
        self.budget = budget

    def __repr__(self):
        """Return a developer-friendly representation of the category."""
        return f"Category('{self.name}', {self.budget})"