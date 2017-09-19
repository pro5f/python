class MyClass2:
    """A simple example class"""
    def __init__(self):
        self.i = 67890
    def f(self):
        print "Hello MyClass2"
    def v(self, input):
        print("Input = {0}".format(input))

x = MyClass2()
print(x.__doc__)
print(x.i)
x.f()
x.v(22)
