from classes.budget import Budget

budget = Budget('Decembers')
budget.increase_income('Salary 1', '1300')
budget.increase_income('Salary 2', '2000')
budget.reduce_income('Salary 2', '1000')
print(budget.income.income_dict)
print(budget.remaining_balance)
