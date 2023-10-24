# Advanced Class

- Class and Static Method
- Class Attribute
- Data Class
- Dynamic Attribute
- Typing

## Class and Static Method

By convention, the first parameter of a method is `self`. It points to the newly created instance. In runtime, Python interpreter provides the argument. These methods are called __instance methods__.

Python has two other types of methods:

- Class method: the first parameter is `cls` that points to the current class type. In runtime, Python interpreter provides the `cls` argument. Class methods are used to modify class attributes that will be introduced later.
- Static method: Python interpreter doesn't provide any argument. These methods work like functions because they cannot change any class or instance attributes. They are defined in the class namespace. 

### Class Method

Python uses the `@classmethod` decorator to specify a class method. A __decorator__ is a Python programming constructor that provide addition information or functions for a class, a function, a class attribute or a method.

You can call a class method without an instance using the `ClassName.method()` syntax. You can also call it with a class instance. Python interpreter provides the `cls` argument for both types of call.


```python
class MyClass:

    @classmethod
    def call_method(cls):
        print(f"class method of {cls}")

MyClass.call_method() # class method of <class '__main__.MyClass'>

my = MyClass() 
my.call_method() # class method of <class '__main__.MyClass'>

```

### Static Method

Python uses the `@staticmethod` decorator to specify a static method. 

You can call a class method without an instance using the `ClassName.method()` syntax. You can also call it with a class instance. Python interpreter provides no argument for both types of call.


```python
class MyClass:

    @staticmethod
    def call_method(number):
        print(f"call static method with argument {number}")

MyClass.call_method(42) # call static method with argument 42

my = MyClass()
my.call_method(42) # call static method with argument 42

```

## Class Attribute

A class is a blueprint for its instances.

A class is an object in Python that can have its own attributes.

A class attribute is defined directly in a class body.

A class attribute can be access using both class name and the instances of the class.

If you write an attribute using an instance, it creates an instance attribute.


```python
class MyClass:
    class_count = 1

    def __init__(self, count):
        self.instance_count = count

print(MyClass.class_count) # 1

MyClass.class_count += 1
print(MyClass.class_count) # 2

my = MyClass(42)
print(my.class_count) # 2
print(my.instance_count) # 42

# this creates a new instance attributed named class_count
my.class_count = 7 
print(my.class_count) # 7

# class attribute is still there
print(MyClass.class_count) # 2

```

### Why Use Class Attribute

Python developers use class attributes in two common cases:

- with descriptor (to be introduced later), to define instance attributes with some processing logic.
- To store class level data that is not associated with an instance. 

For example, keep a count of number of instances created. To avoid repeating the class name, you can use the __special attribute__ `self.__class__` to access its class object. In Python, identifiers start and end with double underscore are __special__ identifiers.  


```python
class MyClass:
    count = 0

    def __init__(self, number):
        self.__class__.count += 1
        self.number = number

first = MyClass(5)
second = MyClass(7)
print(MyClass.count) # 2

```

## Data Class

A data class consists of a collection of attributes. The purpose is to make it easy to use the composite data and its parts.

Python provides three help classes for building data classes.

- `collections.namedtuple`: a function to build composite data with named attributes.
- `typing.NamedTuple`: a class used to build composite data with typed and named attributes.
- `dataclasses.dataclass`: a decorator used to build data classes.

### Why Data Class

There are a lot of work to do to define a composite data class because a simple definition is not good enough.

- The representation string is useless
- The `==` uses the default identity equality that is incorrect here.


```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(3, 5)
point2 = Point(3, 5)
print(point1) # <__main__.Point object at 0x1168c8390>
print(point1 == point2) # False

```

### `collections.namedtuple`

The `namedtuple` is a simple solution to fix the simple class issues. You can use `from module import name` syntax to import an identifier from the module.


```python
from collections import namedtuple

Point = namedtuple("Point", "x y")

point1 = Point(3, 5)
point2 = Point(3, 5)
print(point1) # Point(x=3, y=5)
print(point1 == point2) # True

```

### `typing.NamedTuple`

The `NamedTuple` provides type hint to a data class. It works similar as `namedtuple`. In an IDE, it provides the type hints of data components. However, it doesn't enforce the data type in the runtime.


```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float = 0
    y: float = 0

point1 = Point(3, 5)
point2 = Point(3, 5)
print(point1) # Point(x=3, y=5)
print(point1 == point2) # True

```

### `dataclasses.dataclass`

The `dataclass` is a decorator for building mutable or immutable data class.


```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

point1 = Point(3, 5)
point2 = Point(3, 5)
print(point1) # Point(x=3, y=5)
print(point1 == point2) # True

```

### Which One to Use

- Simple immutable composite data: `namedtuple`
- Simple with type hints: `NamedTuple`
- Rich function or mutable composite data: `dataclass`

## Dynamic Attribute

In Python, both data attributes and methods of a class are collectively called as __attributes__.

Methods are different from data attributes because they are __callable__ using a so-call function call syntax `obj.method()`.

Dynamic attributes are calculated but are accessed as regular data attributes.

Python provides `@property` decorator to define the read and write operations for dynamic attributes.


```python
class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    @property
    def fullname(self):
        return self.firstname + " " + self.lastname
    
    @fullname.setter
    def fullname(self, full):
        self.firstname, self.lastname = full.split()

tom = Person("Tom", "Hank")
print(tom.fullname) # Tom Hank

tom.fullname = "Tommy Hanks"
print(tom.firstname, tom.lastname) # Tommy Hanks   

```

### Other Dynamic Attributes

When you want to define some logics behind an attribute that can be used in multiple places, you can define the so-called __descriptor__ classes that control the read, write, and delete of class attributes.

Additionally, special class methods such as `__getattr__` and `__setattr__` can also customize the attribute access behaviors.

These advanced features are introduced in the Python data model section.

## Typing

The type of a value defines the set of valid operations for the value.

Typing is the mechanism of a programming language for type definition and type checking.

A class defines the type of its instances. Its methods define its data operations.

Therefore, class and class inheritance define the valid operations of an instance.

### Dynamic Typing vs Static Typing

Because there is no separate compiling stage for a Python program, Python is categorized as a __dynamic typing__ program language. A dynamic typing language checks data type and operations at runtime.

Programming languages such as C, C++, Java and C# can check types and operations when they compile source code, they are called __static typing__ program language. These language can find many type errors during the compiling phase. 

Since Python 3.5, Python introduces __type hints__ that allow external type checker tools to check type and operations before the code execution. It helps to improve the code quality by finding out invalid daa operations such as dividing a string by a number.

### Duck Typing and Goose Typing

As a dynamic typing program language, Python supports two run-time typing mechanism:

- duck typing: just run the operation, throw an exception if the value doesn't support it.
- goose typing: use `isinstance` to check the instance type, then run the corresponding operations.

### Duck Typing Example

Python supports duck typing from the beginning. It got the name from the so-called __duck test__: " if it quacks like a duck, then it is a duck".

For example, all Python objects have a special method `__str__`, either inherit from `object` or defined in their classes. The method creates a string representation of the object, Therefore, you can call `print(obj)` for any object. `print` just call the `obj.__str__()` and write the string.

The duck typing allows you to apply an operation on different types as long as they define a common method.

Following is an example:


```python
class Duck:
    def quack(self):
        print("quack, quack")

class Player:
    def quack(self):
        print("quack like a duck")


actors = [Duck(), Player()]
for actor in actors:
    actor.quack()

```

### Goose Typing Example

In goose typing, you check the type of an instance and call the corresponding operations.


```python
class Duck:
    def quack(self):
        print("quack, quack")

class Dog:
    def bark(self):
        print("bark, bark")

actors = [Duck(), Dog()]

for actor in actors:
    if isinstance(actor, Duck):
        actor.quack()
    elif isinstance(actor, Dog):
        actor.bark()
    else:
        print("oops")

```

### Abstract Base Classes

To support goose typing, Python defines many __abstract base classes__ in its `collection.abc` module. Here the word `abstract` means that you don't create an instance for the classes. They are used for goose typing purpose.

The supported operations are in [`collection.abc` document](https://docs.python.org/3/library/collections.abc.html).

For example, if a class defines the special `__len__` method, then you can call `len` function on all its instances.


```python
import collections.abc

# return None if the object doesn't support len() operation
def get_len_safe(my_obj):
    size = None
    if isinstance(my_obj, collections.abc.Sized):
        size = len(my_obj)
    
    return size

```
