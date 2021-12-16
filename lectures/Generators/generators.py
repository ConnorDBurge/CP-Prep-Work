import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "transactions.csv")


def csv_reader(filename):
    for row in open(filename, 'r'):
        yield row

# for i in csv_reader(path):
#     print(i)


# generator comprehension
x = (i for i in range(10))
for i in x:
    print(i)
