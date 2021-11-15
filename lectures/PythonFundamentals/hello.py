greeting = 'Hello World'
print(greeting)


def is_greater_than_five(x):  # function
    if x > 5:  # if-statement
        # output to console, with string interpolation
        print(f"{x} is greater than 5")
    else:
        print(f"{x} is less than or equal to 5")


num = 9
is_greater_than_five(num)
num = 2
is_greater_than_five(num)

# global variable => value is accessible anywhere (generally bad practice)
some_var = "A"
# global variable, constant value (convention) in CAPS => value isn't intended to change
CONST_VAR = "B"


def my_func(x):
    local_var = "C"  # local variable => value is only available in current function

    if x > 5:
        other_local_var = "D"
    else:
        other_local_var = "d"

    print(local_var)
    print(other_local_var)  # variables are not confined to control blocks


my_func(9)
print(some_var)
print(local_var)  # error
