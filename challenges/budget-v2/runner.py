from classes.budgets import Budgets

budgets = Budgets()

budgets.new_transaction('may', 'income', 'Salary 1', '156.17')
budgets.new_transaction('may', 'bills', 'Cox', '156.17')

# budgets.change_transaction_name('may', 'income', 'Salary 1', 'Connor Paycheck')

for k, v in budgets.budgets.items():
    print(str(v))
