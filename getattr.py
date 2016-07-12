class A:
    def __init__(self):
        self.name = 'Tony'
        # self.age = 26
    def method(self):
        print "method print"


Instance = A()

print getattr(Instance, 'name', 'not find')
print getattr(Instance, 'age', 'not find')

print getattr(Instance, 'method', 'default')
print getattr(Instance, 'method', 'default')()


