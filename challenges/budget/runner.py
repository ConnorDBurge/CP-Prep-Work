from classes.budget import Budget

budget = Budget('December')

budget.increse_transaction('income', 'Salary 1', '2000')

budget.increse_transaction('bills', 'Cox', '178')
budget.increse_transaction('bills', 'Verizon', '103')
budget.reduce_transaction('bills', 'Cox', '134')

budget.increse_transaction('food', 'Grocery', '420')
budget.increse_transaction('food', 'Restaurant', '60')

budget.increse_transaction('transportation', 'Gas', '220')
budget.increse_transaction('transportation', 'Registration', '145')

print(str(budget))
