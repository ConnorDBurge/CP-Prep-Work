class A1:
    def print_something(self):
        print('A1')


class B1(A1):
    def print_something(self):
        print('B1')


class B2(A1):
    def print_something(self):
        print('B2')


class C1(B1, B2):
    # def print_something(self):
    #     print('C1')
    pass


c = C1()
c.print_something()
print(C1.__mro__)
