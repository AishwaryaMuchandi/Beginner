# Create the custom Python classes which have methods and
# attributes and implement single inheritance, multiple inheritance,
# and multilevel inheritance

class Parent:
    def __init__(self):
        self.parent_attribute = "Parent Attribute"
    
    def parent_method(self):
        return "Parent Method"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = "Child Attribute"
    
    def child_method(self):
        return "Child Method"

child_instance = Child()

print(child_instance.parent_attribute)
print(child_instance.parent_method())
print(child_instance.child_attribute)
print(child_instance.child_method())

# MULTIPLE INHERITANCE

class Parent1:
    def method1(self):
        return "Method from Parent1"

class Parent2:
    def method2(self):
        return "Method from Parent2"

class Child(Parent1, Parent2):
    def method3(self):
        return "Method from Child"

child_instance = Child()

print(child_instance.method1())
print(child_instance.method2())
print(child_instance.method3())

# MULTILEVEL INHERITANCE

class GrandParent:
    def grandparent_method(self):
        return "Method from GrandParent"

class Parent(GrandParent):
    def parent_method(self):
        return "Method from Parent"

class Child(Parent):
    def child_method(self):
        return "Method from Child"


child_instance = Child()

print(child_instance.grandparent_method())
print(child_instance.parent_method())
print(child_instance.child_method())

