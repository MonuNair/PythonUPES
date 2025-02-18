class ClassName:
    # Constructor method (initializer)
    def __init__(self, attribute):
        self.attribute = attribute  # Instance variable

    # Method (function inside a class)
    def show_attribute(self):
        print("Attribute value:", self.attribute)

# Creating an object of the class
obj = ClassName("Hello, Python!")
obj.show_attribute()