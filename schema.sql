-- Stores the categories available for expenses.
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    budget REAL
);

-- Stores individual expenses and links each expense to a category.
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    amount REAL NOT NULL CHECK (amount > 0),
    category_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    note TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
