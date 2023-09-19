# Variables

> Reference and Mutability

- Object
- Type
- Value
- Variable
- Tuple

## Object Definition

In [Python Reference Document](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types):

> All data in a Python program is represented by **objects** or by **relations between objects**.
> Every object has an **identity**, a **type** and a **value**.

### Object in English

Every Python data is represented as an object or a relation of objects. A number, a string, a list, a file,,, they are objects.

Objects may have relations such as a student (an object) has two attributes: a name (an object) and birthday (an object).

### Mutability

An object has an identity, a type and a value.

Its identity and type never change.

An object’s value is

- _mutable_: if the value can change.
- _immutable_: if the value is unchangeable.

### Identity Operations

The `id()` function returns an object’s identity. For example:

```python
# the return values change for different runs
id(3) # returns a memory address 4358499512
id("hello") # returns a memory address 4340502768
```

The `is` or `is not` operator compares the identity of two objects: `True` if they have the same identity, `False` if not.

```python
# each value is a different object with a unique id
id(3) is not id("hello") # True
id(3) is not id(3) # True
id("hello") is not id("hello") # True
```

## Type

An object’s type determines the operations/functions that you can apply on an object. For example:

- an integer type supports `/`, the division, but a string type doesn’t.
- A string type supports `len()`, the length operation on an object, but an integer type doesn’t.

Use `type()` built-in function to get the type of an object.

```python
type(3) # returns <class 'int'>
type(3.5) #returns <class 'float'>
type("a") #returns <class 'str'>
type("hello") #returns <class 'str'>
type([1, 3, 5]) #returns <class 'list'>
type(True) # returns bool
```

### Same Type

In Python, everything is an object, including an object’s type.

Use `is` or `is not` to find if two types are the same.

All following comparisons return `True`:

```python
type(3) is type(7) # True: the same int type
type(3.5) is not type(7) # True: int is not float
type("h") is type("hello") # True: the same string type
type(3) is not type("a") # True: int is not string
```

### Type Defines Operations

Again, an object’s type defines the set of valid operations one can put on the object’s value.

For example, for a `string`, you can perform the following operations that may not be valid for other types such as `int` or `bool`:

- get its length or uppercase/lowercase
- find if a string is a substring of another string
- concatenate multiple strings

## Value

All operations/functions work on values. Many people use term “value” or “data” to mean the object behind it.

Nonetheless, it is important to know that _mutability_ is about an object’s value. An object’s type and id never change.

### Mutability Examples

All integers and strings are immutable, i.e., their values never change once created.

Lists are mutable data type. You can add/remove/change list elements. For example, `[1, 2, 3].pop()` removes and returns the last element, i.e., `3`, the object value changes to `[1, 2]`.

- You need a reference/variable(introduced later) to the object to see the changes.

### Mutability is Important

An object’s mutability is determined by its type. Mutability affects many operation behaviors.

All integers and strings are immutable; therefore all change operations create _new_ objects. The operation `"hello".upper()` operation creates a new string `'HELLO’` without changing the original `"hello"`.

List is mutable. Some operations make _in-place_ change of the value of a list object. The operation `[1, 2, 3].pop()` remove the last element on the same object, i.e., its value changes.

- You need a reference (a variable) to the object and see the mutability effect.

### Data, Object, and Value

In most contexts, the three are used interchangeably in programming. Conceptually, the data type concept is important to determine valid operations while the value concept is important for mutability.

Formally,

- Data: everything processed by a Python program.
- Object: abstraction of data that has an identity, a type and a value. Identity and type are meta-data of the object.
- Value: the ”real data” used in computation. The object type determines its mutability.

## Variable

A Python variable is a _symbolic name_ that is a _reference_ to an object.

Technically:

- A variable is a name of a memory address.
- The memory content is the memory address of an object.

Conceptually:

- A variable is a named reference, i.e., a label, to an object.
- Literally, variable can refer to different objects at different time, thus it varies.

## A Variable Is Not

A variable is not a _container_ / _box_ / _location_ that you can put a an object into it.

It might be the cases for other programming languages such as C/C++.

In Python, a variable is a symbolic name/label that you can bind to different objects.

### Assignment Statement

You create a variable using an assignment statement `name = something`:

- `name`: the Left hand side (LHS) of the assignment. It must be a variable name.
- `something`: the right hand side (RHS) of the assignment. It can be any object or operations of objects.

You must create a variable before use it. Her the `use` means anywhere except in LHS. You often use a variable in an operation or in RHS of an assignment.

```python
PI = 3.1415926
cat_names = ["lemon", "kiwi", "orange"]

number_input = input("Please input a number: ")
# use after creation
number = int(number_input)

# Assign one value 0 to multiple variables
x = y = z = 0

# wrong - the LHS must be a variable
10 = PI
```

### Why Variable?

Essentially a variable is a _named reference_ of an object.

A named reference is needed for:

- Meaningful names in a context.
- Using objects in multiple places.
- Objects created at runtime (when a program is running).

```python
# Too bad, 3.14 is a magic number
x = (10 ** 2) * 3.14

# the meaning of numbers
PI = 3.14
diameter = 10
circumference = diameter * PI

# it is a list of cat names, not fruit names
cat_names = ["lemon", "kiwi", "orange"]
```

```python
# the data could have 100 or 1,000,000 elements
cat_names = ["lemon", "kiwi", "orange"]
# change the mutable data and print it
cat_names.append("apple")
print(cat_names)
```

### Objects Created at Runtime

Create objects from user input / network / function call.

Function call inputs (parameters) are alias of its arguments

```python
# number refers to the input (argument)
def double(number):
    return number * 2

# refer to the function results
# they don’t exist before code execution
number_input = input("Please input a number: ")
number = int(number_input)

# now the variable refers/binds to a new object
# the literal meaning of a variable: a variable's referred object varies
number = double(number)
```

### Python Identifier

A Python variable is a _symbolic name_, an _identifier_ in Python.

A function name is also an identifier.

There are some rules for a valid identifier:

- Must be started with a letter or an underscore (`_`).
  - specifically, the first letter cannot be a numeric character.
- Cannot conflict with a keyword.
  - Keywords are reserved by Python standard such as `if`, `else`, `for`, etc.
- Contains no special characters such as `@`, `%`, `$`, etc.

### Name Matters

Use the most meaningful name in the context !!!

Use snake_case naming convention for multi-word name.

Use UPPERCAS_NAME for constants.

```python
# good names
scores = [27, 87, 92]
score1 = scores[0]
first_name = "Alice"
# constants use UPPERCASE names
KILOGRAM_ABBREVIATION = "kg"
ULTIMATE_ANSWER = 42
# bad names. Yes, math.pi is a bad name in today's standard
pi = 3.1415926

1st_score = scores[0] # invalid name
# names like i, j, k are meaningless
for i in scores:
    print(i)
```

### The Semantics of Assignment

The “assignment” is misleading, it actually binds/re-binds an identifier to an object.

Variable is not a container; it is a name/label/identifier/reference that refers to an object.

LHS and RHS are technical terms in programming. They specify the location of code constructs.

When a variable is on the LHS, it binds to the RHS.

When a variable is on the RHS, the referred object value is used in place of the variable.

### Bind and Alias

When the RHS is a literal value, the LHS variable is _bound_ to the value.

When the RHS is a variable, the LHS variable is _bound_ to the referred object in RHS. It creates an _alias_.

- `numbers = [2, 1, 3, 4, 7]`: binds a label to a list object
- `numbers2 = numbers`: creates an alias of the object labelled by `numbers`
- `name = "Trey`: binds a label to a string object.

![Variable Labels](../images/variable.png)
[Image source](https://www.pythonmorsels.com/pointers/)

### More Examples

You can use `is` or `is not` operator to check if two variables refer to the same objects.

```python
x = 3
y = 5
# False because they refer to different objects
print(x is y)

# True because they refer to different objects
print(x is not y)
z = x

# True because they refer to the same object
# They are aliases of 3
print(x is z)
```

```python
scores = [90, 67, 82]

# This creates an alias of mutable data
scores2 = scores

scores2[0] = 77

print(scores2) # output: [77, 67, 82]
# they refer to the same object, thus the same output
print(scores) # output: [77, 67, 82]
```

### Function Calls

Binding also happens in a function call. A function parameter is bound to the argument object. If the argument is a variable, it creates an alias to the object.

Be careful when you use mutable arguments in function calls.

```python

# changing input is usually bad
def report_scores(scores):
    scores.append(100)
    for score in scores:
        print(score)

scores = [27, 87, 92]
report_scores(scores)

# Surprise or not: it is changed to [27, 87, 92, 100]
print(scores)
```

### Type Conversion

You often need to convert an object to a different type. For example, all `input()` function outputs are strings. If you need a number, you should call `int()` or `float()` to convert it to a desired type. Similarly, you can convert a number into a string using the `str()` function.

```python
age_input = input("Please enter your age: ")

# convert to an integer for computation
age = int(age_input)
next_year_age = age + 1

# you can concatenate a string with another string
message = "Next year you will be " + str(next_year_age)
print(message)

# The above is for type conversion demo, a simpler version uses f-string
message = f"Next year you will be {next_year_age}"
print(message)
```

### Value and Variable

In programming, it is often important to distinguish an object and its references.

An object is a single piece of data that has a unique identity and a fixed type.

An object may have many references. A variable is a reference to an object.

In most computation, data, object and value are interchangeable because a valid computation only cares about the value.

In Python, an object is used in two syntactic form: a literal value or a reference. People often use values and variables to mean objects and use object in a specific context: object-orient programming.

## None

Python has a special type `NoneType` that has only a single value `None`. It means _"no value"_ or _"missing value"_. For example, if a function doesn't return a value, it has an implicit return value of `None`.

Please use `is` or `is not` to determine if a variable is `None` or not.

```python
x = 3
y = None

x is None # False
x is not None # True
y is None # True
y is not None # False
type(y) # NoneType
```

## Tuple

The `list` type is a mutable type that represents a sequence of values. Python provides a `tuple` immutable type to represent a sequence of values.

A tuple consists of a number of values separated by commas. Like list, the values can be of different types. In practice, people like to use tuple to represent two or three values that are of different types.

You can access item using an 0-based index inside a pair of square brackets.

```python
# The values can be of different types.
my_tuple = 1, 3, "Hello"

# A tuple with a single value, the trailing comma is mandatory here
single_tuple = 7,

# An empty tuple has no value
empty_tuple = ()

# Tuple can be nested
nested_tuple = "look", my_tuple, (3.5, 4.2)

# Python represents a tuple in a parenthesis
print(my_tuple) # output: (1, 3, 'Hello')
print(my_tuple[2]) # output: 'Hello'
print (single_tuple) # output (7,)
print(empty_tuple) # output ()
print(nested_tuple) # output: ('look', (1, 3, 'Hello'), (3.5, 4.2))
print(nested_tuple[1]) # output: (1, 3, 'Hello')

```

### Tuple Operations

Because a tuple is immutable, it only supports read-only operations.

```python
my_tuple = 1, 3, "Hello"
single_tuple = 7,

# length
print(len(my_tuple)) # output: 3

# adding two tuple generates a new one
combined_tuple = my_tuple + single_tuple
print(combined_tuple) # output: (1, 3, 'Hello', 7)

# unpack and create multiple variables
number1, number2, message = my_tuple
print(number1, message) # output: 1, 'Hello'

# use _ to ignore an element
_, _, message = my_tuple
print(message) # output: 'Hello'
```

### Tuple Use Cases

It is a rule of thumb that if is possible, please use an immutable value. You have the peace of mind that the value can be used in multiple places and stays the same.

In so-called functional programming, a best practice is that a function only has immutable values as its arguments, it is easier to use and easier to reason about than a function that has mutable values.

Tuple is often used as function return value to represent multiple return results.

```python
scores = 90, 67, 82

def get_max_min(numbers):
    return max(numbers), min(numbers)

print(get_max_min(scores)) # output (90, 67)
```

## Summary

Python is a high-level PL that hides the memory details.

However, these concepts are important to write correct Python Code:

- An object's type and identity are fixed once it is created.
- An object's type determines the operations and mutability of the object's value.
- Variables are references/binds to objects.
- Variables may refer to different objects in different time.
- Assignment or function parameter create aliases that refer to the same corresponding RHS/argument object.
