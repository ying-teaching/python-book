# Python Data Model

> Coding like poetry should be short and concise. ―Santosh Kalwar

- Overview
- Special Methods
- Number and Boolean Value
- Collection
- Callable
- Metaprogramming
  - Instance and Attribute
  - Class

## Overview

- Motivation
- Language Constructs
- What is Python Data Model?
- Pythonic Style

### Motivation

There are three basic requirements in design of data operations:

- Consistent: it is easy to predict the behaviors of a new construct instance.
- Composable: constructs can be selected and assembled in various combinations to enable desired behaviors.
- Open: developers can create new types that work in the same way as the built-in types and standard library types.

### Language Constructs

Python language constructs can be classified into four categories:

- built-in operators such as `+`, `-`, `>=`, list index `[]`, function call `()`, and so on.
- built-in functions such as `len()`, `repr()`, `bool()`, etc.
- specific syntax such as `for` loop statement and `with` context manager statement.
- built-in types and new type definitions (`class`).

### What is Python Data Model?

Python _data model_ is the set of APIs that defines the interfaces of language constructs that satisfies the three basic requirements:

- consistent: it is standardized by Python language specification and PEPs.
- Composable: the APIs work well with each other.
- Open: new objects fit well with the Python language syntax.

It is defined in Python Language Reference [Data Model](https://docs.python.org/3/reference/datamodel.html).

### Pythonic Style

> "There should be one-- and preferably only one --obvious way to do it." - The Zen of Python

Python promotes an idiomatic coding style, the so-called _Pythonic_ style, that leverages Python data model and demonstrates idiomatic language features.

For example, to find an object's length, you use the built-in `len()` function, not a function like `length()`/`size()`, or a method like `my_object.len()` or `my_object.size()`.

Every Python developers should be familiar with common Python idioms. Following are two resources:

- [Python Programming/Idioms](https://en.wikibooks.org/wiki/Python_Programming/Idioms)
- [Idiomatic Python](https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/idiomatic-python.html)

## Special Methods

The Python data model is a set of APIs. The APIs are defined as a set of standard _special methods_.

All special methods follow a special naming style: starting and ending with double underscores: `__*__`. They are known as _dunder_ (double underscore) methods.

Developers _should not_ create or use any dunder identifier not standardized by the language reference because they are subject to breakage without warning in future Python versions.

In a Python interpreter, built-in functions, operators, and special syntax invoke these special class methods to perform data operations.

### Build-in Functions

`len()` invokes the `__len__()` method to get the length/size of an object.

`repr()` invokes the `__repr()` method to compute the string representation (serialized string) of an object. It is used by developer for debugging purpose.

`str()`, `format()`, and `print()` invokes `__str__()` method to compute a user friendly representation of an object. The default implementation of `object` calls `object.__repr__()`.

### Built-in Operators

`+` invokes the `__add__()` method on its left operand. If the first operand doesn't define the `__add__()` method, it invokes `__radd__()` method of the right operand. If both are not defined, it returns `NotImplemented` exception.

`==` invokes the `__eq__()` method. By default, object implements **eq**() by using `is` that checks if two references point to the same object. In most cases, this is not what you want and you should implement the `__eq__()` method.

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

As an example, the following code defines a new `Vector` type that works well with `+` and
`*`. It also defines `__repr__` to have a better string representation of the data.

```python
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # scalar multiplication
    def __mul__(self, number):
        x = self.x * number
        y = self.y * number
        return Vector(x, y)

    # a string representation
    # the x!r conversion flag means `repr(x)`
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"


point_1 = Vector(2, 4)
point_2 = Vector(3, 5)
point_3 = point_1 + point_2
point_4 = point_3 * 10

print(point_3, point_4) # Vector(5, 9) Vector(50, 90)
```

### Boolean Value

Any Python object can be used in a boolean context or be an operand of built-in `bool()` function. Boolean context include conditions in `if` or `while` statement, or as operands of `and`, `or`, and `not` logical operators. Every object is either _truthy_ or _falsy_ in a boolean context.

By default, any instance of a new type is truthy unless either `__bool__()` or `__len__()` method is defined in the type. In a boolean context or a call of `bool()`, the `__bool()__` method is called. If the `__bool__()` method is not defined, Python calls `__len__()` method. If the result is 0, it is falsy or `False`. Otherwise, it is truthy or `True`.

The `Vector` type has an additional `__bool__()` method in the following code:

```python
class Vector:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)

    # scalar multiplication
    def __mul__(self, number):
        x = self._x * number
        y = self._y * number
        return Vector(x, y)

    # a string representation
    # the x!r conversion flag means `repr(x)`
    def __repr__(self):
        return f"Vector({self._x!r}, {self._y!r})"

    def __bool__(self):
        return bool(self._x) or bool(self._y)


point_1 = Vector()
point_2 = Vector(3, 5)

print(bool(point_1), bool(point_2)) # False True
```

## Collection

Python built-in collection types include `str`, `list`, `tuple`, `range`, `set`, `dict`, and so on. They all have three special methods:

- `__len__()` to support built-in `len()` function or `bool()` function.
- `__iter__()` to support `for`, unpacking, and other iteration operations.
- `__contains__` to support `in` operator.

Except `set`, all collection types support getting a value by a key (an index or any immutable object) using syntax `obj[key]`. It is equivalent to `type(obj).__getitem__(obj, key)`. The `__getitem__` can also be used to support iteration without defining `__iter__` method.

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


milk = Item("Milk", 1)
banana = Item("Banana", 5)
bread = Item("Bread", 2)
my_list = ShoppingList([milk, banana, bread])

for item in my_list:
    print(item) # print each item

print(f"There are {len(my_list)} items.") # There are 3 items.

has_milk = "Milk" in my_list
has_chip = "Chip" in my_list
print(has_milk, has_chip)  # True False
```

## Callable

Both functions, classes, and methods are _callable_ in Python: you append a pair of parentheses after the name of a function or a class. Python allows instances of a class to be callable like functions by define a `__call__` method in the class.

It is often used to implement function-like behavior for a class instance. For example, the following class allows each instance to have a different count start and step.

```python
class Counter:
    def __init__(self, start = 0, step = 1):
        self._count = start
        self._step = step

    def __call__(self):
        self._count += self._step
        return self._count

counter = Counter()
print(counter())  # Output: 1
print(counter())  # Output: 2

counter = Counter(10, 7)
print(counter())  # Output: 17
print(counter())  # Output: 24

```

## Metaprogramming

Python has a set of special methods that can be used to customize the class definition. These methods include:

- Instance creation and destruction
- Attribute management
- Class creation: `__init_subclass__`, class decorator, metaclass, and so on.

These are advanced topics that customize the class behavior - so-called _metaprogramming_. In metaprogramming, classes are objects that are created and customized at runtime.

Python tools/frameworks such as `@dataclass` and Django uses metaprogramming to make it easy to develop application. An application developer rarely use them directly but it is better to know the concepts.

## Instance and Attributes

- Instance creation and destruction: `__new__`, and `__del__`. You use these methods to customize instance creation, initialization and deletion.
- Attribute management: `__init__`, `__getattribute__`, `__getattr__`, `__setattr__`, `property` and descriptor. You use these methods to control the `.` attribute access behavior of a class and its instances.

### The `__init__(self, ...)` Method

Most classes define the `__init(self, ...)__` method to set attributes of an instance of the class. There are some questions for this method:

- When is it called? You might know the answer: it is called when you create an instance by calling a `cls(...)` where `cls` is a class name. You almost never call this method directly.
- The `__init__(self, ...)__` returns nothing, how could Python create the instance? It is not clear.
- Where does the first argument `self` come from? It is not clear.

There is more to explain about the instance creation.

### Instance Creation

There are two steps to create an instance of a class:

- `__new__()` static method creates a new instance. It is the _constructor_ method. Its first argument is a class, often named as `cls`. It returns a new instance that is passed to the next initialization step.
- `__init()__` instance _initializer_ method that set the attributes of an instance. Its first argument is the newly created instance, often named as `self`. It has no return value.

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

print(name1, name2) # Alice Bob
```

### Property

A property let you use a set of methods as a normal data attribute. It is Pythonic way to implement _getter_ and _setter_ methods to customize the attribute behavior.

The advantage of using methods behind a data attribute are:

- Uniform access: you can use a simple data attribute or methods without change its usage.
- Getter and setter control: you can validate, transform the attribute access behaviors.
- Computed properties: a method allows to calculate and/or cache the result.

```python
import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # this is the getter method
    @property
    def radius(self):
        return self._radius

    # this is the setter method
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # calculated value
    @property
    def area(self):
        return math.pi * self._radius ** 2


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
        # this is low level function that
        # must directly manipulate object mapping.
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        instance.__dict__[self.storage_name] = value

class Size:

    # define a class attribute with a descriptor instance
    # the attribute is actually stored/accessed in
    # an instance of Size
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

desk_size.length = - 1 # ValueError: Value cannot be negative
```

### Dynamic Attributes

The `__getattribute__(self, name)` and `__getattr__(self, name)` are called when the `name` attribute is not found in the current object. Therefore, they are used to define dynamic (computed) attribute value or raise `AttributeError` if the requested name is invalid.

The `__setattr__(self, name, value)` method is called whenever an attribute is assigned a value on an instance. You can define this method in your class to control and customize the behavior of attribute assignment.

Both _property_ and _descriptor_ use these attribute management methods to create the read/write attributes. If possible, you should use property to define dynamic attributes because it is the simplest. Descriptor is the choice if multiple classes/attributes have the same logic. Django `models` is a descriptor.

The attribute management special methods are rarely needed in applications.

## Class Creation

Python provides several approaches to customize class creation in frameworks or libraries.

- `**init_subclass**``: allow a base class to customize its subclass behaviors.
- class decorator: it takes a class as an argument and returns a - decorated class with desired behavior.
- metaclass: define the behavior and structure of other classes.

### A Redundancy Problem

Python is famous for its simplicity. But the following object-oriented programming code is not simple because you need to type each attribute name three times.

```python
class Vector:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
```

Python supports class attributes that each attribute name is typed once like the following.

```python
class Vector:
    x = 0
    y = 0
```

However, class attributes are shared by all instances. Is it possible to use the simple class attribute syntax to create instance attribute? Python metaprogramming provides multiple approaches.

### `_init_subclass__`

This special method is defined in a base class to customize the creation of its subclasses. There are two basic tasks to create instance attributes from the subclass' class attributes:

- in `__init_subclass__`, copy each subclass' class attribute as an instance attribute.
- in `__init__`, reset the instance attributes if a caller provides vector attribute values.

```python
class VectorBase:
    def __init_subclass__(cls):
        super().__init_subclass__()
        for name, value in cls.__dict__.items():
            if not name.startswith("__"):
                setattr(cls, name, value)

    def __init__(self, *args):
        if args:
            self.x, self.y = args

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

class Vector(VectorBase):
    x = 0
    y = 0

v0 = Vector()
v1 = Vector(2, 3)
v2 = Vector(10, 20)
v0.x = 7
v1.y = 17

print(v0, v1, v2) # Vector(7, 0) Vector(2, 17) Vector(10, 20)
```

### Class Decorator

Similar to function decorator, a class decorator takes a class as an argument and returns a new class to replace the decorated class. Because it can be applied to any class, it is more flexible and more complex than the `_init_subclass__()` approach. `@dataclass` is a class decorator defined in standard library. It customizes class attributes such as instance attributes, `__init__()`, `__repr__()`, `__eq__()`, and so on.

For the case of the `Vector` class, the class decorator logic is similar to the `VectorBase`.

```python
def vector_class(cls):
    for name, value in cls.__dict__.items():
        if not name.startswith("__"):
            setattr(cls, name, value)

    def _init(self, *args):
        if args:
            self.x, self.y = args

    setattr(cls, "__init__", _init)

    return cls

@vector_class
class Vector(VectorBase):
    x = 0
    y = 0

v0 = Vector()
v1 = Vector(2, 3)
v2 = Vector(10, 20)
v0.x = 7
v1.y = 17

print(v0, v1, v2) # Vector(7, 0) Vector(2, 17) Vector(10, 20)
```

### Metaclass

Metaclass is the most advanced and most capable approach to customize class creation. However, it is the most complex one that should be avoided if other approaches work for you. It you are not sure whether you need it, you don't.

A metaclass is a class whose instances are classes -- a class' class, thus the name metaclass. It is essentially a class factory.

By default, a class is an instance of `type` - the default built-in metaclass. You can define new metaclass and set it as a metaclass for a class using the `metaclass` argument like `class MyClass(BaseClass, metaclass=MyMetaClass): ...`

### `__new__()` and `__init__()`

When Python sees a class definition like `class MyClass(BaseClass, metaclass=MyMetaClass): ...`, it calls `MyMetaClass.__new__()` to create a new class.

An interesting fact is that every metaclass is a subclass of `type`. After customization, a metaclass calls `super().__new__(...)` to let `type` create the new class.

Then it calls `MyMetaClass.__init__()` to set the new class attributes. This method has the following arguments:

- `cls`: the new class created by the `__new__()` method.
- `name`: the name of the new class.
- `bases`: a tuple consists of base classes of the new class.
- `attributes`: a mapping represents the attributes of the new class.

For the simple purpose of reducing boilerplate code of the `Vector` class, the logic is similar to other examples. Again, it is for demo purpose, you probably never need to use it in your application development or data analysis career.

```python
class VectorMeta(type):
    def __init__(cls, name, bases, attributes):
        super().__init__(name, bases, attributes)
        for name, value in attributes.items():
            if not name.startswith("__"):
                setattr(cls, name, value)

        def _init(self, *args):
            if args:
                self.x, self.y = args

        def _repr(self) -> str:
            return f"Vector({self.x}, {self.y})"

        setattr(cls, "__init__", _init)
        setattr(cls, "__repr__", _repr)


class Vector(metaclass=VectorMeta):
    x = 0
    y = 0

v0 = Vector()
v1 = Vector(2, 3)
v2 = Vector(10, 20)
v0.x = 7
v1.y = 17

print(v0, v1, v2) # Vector(7, 0) Vector(2, 17) Vector(10, 20)
```

## Summary

Python languages constructs are consistent, composable and open. You can define new data types that work seamlessly with

- built-in operators such as `+`, `-`, `>=`, list index `[]`, function call `()`, and so on.
- built-in functions such as `len()`, `repr()`, `bool()`, etc.
- specific syntax such as `for` loop statement and `with` context manager statement.

Additionally, you can even customize the class creation at runtime using metaprogramming that make your code simple and powerful.
