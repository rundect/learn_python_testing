class MyClass:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        return "hi my name is: {}".format(self.name)


# instantiates MyClass and calls a method on the object
def function_b():
    param1 = MyClass("foo")

    # returns "hi my name is: foo"
    return param1.sayhi()


