# Higher Order Functions

# a function can take another function as an arguments
def func(f, x):
    return f(x)

# A simple function to pass
def square(x):
    return x * x

# Using apply function to apply the square function
res = func(square, 5)
print(res)

"""
Functions as First-Class Objects:
In Python, functions are first-class objects, meaning that they can be treated like any other object, such as integers, strings, or lists. This gives functions a unique level of flexibility and allows them to be passed around and manipulated in ways that are not possible in many other programming languages.

What Does It Mean for Functions to Be First-Class Objects?
Can be assigned to variables: Functions can be assigned to variables and used just like any other value.
Can be passed as arguments: Functions can be passed as arguments to other functions.
Can be returned from other functions: Functions can return other functions, which is a key concept in decorators.
Can be stored in data structures: Functions can be stored in lists, dictionaries, or other data structures.

"""

# Understand from this example
def greet(name):
    return f"Hello, {name}"

say_hi = greet
print(say_hi("Alice")) # output: Hello, Alice

# Passing a function as an argument
def func(f, v):
    return f(v)

res = func(say_hi, "Vaibhav")
print(res)


# Returning function from another function
def make_multiplication(f): # decorator function which takes argument as a function
    def multiplication(g):  # wrapper function which is also takes an argument
        return f * g
    return multiplication

dbl = make_multiplication(5) # decorator function assigned to a variable as an object
print(dbl(2))

# types of decorators

# 1. Function Decorators:

# simple decorator function

def decorator(func):
    def wrapper():
        print("before calling function")
        func()
        print("after calling function")
    return wrapper

@decorator
def show():
    print("show worked!")

show()


# 2. Method Decorators:
"""
Used to decorate methods within a class. 
They often handle special cases, such as the self argument for instance methods.
"""
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("before function call")
        res = func(self, *args, **kwargs)
        print("after function call")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("say hello")

obj = MyClass()
obj.say_hello()

# 3. Class Decorators
"""
Class decorators are used to modify or enhance the behavior of a class. Like function decorators, 
class decorators 
are applied to the class definition. They work by taking the class as an argument and 
returning a modified version of the class.
"""

def func(cls): # a decorator function which takes a class as an argument
    cls.class_name = cls.__name__
    return cls

@func
class Person:
    pass

print(Person.class_name)

# chaining decorators
"""
In simpler terms chaining decorators means decorating a function with multiple decorators.
"""
def decorator(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decorator1(func):
    def wrapper():
        x = func()
        return 2 * x
    return wrapper

@decorator
@decorator1
def multiply():
    return 10

@decorator1
@decorator
def multiply1():
    return 10

print(multiply())
print(multiply1())


# builtin decorators

# 1. @staticmethod
"""
The @staticmethod decorator is used to define a method that doesn't operate on an 
instance of the class (i.e., it 
doesn't use self). Static methods are called on the class itself, not on an instance of the class.

it is also used in Abstraction in OOPs
"""

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# using the static method
res = MathOperations()
print(f"staticmethod: {res.add(1, 2)}")

# 2. @classmethod

"""
The @classmethod decorator is used to define a method that operates on the class itself (i.e., it uses cls). 
Class methods can access and modify class state that applies across all instances of the class.
"""

class Employee:
    raise_amount = 5

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# using class method
Employee.set_raise_amount(1.4)
print(f"class method: {Employee.raise_amount}")



# 3. @property decorator

"""
It is also used in encapsulation in OOPs.

The @property decorator is used to define a method as a property, which allows 
you to access it like an attribute. 
This is useful for encapsulating the implementation of a 
method while still providing a simple interface.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value

    @property
    def area(self):
        return self._radius * self._radius * math.pi

# Using the property
c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
print(c.area)