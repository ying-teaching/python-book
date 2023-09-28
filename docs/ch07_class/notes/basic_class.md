# Basic Class

- Introduction
- Define a Class
- Instances
- Inheritance
- Cautious About OOP

## 1 Introduction

Every Python data is an object. Except literal values of built-in types, all objects are created from classes. In object-oriented programming (OOP), these objects are called _instances_. A class, working as a template, defines the attributes and methods that its instances can have. A class is the type of its instances.

### 1.1 Why Class and OOP?

There are many reasons for class and the object-oriented programming paradigm. Some common reasons for Python OOP are:

- People use the concepts of class (type) and instance in real life.
- OOP brings the benefits of inheritance, encapsulation, and polymorphism.
- In Python, class provides a unified method to allows developers to create new data types that organize data and functions in a flexible way.

### 1.2 Inheritance

Classes have the parent-child relationship. A __subclass__ can inherits from one more __superclasses__. A superclass can be inherited by many subclasses.

This is called implementation inheritance because a subclass inherits all attributes and methods defined in its superclass code. A subclass can choose to override the inherited attributes and methods.

Theoretically, inheritance reduces redundant code in its subclasses.

Practically, inheritance, especially deep class hierarchy, creates strong coupling among classes. When there is a change, it is hard to change the involved classes.

### 1.3 Encapsulation

The data (the attributes) and functions (the methods) are encapsulated inside a class. You only use methods and attributes, together called interfaces, to access instances. 

The implementation of attributes and methods could be changed without affecting its use if the class interface doesn't change.

Encapsulation is a desired objective. In practice, it is hard to define a flexible interface that works in different contents. 

### 1.4 Polymorphism

An operation can work on different types.

Polymorphism provides simplicity for both coding and conceptual understanding.

For example:

- the built-in `+` works with two numbers or two strings. Both `3 + 5` and `"Good" + " day"` make sense.
- the built-in `len` function can work with a string, a list, or ideally any collection data types. It is easy that you can use `len('abc')` and `len([10, 20, 30])`.

### 1.5 Beyond OOP

In addition to OOP, classes are used to define new data types, primarily for three purposes:

- composite data that consists of a collection of attributes. It is often called __data classes__. The purpose is to make it easy to use the composite data and its parts.
- stateful objects. Some object operations are stateful, i.e., each method call may return different results because the internal states may change in a method call. A user interface is a typical stateful object. People avoid stateful objects in multi-thread computation because it may introduce subtle concurrent bugs.
- combination of data and relevant operations. For example, a complex number and common complex number operations are defined in a `complex` class. Usually the class data is immutable to distinguish it from a stateful object.

## 2 Define a Class

You use the `class` statement to define a class. Following is an example:


```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
```

### 2.1 Explanation

The following is line-by-line explanation of the code.

- `class Rectangle:`: defines a class named `Rectangle`.
-  `def __init__(self, length, width):`: the `__init__` is a special initialization method, also called a `constructor` method, it is used to create an instance of the class. The first parameter of all class methods should be `self`. It means the object being created. After the `self`, you can have zero, one or more parameters used to create an object for the class. Here we have two parameters.
- `self.length = length`: this line create an attribute called `length` because the syntax of `self.length`.
- `self.width = width`: this line create an attribute called `width` because the syntax of `self.width`.
- `def area(self):`: this line defines a method called `area`. The first parameter must be `self` and it doesn't take other parameter. 
- `return self.length * self.width`: the method body of `area` method. Inside the class methods, use `self.attribute_name` to refer the object's attribute.

## 3 Instances

You use the class name and the parameters specified in `__init__` method to create an object. To call an object method or access an attribute, use the dot notations explained as the following:

- `rect = Rectangle(3, 5)`: create an instance of `Rectangle` with specified length and width. `rect` points to the newly created object.
- `area = rect.area()`: The dot notation `rect.area()` is used to call a method of an object.
- `print(f'Length: {rect.length}, width: {rect.width}, area: {area}')`: print the result. Use not notation `rect.length` and `rect.width` to access object's properties.


```python
rectangle = Rectangle(3, 5)
area = rectangle.area()
print(f'Length: {rectangle.length}, width: {rectangle.width}, area: {area}')
```


### 3.1 Change Attribute

You can use the attribute to change the object by putting the attribute in the left hand side of an assignment. For example:



```python
rectangle.width = 7
area = rectangle.area()
print(f'Length: {rectangle.length}, width: {rectangle.width}, area: {area}')
```

### 3.2 OOP Benefits

- Encapsulation: the data (the attributes) and functions (the methods) are encapsulated inside a class. You only use methods (`rectangle.area()`) and attributes ()`rectangle.length` and `rectangle.width`), together called interfaces, to access data. The detail implementation could be changed without affecting its interfaces.
- Polymorphism: a function can work on different types. In the following example, the `print_area()` function can use any object that has an `area()` method. code using the class and its objects.



```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2 

def print_area(shape):
    print(shape.area())

circle = Circle(10)
rectangle = Rectangle(2, 5)

print_area(circle)
print_area(rectangle)

```

## 4 Inheritance

When multiple classes share some common attributes or methods, you can define a base class or a parent class and put common attributes/methods in it. When another class inherits the base class, the subclass/child class will have all the properties/methods defined in its parent class. For example, assume that both `Rectangle` and `Circle` have a `color` attribute , you can define a base class `Shape`. 


```python
import math

class Shape:
    def __init__(self, color):
        self.color = color

    # suppose we also have many methods/attributes
    # ....
    def do_something(self):
        print(f'a {self.color} task, hundred lines of code')

class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)   # you must call this as the first 
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

class Rectangle(Shape):
    # a special method used to create an instance of this class
    # this method initialize instance attributes
    def __init__(self, color, length, width):
        Shape.__init__(self, color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# an instance/object of the Rectangle class
rect = Rectangle('red', 5, 3)
circle = Circle('blue', 10)

rect.do_something()
circle.do_something()

```

## 5 Cautious About OOP

OO was popular because GUI applications were popular. These days, as computers have multiple cores and more code are developed for backend data processing, OO shows some disadvantages:

- combine data and function in a class is error prone because instances can be changed and shared by multiple threads. Like global data, it is dangerous. Immutable data are preferred this days. 
- inheritance, especially multiple inheritance, is confusing and not used widely in data processing.

It is nice to know the basic terms because OO had been popular for more than two decades and there are many legacy code. New applications, especially non-GUI applications, use more and more immutable data and functions (not object methods).

Using functions to process immutable data, so-called functional programming, is the current trend.
