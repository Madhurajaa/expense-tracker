# Day 10 Journal

## 1. What changed when the calculation functions became methods on Tracker?

Earlier, `calculate_total()` and `calculate_category_totals()` were separate functions that received the expenses list as an argument.

In Day 10, I moved this logic into the `Tracker` class as methods. Since Tracker already stores the expenses in `self.expenses`, the methods can directly work with the tracker's own data.

This made the code more organized because Tracker is now responsible for managing and calculating information about its expenses.

## 2. Why does Category exist now when it didn't earn its place yesterday?

Yesterday, Category did not have enough responsibility to be a separate class.

In Day 10, Category has a real purpose because it stores a category name and monthly budget. Tracker can use Category objects to check whether spending has gone over the budget using `over_budget()`.

So Category is now useful because it has a meaningful responsibility in the expense tracking system.

## 3. Where were you tempted to use inheritance, if anywhere, and why didn't you?

I did not use inheritance in this task because `Expense`, `Category`, and `Tracker` do not have a parent-child relationship.

`Tracker` manages Expense objects and Category objects, while Expense and Category have their own responsibilities. Composition was more suitable than inheritance for this design.

## 4. How did the DSA problems go?

I completed both DSA problems: Group Anagrams and Best Time to Buy and Sell Stock.

For Group Anagrams, I used a sorted version of each word as the dictionary key so that words with the same letters are grouped together.

For Best Time to Buy and Sell Stock, I used a one-pass approach by tracking the minimum price seen so far and the maximum profit