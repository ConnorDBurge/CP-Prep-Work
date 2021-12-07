import inquirer
import re

questions = [
    inquirer.Text('category_name', message="Category"),
    inquirer.Text('name', message="Transaction Name"),
    inquirer.Text('amount', message="Amount")
]
answers = inquirer.prompt(questions)  # returns a dictionary
print(answers)

questions = [
    inquirer.Text('user', message='Please enter your github username',
                  validate=lambda _, x: x != '.'),
    inquirer.Password('password', message='Please enter your password'),
    inquirer.Text('repo', message='Please enter the repo name',
                  default='default'),
    inquirer.Checkbox('topics', message='Please define your type of project?', choices=[
                      'common', 'backend', 'frontend'], ),
    inquirer.Text(
        'organization', message='If this is a repo from a organization please enter the organization name, if not just leave this blank'),
    inquirer.Confirm(
        'correct',  message='This will delete all your current labels and create a new ones. Continue?', default=False),
]
answers = inquirer.prompt(questions)  # returns a dictionary
print(answers)
