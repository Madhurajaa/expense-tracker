-- 1. Total spend across all expenses
SELECT SUM(amount) AS total_spend
FROM expenses;


-- 2. Spend per category, highest first
SELECT categories.name,
       SUM(expenses.amount) AS total_spend
FROM expenses
JOIN categories
    ON expenses.category_id = categories.id
GROUP BY categories.name
ORDER BY total_spend DESC;


-- 3. Spend for a given month
SELECT SUM(amount) AS total_spend
FROM expenses
WHERE date >= '2026-08-01'
AND date < '2026-09-01';


-- 4. Spend per category for a given month
SELECT categories.name,
       SUM(expenses.amount) AS total_spend
FROM expenses
JOIN categories
    ON expenses.category_id = categories.id
WHERE expenses.date >= '2026-08-01'
AND expenses.date < '2026-09-01'
GROUP BY categories.name
ORDER BY total_spend DESC;


-- 5. Five largest single expenses
SELECT expenses.amount,
       categories.name,
       expenses.date,
       expenses.note
FROM expenses
JOIN categories
    ON expenses.category_id = categories.id
ORDER BY expenses.amount DESC
LIMIT 5;


-- 6. Categories over budget
SELECT categories.name,
       categories.budget,
       SUM(expenses.amount) AS total_spent
FROM expenses
JOIN categories
    ON expenses.category_id = categories.id
GROUP BY categories.id
HAVING SUM(expenses.amount) > categories.budget;


-- 7. Average expense amount per category
SELECT categories.name,
       AVG(expenses.amount) AS average_spend
FROM expenses
JOIN categories
    ON expenses.category_id = categories.id
GROUP BY categories.name;


-- 8. Count of expenses per month
SELECT strftime('%Y-%m', date) AS month,
       COUNT(*) AS expense_count
FROM expenses
GROUP BY strftime('%Y-%m', date)
ORDER BY month;
