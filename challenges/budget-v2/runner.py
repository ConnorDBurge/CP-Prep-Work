from classes.budget import Budget

# income = Category('income')
# income.transaction('Salary 1', '1317')
# income.transaction('Salary 2', '1500')

# bills = Category('bills')
# bills.transaction('Cox', '178')
# bills.transaction('Netflix', '4.00')
# bills.transaction('Netflix', '4.99')
# bills.transaction('USAA', '145.76')

budget = Budget('December')
budget.transaction('income', 'Salary 1', '1317')
budget.transaction('bills', 'Netflix', '4.99')
budget.transaction('income', 'Salary 2', '1500')
budget.transaction('bills', 'Cox', '178')
budget.transaction('transportation', 'Gas', '240')
budget.transaction('bills', 'Cox', '154')


# print(budget.get_income())
# print(budget.get_expenses())
# print(budget.get_remaining())

print(str(budget))
