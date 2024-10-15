# Python

The first sentence of [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

> Python is an easy to learn, powerful programming language.

Part of the reason for this claim is that [Python Data Model](https://docs.python.org/3/reference/datamodel.html) defines the interfaces of the building blocks (constructs) of the language itself.

Why? What? How?

## Python Data Model

- Overview
- Special Methods
  - Scalar Value: Number and Boolean
  - Collection
  - Syntax: Callable and Loop
- meta-programming
  - Attribute
  - Class

## Overview

- Motivation
- Language Constructs
- What is Python Data Model?
- Pythonic Style

### Motivation

There are three basic requirements in the design of a programming language:

- Consistent: it is easy to predict the behaviors of a construct.
- Composable: constructs can be selected and assembled in various combinations to enable desired behaviors.
- Open: developers can create new types that work in the same way as the built-in types and standard library types.

### Language Constructs

- Data
  - Atomic types and composite types (sequence, mapping, and set)
  - Built-in types and new types (Classes)
- Operations
  - built-in operators such as `+`, `-`, `>=`, list index `[]`, function call `()`, and so on.
  - built-in functions such as `len()`, `repr()`, `bool()`, etc.
  - user defined functions
- Program Control Structure: specific syntax for statements, branches and loops. For example:
  - `for` loop statement or `with` context manager statement.
  - work with user defined types
- Meta programming: write code that generate code

### What is Python Data Model?

Python *data model* is the set of APIs that defines the interfaces of the language constructs that satisfies the three basic requirements:

- consistent: it is standardized by Python language specification and PEPs.
- Composable: the APIs work well with each other.
- Open: new objects fit well with the Python language syntax.

It is defined in Python Language Reference [Data Model](https://docs.python.org/3/reference/datamodel.html).

### Pythonic Style

> "There should be one-- and preferably only one --obvious way to do it."  - The Zen of Python

Python promotes an idiomatic coding style, the so-called *Pythonic* style, that leverages Python data model and demonstrates idiomatic language features.

For example, to find an object's length, you use the built-in `len()` function, not a function like `length()`/`size()`, or a method like `my_object.len()` or `my_object.size()`.

Every Python developers should be familiar with common Python idioms. Following are two resources:

- [Python Programming/Idioms](https://en.wikibooks.org/wiki/Python_Programming/Idioms)
- [Idiomatic Python](https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/idiomatic-python.html)

### Common Python Idioms: List Comprehension and Generator Expression

As described in [Python Docs](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions), two common operations on an iterator’s output are

- performing some operation on every element
- selecting a subset of elements that meet some condition.

List comprehensions and generator expressions (short form: `listcomp` and `genexp`) are a concise notation for such operations, borrowed from the functional programming language `Haskell`.

- use `liscomp` for small data collection that can be created in one call.
- use `genexps` for large data sets or you don't need all the values at once.

```python
# list comprehension: create a list all at once
# to  create  a list of squares of numbers from 0 to 9
result1 = []
for i in range(10):
    result1.append(i * i)

# using list comprehension - a common idiom in python
result2 = [i * i for i in range(10)]
```

```python
# using a generator expression: computes the values as necessary (lazy evaluation)

weights = [0.1, 0.2, 0]
inputs = [8.5, 0.65, 1.2]
bias = 2

sum1 = 0
for weight, input in zip(weights, inputs):
    sum1 += weight * input

sum1 += bias

# using a generator expression, generate a pair each time when needed
# good for large data sets or you don't need all the values at once
wi_in_gen = (weight * input for weight, input in zip(weights, inputs))

# now all values are needed, one by one
sum2 = sum(wi_in_gen, bias)

print(sum1, sum2)  # 2.98 2.98
```

```python
import random

TEN_MILLION = 10**7
# Generator expression to create one million random numbers between 1 and 100
# just a generator expression, no numbers are generated yet
random_numbers = (random.randint(1, 100) for _ in range(TEN_MILLION))

# Display the first 10 numbers - only generate the first 10 numbers
first_ten = [next(random_numbers) for _ in range(10)]
print(first_ten)
```

## Python Data Model: Special Methods

The Python data model is a set of APIs. The APIs are defined as a set of standard *special methods*.

All special methods follow a special naming style: starting and ending with double underscores: `__*__`. They are known as `dunder` (double underscore) methods.

Developers *should not* create or use any `dunder` identifier not standardized by the language reference because they are subject to breakage without warning in future Python versions.

In a Python interpreter, built-in functions, operators, and special syntax invoke these special class methods to perform data operations.

### Build-in Functions

`len()` invokes the `__len__()` method to get the length/size of an object.

`repr()` invokes the `__repr__()` method to compute the string representation (serialized string) of an object. It is used by developer for debugging purpose.

`str()`, `format()`, and `print()` invokes `__str__()` method to compute a user friendly representation of an object. The default implementation of `object` calls `object.__repr__()`.

### Built-in Operators

`+` invokes the `__add__()` method on its left operand. If the first operand doesn't define the `__add__()` method, it invokes `__radd__()` method of the right operand. If both are not defined, it returns `NotImplemented` exception.

`==` invokes the `__eq__()` method. By default, object implements __eq__() by using `is` that checks if two references point to the same object. In most cases, this is not what you want and you should implement the `__eq__()` method.

`self[key]` invokes `self.__getitem__(self, key)` for sequence type where `key` is an integer and mapping type where `key` is any immutable value.

Method call `self(...)` invokes `self.__call__(self, ...)`. If a class defines `__call__(self, ...)` method, its instances are callable using syntax `instance(...)`.

### Special Syntax

`for` statement uses `__iter__` method to loop over items of a collection.

`with` statement uses `__enter__` and `__exit__` methods to manage object context. Classes deal with file, database, and network should use the two methods to manage resources.

### Built-in Types and New Types

Python defines a set of built-in types. Each type has a set of valid operations. New types are defined using `class` to emulate the built-in type behaviors. Following sections will give examples emulating built-in types and customizing new type creation.

- Number and Bool
- Collection
- Class and Metaclass

## Emulating Numeric Operations

Python is a high level programming language that has built-in numeric operators and functions such as `+`, `-` (unary negation or binary subtraction), `*`, `/`, `//` (floor division), `%`, `**`, `<`, `<=`, `==`, `!=`, `>`, `>=`, `abs`, `&` (bitwise And), `~` (bitwise inversion), `^` (bitwise XOR), `|` (bitwise Or), and so on.

Each of these operators or functions has one or more corresponding special methods. For example, `+` invokes either `__add__` of its left operand or `__radd__` of its second operand if the `__add__` is not defined by the left operand.

If a new type defines the corresponding methods, an instance of the type can be operands of the built-in operators and functions

### `+` and `*` Operators

As an example, the following code defines a `Value` type that works well with `+` and `*`. It also defines `__repr__` to have a better string representation of the data.

```python
class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = self.data + other.data
        return Value(out)

    def __mul__(self, other):
        out = self.data * other.data
        return Value(out)


a = Value(2.0)
b = Value(3.0)
c = Value(-2.0)

print(a + b * c)
```

### Boolean Value and Operation with Scalar Values

Any Python object can be used in a boolean context or be an operand of built-in `bool()` function. Boolean context include conditions in `if` or `while` statement, or as operands of `and`, `or`, and `not` logical operators. Every object is either `truthy` or `falsy` in a boolean context.

By default, any instance of a new type is `truthy` unless either `__bool__()` or `__len__()` method is defined in the type. In a boolean context or a call of `bool()`, the `__bool()__`  method is called. If the `__bool__()` method is not defined, Python calls `__len__()` method. If the result is 0, it is `falsy`(`False`). Otherwise, it is `truthy` (`True`).

The `Value` type defines a `__bool__()` method in the following code.

Additionally it let `Value` with scalar numbers.

```python
class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = self.data + other.data
        return Value(out)

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = self.data * other.data
        return Value(out)

    def __bool__(self):
        return bool(self.data)


a = Value(0)
b = Value(3)

print(bool(a), bool(b), (a + 1) * b)  # False True Value(data=3.0)
```

```python
# how about 2 + a,  3 * b, a - b
class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data)
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data)
        return out

    def __rmul__(self, other):  # other * self
        return self * other

    def __neg__(self):  # -self
        return self * -1

    def __sub__(self, other):  # self - other
        return self + (-other)

    def __radd__(self, other):  # other + self
        return self + other


a = Value(0)
b = Value(3)

print(bool(a), bool(b), 2 * (1 + a) - b)  # False True Value(data=6.0)
```

## Collection

Python built-in collection types include `str`, `list`, `tuple`, `range`, `set`, `dict`, and so on. They all have three special methods:

- `__len__()` to support built-in `len()` function or `bool()` function.
- `__iter__()` to support `for`, unpacking, and other iteration operations.
- `__contains__` to support `in` operator.

Except `set`, all collection types support getting a value by a key (an index or any immutable object) using syntax `obj[key]`.

- It is equivalent to `type(obj).__getitem__(obj, key)`.
- The `__getitem__` can also be used to support iteration without defining `__iter__` method.

By implementing the corresponding special methods, a new type can emulate a built-in collection type the works well in a Pythonic style.

```python
from collections import namedtuple

Item = namedtuple("Item", "name quantity")


class ShoppingList:
    def __init__(self, items):
        self.items = items
        self.names = [name for (name, _) in items]

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __contains__(self, name):
        return name in self.names
```

```python
milk = Item("Milk", 1)
banana = Item("Banana", 5)
bread = Item("Bread", 2)
my_list = ShoppingList([milk, banana, bread])

print(my_list[0])  # Item(name='Milk', quantity=1)

for item in my_list:
    print(item)  # print each item

print(f"There are {len(my_list)} items.")  # There are 3 items.

has_milk = "Milk" in my_list
has_chip = "Chip" in my_list
print(has_milk, has_chip)  # True False
```

```python
# to improve for loop
from collections import namedtuple

Item = namedtuple("Item", "name quantity")


class ShoppingList:
    def __init__(self, items):
        self.items = items
        self.names = [name for (name, _) in items]

    # __getitem__ method is for indexing
    def __getitem__(self, index):
        return self.items[index]

    # more efficient than __getitem__ for iteration
    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, name):
        return name in self.names
```

## Callable

Both functions, classes, and methods are *callable* in Python: you append a pair of parentheses after the name of a function or a class. Python allows instances of a class to be callable like functions by define a `__call__` method in the class.

It is often used to implement function-like behavior for a class instance. For example, the following class allows each instance to have a different count start and step.

```python
class Counter:
    def __init__(self, start=0):
        self._count = start

    def __call__(self):
        self._count += 1
        return self._count


counter = Counter()
print(counter())  # Output: 1
print(counter())  # Output: 2

counter = Counter(10)
print(counter())  # Output: 11
print(counter())  # Output: 12
```

## Meta-programming: Code That Generates Code

Python has a set of special methods that can be used to customize the class definition. These methods include:

- Customize instance creation
  - Instance creation
  - Attribute management
- Advanced: customize class creation
  - Class creation: `__init_subclass__`
  - Class decorator
  - `metaclass`

In meta-programming, instances and classes are objects that are created and customized at runtime.

Python tools/frameworks such as `PyTorch` and `Django` use meta-programming to make it easy to develop application. An application developer don't use them often but it is better to know the concepts.

### Why Meta Programming

- Simple: writing less code
- Powerful: expressive code

For example, in data analysis, one needs a simple way to create classes that mainly hold data. The data class should have good string representation and be able to tell their equality.

### Without `@dataclass``

The following code use type hints for better readability.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
```

### With `@dataclass`

```python
# both __repr__ and __eq__ methods are defined
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


alice = Person("Alice", 30)
bob = Person("Bob", 30)
alice2 = Person("Alice", 30)

print(alice)  # Person(name=Alice, age=30)
print(alice == bob)  # false
```

## Instance and Attributes

- Instance creation: `__new__`. You use it to customize instance creation and initialization.
- Attribute management: `__init__`, `__getattribute__`, `__getattr__`, `__setattr__`, `property` and descriptor. You use these methods to control the `.` attribute access behavior of a class and its instances.

### The `__init__(self, ...)` Method

Most classes only define the `__init__(self, ...)` method to set attributes of an instance of the class. There are some questions for this method:

- When is it called? You might know the answer: it is called when you create an instance by calling a `cls(...)` where `cls` is a class name. You almost never call this method directly.
- The `__init__(self, ...)` returns nothing, how could Python create the instance? It is not clear.
- Where does the first argument `self` come from? It is not clear.

There is more to explain about the instance creation.

### Instance Creation

There are two steps to create an instance of a class:

- `__new__()` static method creates a new instance. It is the *constructor* method. Its first argument is a class, often named as `cls`. It returns a new instance that is passed to the next initialization step.
- `__init()__` instance *initializer* method that set the attributes of an instance. Its first argument is the newly created instance, often named as `self`. It has no return value.

All classes are subclass of the `object` base class. If a class doesn't define any of the method, Python calls the default implementation defined in the `object` base class.

### `__new__()` Use Cases

You rarely need to define `__new__()`. It is often used to develop frameworks or libraries.

`__new__()` is mainly used to define subclasses of immutable types (like `int`, `str`, or `tuple`) to customize instance attributes because it is too late to change anything once the instance is created.

It is also used in a metaclass in order to customize class creation.

Following is an example that create a `Name` instance that has titled string. The first char is an uppercase one. Because `str` is immutable, you cannot change it in `__init__()` method.

```python
class Name:
    def __new__(cls, name):
        instance = super().__new__(cls)
        instance.name = name.title()
        return instance

    def __repr__(self) -> str:
        return self.name


name1 = Name("alice")
name2 = Name("BOB")

print(name1, name2)  # Alice Bob
```

### Property

A property let you use a set of methods as a normal data attribute. It is Pythonic way to implement `getter` and `setter` methods to customize the attribute behavior.

The advantage of using methods behind a data attribute are:

- Uniform access: you can use a simple data attribute or methods without change its usage.
- Getter and setter control: you can validate, transform the attribute access behaviors.
- Computed properties: a method allows to calculate and/or cache the result.

```python
import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # this is the getter method
    def radius(self):
        return self._radius

    @radius.setter  # this is the setter method
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property  # calculated read-only value
    def area(self):
        return math.pi * self._radius**2


circle = Circle(1)
radius = circle.radius
area = circle.area
print(f"Radius {radius} has an area of {area}")
# output: Radius 1 has an area of 3.141592653589793

circle.radius *= 10
radius = circle.radius
area = circle.area
print(f"Radius {radius} has an area of {area}")
# output: Radius 10 has an area of 314.1592653589793

circle.radius = -1  # ValueError: Radius cannot be negative
```

### Descriptor

Descriptors are used to customize the behavior of getting, setting, or deleting an attribute's value. Descriptors provide a general mechanism to control attribute access in Python classes.

A Python property is actually a specific implementation of the descriptor that often used to decorate class methods. It can also be used as a typical descriptor that is defined as a class attribute.

One descriptor can be used by multiple attributes.

### Descriptor Implementation

To create a descriptor, you typically define one or more of the following methods within a class:

- `__set_name__(self, owner, attribute_name)`: this method store the attribute name in each descriptor instance.
- `__get__(self, instance, owner)`: This method is called when you access the attribute's value. The parameters are descriptor instance, the instance of the object it's accessed on, and the class of that object. You should return the value you want to provide for the attribute.
- `__set__(self, instance, value)`: This method is called when you set the attribute's value. The parameters are the descriptor instance, the instance of the object it's set on, and the new value. You can implement custom logic to handle the setting of the value.
- `__delete__(self, instance)`: This method is called when you delete the attribute. It is rarely used.

```python
class PositiveNumber:

    def __set_name__(self, owner, attribute_name):
        # different attribute has different storage name
        self.storage_name = attribute_name

    def __get__(self, instance, owner):
        # this is a low level function that
        # must directly manipulate object mapping.
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        instance.__dict__[self.storage_name] = value


class Size:

    # define a class attribute with a descriptor instance
    # the attribute is actually stored/accessed in an instance of Size
    width = PositiveNumber()
    length = PositiveNumber()

    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length


desk_size = Size(2, 5)
print(desk_size.area)

desk_size.length = 10
print(desk_size.area)

desk_size.length = -1  # ValueError: Value cannot be negative
```

### Dynamic Attributes

Dynamic attributes are useful when you need to store additional data with an object, but the attribute names are not known until runtime.

All defined attributes are usually stored in the object's `__dict__` that is a dictionary.

The special method `__getattr__(self, name)` is called when the `name` attribute is not found in the current object. Therefore, it can be used to define dynamic (computed) attribute value or raise `AttributeError` if the requested name is invalid.

The `__setattr__(self, name, value)` method is called whenever an attribute is assigned a value on an instance. You can define this method in your class to control and customize the behavior of attribute assignment.

Both *property* and *descriptor* use these attribute management methods to create the read/write attributes. If possible, you should use property to define dynamic attributes because it is the simplest. Descriptor is the choice if multiple classes/attributes have the same logic. Django `models` is a descriptor.

```python
class DynamicConfig:
    def __init__(self, config_dict):
        self.config_dict = config_dict

    def __getattr__(self, name):
        if name in self.config_dict:
            return self.config_dict[name]
        else:
            raise AttributeError(f"Config attribute '{name}' not found")


# Create a dynamic config object
config = DynamicConfig({"database": "mysql", "host": "localhost", "port": 3306})

# Access dynamic attributes
print(config.database)  # Output: mysql
print(config.host)  # Output: localhost
print(config.port)  # Output: 3306

# Try accessing a non-existent attribute
try:
    print(config.username)
except AttributeError as e:
    print(e)  # Output: Config attribute 'username' not found
```

## Too Much Redundancy

Python is famous for its simplicity. But the following object-oriented programming code

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Create an __eq__ method that compares the attributes
    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age)
```

is horrible because

- each attribute is repeated THREE times
- each attributed is repeated the fourth time in `__repr__`
- each attributed is repeated the fifth time in `__eq__`
- both `__repr__` and `__eq__` have the same logic for all data classes: print and compare each attribute.

### Class Attributes Have Simple Syntax

Class is an also `object` in Python - it has class attributes that are typed ONCE.

```python
class Person:
    name: str  # better syntax using type hint
    age: int  # type hint

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
```

However

- Class attributes are shared by all its instances.
- Assigning the same attribute to an instance creates a new instance attribute

```python
# all instances share the same class attributes
alice = Person()
bob = Person()
Person.name = "Alice"
Person.age = 30
bob.name = "Bob"  # it creates a new instance attribute

print(alice, bob)  # Person(name=Alice, age=30) Person(name=Bob, age=30)
```

## The Solution: Creating Instance Attributes from the Class Attributes

Python provides three approaches to customize class/instance creation:

- allow a base class to customize its subclass behaviors.
- class decorator: it takes a class as an argument and returns a - decorated class with desired behavior.
- metaclass: define the behavior and structure of other classes.

### Solution 1: Base Class

The special method `_init_subclass__` is defined in a base class to customize the creation of its subclasses.

However, it is not recommended because inheritance a strong relationship - the chid class inherits everything from its parent class.

```python
class DataClassBase:

    def __init_subclass__(cls) -> None:
        attributes = [attr for attr in cls.__annotations__]

        def _init(self, *args, **kwargs):
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
            for attr, value in kwargs.items():
                setattr(self, attr, value)

        def _repr(self):
            attrs = ", ".join(f"{attr}={getattr(self, attr)}" for attr in attributes)
            return f"{cls.__name__}({attrs})"

        def _eq(self, value: object) -> bool:
            if not isinstance(value, self.__class__):
                return False
            return self.__dict__ == value.__dict__

        setattr(cls, "__init__", _init)
        setattr(cls, "__repr__", _repr)
        setattr(cls, "__eq__", _eq)
```

```python
class Person(DataClassBase):
    name: str
    age: int


class Point(DataClassBase):
    x: float
    y: float


alice = Person("Alice", 30)
bob = Person("Bob", 25)
print(alice, bob, alice == bob)

p1 = Point(1.0, 2.0)
p2 = Point(30.0, 50.0)
```

### Solution 2: Class Decorator

A class decorator takes a class as an argument and returns a new class to replace the decorated class. Because it can be applied to any class, it is more flexible and more complex than the base class approach. `@dataclass` is a class decorator defined in standard library. It customizes class attributes such as instance attributes, `__init__()`, `__repr__()`, `__eq__()`, and so on.

For the case of the `Vector` class, the class decorator logic is similar to the `VectorBase`.

```python
def MyDataClass(cls):

    attributes = [attr for attr in cls.__annotations__]

    def _init(self, *args, **kwargs):
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def _repr(self):
        attrs = ", ".join(f"{attr}={getattr(self, attr)}" for attr in attributes)
        return f"{cls.__name__}({attrs})"

    def _eq(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return False
        return self.__dict__ == value.__dict__

    setattr(cls, "__init__", _init)
    setattr(cls, "__repr__", _repr)
    setattr(cls, "__eq__", _eq)

    return cls
```

```python
@MyDataClass
class Person:
    name: str
    age: int


@MyDataClass
class Point:
    x: float
    y: float


alice = Person("Alice", 30)
bob = Person("Bob", 25)
print(alice, bob, alice == bob)

p1 = Point(1.0, 2.0)
p2 = Point(30.0, 50.0)
print(p1, p2, p1 == p2)
```

### Solution 3: Metaclass

Metaclass is the most advanced and most capable approach to customize class creation. However, it is the most complex one that should be avoided if other approaches work for you. If you are not sure whether you need it, you don't.

A metaclass is a class whose instances are classes -- a class' class, thus the name metaclass. It is essentially a class factory.

A meta class is used in the `metaclass` argument `class MyClass(metaclass=MyMetaClass): ...`

### `__new__()` and `__init__()`

When Python sees a class definition like `class MyClass(metaclass=MyMetaClass): ...`, it first calls `MyMetaClass.__new__()` to create a new class. Then it calls `MyMetaClass.__init__()` to set the new class attributes.

The `MyMetaClass.__init__()` method has the following arguments:

- `cls`: the new class created by the `__new__()` method.
- `name`: the name of the new class.
- `bases`: a tuple consists of base classes of the new class.
- `attributes`: a mapping represents the attributes of the new class.

For the simple purpose of reducing boilerplate code of the `Person` class, the logic is similar to other examples. Again, it is for demo purpose, you hardly need to use it in your application development or data analysis career.

```python
class DataClassMeta(type):
    def __init__(cls, name, bases, dct):
        fields = cls.__annotations__

        def __init__(self, *args, **kwargs):
            for field_name in fields:
                if field_name in kwargs:
                    setattr(self, field_name, kwargs[field_name])
                else:
                    if args:
                        setattr(self, field_name, args[0])
                        args = args[1:]

        def __repr__(self):
            field_values = ", ".join(
                f"{field_name}={repr(getattr(self, field_name))}"
                for field_name in fields
            )
            return f"{name}({field_values})"

        def __eq__(self, other):
            if not isinstance(other, cls):
                return False
            return all(
                getattr(self, field_name) == getattr(other, field_name)
                for field_name in fields
            )

        # Attach the __init__, __repr__, and __eq__ methods to the new class
        setattr(cls, "__init__", __init__)
        setattr(cls, "__repr__", __repr__)
        setattr(cls, "__eq__", __eq__)
```

```python
class Person(metaclass=DataClassMeta):
    name: str
    age: int


class Point(metaclass=DataClassMeta):
    x: float
    y: float


alice = Person("Alice", 30)
bob = Person("Bob", 25)
print(alice, bob, alice == bob)

p1 = Point(1.0, 2.0)
p2 = Point(30.0, 50.0)
print(p1, p2, p1 == p2)
```

## Summary

Python languages constructs are consistent, composable and open. You can define new data types that work seamlessly with

- built-in operators such as `+`, `-`, `>=`, list index `[]`, function call `()`, and so on.
- built-in functions such as `len()`, `repr()`, `bool()`, etc.
- specific syntax such as `for` loop statement and `with` context manager statement.

You can customize new types using meta-programming that make your code simple and powerful.

- For attributes: `@property`, descriptor, dynamic attributes
- For class: Base class, class decorator, metaclass.
