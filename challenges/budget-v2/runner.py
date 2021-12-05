from classes.category import Category

income = Category('income')
income.transaction('Salary 1', '1317')
income.transaction('Salary 2', '1500')

bills = Category('bills')
bills.transaction('Cox', '178')
bills.transaction('Netflix', '4.00')
bills.transaction('Netflix', '4.99')
bills.transaction('USAA', '145.76')


print(income.str(0))
print(bills.str(0))
