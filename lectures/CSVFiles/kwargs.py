my_dict = {
    'donuts': 'yummy',
    'beans': 'gross'
}


def my_func(donuts, beans):
    print(donuts, beans)


my_func(**my_dict)
