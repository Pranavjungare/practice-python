expenses= {
    "Food": 500,
    "Travel": 300,
    "Shopping": 1200,
    "Internet": 700,
    "Entertainment": 400,
    "Bills": 900
}

total_expense=0
highest_expense=0
highest_category=""

for category,amount in expenses.items():

    total_expense += amount

    if amount > highest_expense:
        highest_expense = amount
        highest_category = category

budget = 3000

print("\n-:Expense Report:-")
print("-----------------------------")

for category,amount in expenses.items():
    print(category,":",amount)

print("\nTotal Expenses :",total_expense)
print("Heighest Spending Category :",highest_category)

if total_expense > budget:
    print("\nWARNING: Budget exceded!")
else:
    print("Budget is under control")
print("\n----------------------------------")


