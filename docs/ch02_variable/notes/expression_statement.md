# Expression and Statement

- Expression
- Operator
- Statement

## Expression

An expression is a _code construct_ that is evaluated to a value. A code construct is a piece of code. Following are some common expressions:

- An object or a declared variable, such as: `3`, `Hi`, `x`, `[1, 2, 3]`.
- A computation using operators, such as `3 + 5`, `x < y < z`.
- A function call, such as `len("hello")`, `math.pow(3, 2)`.
- Functions defined inside types are called methods. A method call is an expression. For example: `"hello".upper()`, `[1, 2, 3].pop()`.

### Evaluation

Evaluation refers to the process that Python interpreter generates the final object of an expression.

Expressions have a common characteristic: the evaluation of the code construct generates a _single object_.

An object may have a single value such as `3` or multiple values like a list or a tuple.

An expression may have nested expression. For example, a list or a tuple may have other tuple or list or dictionary as its element. There is no limit on the nested levels.

Python evaluates expressions from left to right.

### Expression Examples

- `3` is an literal expression, evaluated to `3`
- `3 + 5` is an addition operation expression, evaluated to `8`
- `len("hello")` is a function call expression, evaluated to `5`
- `math.pow(3, 2)` is an method call expression. evaluated to `9`
- `len("hello"), math.pow(3, 2)` is an expression that has two nested evaluation, the final evaluation result is a tuple of `(5, 3)`.

There are other code constructs that are expressions. They will be introduced later.

## Operator

An operator is a _special symbols_ that perform operations on values and variables.

A high-level programming language like Python has many built-in operators that make the language simple and easy to understand. For example, very few programming languages have built-in support for chained comparison like `x < y < z` or matrix multiplication operation with `@`. Python allows both, though matrix data types are not provided by third party libraries.

The data that an on operator acts on are called _operands_. An operator may take one operand (_unary operator_), two operands (_binary operator_), or three operands (_ternary operator_).

Python has 7 types of operators.

### Types of Operators

1 Arithmetic Operators

2 Relational Operators

3 Logical (Boolean) Operators

4 Membership Operators

5 Identity Operators

6 Bitwise Operators

7 Assignment Operators

```python
# 1 Arithmetic Operators, evaluated to a number
# if there is a float number operand, the result is a float number

-5 # unary negation: -2
5 + 3.5 # Addition: 8.5
5 - 3 # Subtraction: 2
5 * 1.5 # multiplication: 7.5
5 / 2.0 # division: 2.5
5**3.5  # exponential: 279.5084971874737
5 // 3 # floor division or quotient: 1
5 % 3 # modulus or remainder: 2

# @ is a matrix multiplication operator used by 3rd party libraries
```

```python
# 2 Relational Operators, evaluated to a boolean value of True or False

3 == 5 # equal to: False
3 != 5 # not equal to: True
3 > 5 # greater than: False
3 < 5 # less than: True
3 >= 5 # greater than or equal to: False
3 <= 5 # less than or equal to: True

```

### 3 Logical Operators

Also called `Boolean` operators. there are three of them: `not`, `and`, and `or`. There are four important details for boolean operators:

- all Python objects can be `Truthy` or `Falsy`.
- `not` is a unary boolean operator, it always returns a `True` or `False`.
- The return value of `and` and `or` is determined by their operands.
- `and` and `or` operations support short circuiting.

### Truthy and Falsy

All Python objects can be `Truthy` or `Falsy`, used as `True` or `False` in places where a boolean value is required. For example, logical operation and branching code.

You can find the `Truthy` or `Falsy` value using the built-in function `bool()`. Empty values such as `0`, `None`, empty list `[]`, empty tuple `()` and empty dictionary `{}` are `Falsy`. Most values are `Truthy`.

```python
bool([]) # False
bool(3) # True
not(3) # negation operation:False
not(3 == 5) # negation operation: True
not(True) # negation operation:False
```

### `and` and `or` Logical Operation

The evaluation rules are:

- `x or y`, if `x` is `True` or `Truthy`, then `x`, else `y`
- `x and y`, if `x` is `False` or `Falsy`, then `x`, else `y`

If it is confusing, use `if/else` statement.

```python

(3 == 5) and (3 != 5) # False
(3 == 5) or (3 != 5) # True
3 or 5 # 3
3 and 5 # 5
0 and "hi" # 0
0 or "hi" # "hi"

```

### Short-circuiting

Python supports short-circuiting in `and`/`or` operations: if it can determine the result from the left part, it doesn't evaluate the later part.

```python
# short-circuiting in and/or
def demo_true():
    print("True")
    return True

def demo_false():
    print("False")
    return False

demo_true() and demo_false() # True, False
demo_true() or demo_false() # True
demo_false() and demo_true() # False
demo_false() or demo_true() # False, True
```

### 4 Membership Operator

The membership operator `in` and `not in` are used to find if a value is a member of a sequence. A sequence can be a string, a list, a tuple, or even a dictionary.

```python
5 in [1, 5, 7] # True
key = "hi"
greeting = "hello"
key in "hello" # False
key not in greeting # True
table = {key: greeting, "az": "arizona"}
key in table # True
key not in table # False
```

### 5 Identity Operator

`is` and `is not` are used to check if _two variables_ refer to the same object, i.e., if two variables are aliases of the same object. Use `==` to check if two values are equal or not. It is not recommended to use identity operator on literal values.

There are some surprises in these two concepts. In Python, small integer values (from -5 to 256, inclusive) and strings are shared by all references for performance reason. Therefore, variables with the same value refer to the same object, so-called _interning_. But it is implementation-specific.

Practically, it is safe and simple to remember that only an assignment `x = y` or a function/method call create an alias.

```python
x = 3
y = 3
x == y # True, of course
x is y # True, interning

x = 257
y = 257
x is y # False !!! no interning

x = "abc"
y = "abc"
x == y # True
x is y # True, interning

x = [1, 2, 3]
y = [1, 2, 3]
x == y # True
x is y # False !!!

z = x
z is x # True
```

### 6 Bitwise Operators

Python has one unary and several binary bit operators that act on binary data. Their operands only have `0`s or `1`s.

```python
x = 0b01 # binary data, 1
y = 0b10 # binary data, 2
~x # bitwise NOT or complement. result is -2
x & y # bitwise AND, result: 0
x | y # bitwise OR, result: 3
x ^ y # bitwise XOR, result: 3
x << 2 # left-shift, result: 4
x >> 2 # right-shift, result: 0

```

### 7 Assignment Operator

Assignment operator `=` binds a variable in LHS to the _RHS expression_. It creates the variable if it is the first time binding for the variable, otherwise, it re-binds it to a different object.

The `=` assignment operation is _not an expression_ because it binds a variable to an object, but the operation generates no value, i.e., you cannot use an assignment in a place that requires a value. It is a syntax error to write code like `(x = 3) = 5` or `if (x = 3)`.

### Augmented Assignment

It is common to use a variable in an arithmetic or bitwise operation and assign the result back to the variable. Augmented assignment makes it simple to write those operations. It works for all binary arithmetic or bitwise operators. The LHS variable is used as the first operand of the operator.

```python
x = 5
x = x + 3
x = x << 2

# Augmented assignment
x += 3
x <<= 2
```

### The Walrus Operator

Python 3.8 (released in 2019) brings a walrus `:=` operator that work as an assignment expression. It performs two tasks: assign the RHS expression value to the LHS variable and use the value as its expression value.

It combines two tasks into one operation. It makes code simpler in some cases.

```python
# Before Python 3.8
name = input("Please type your name: ")
if name:
    print(name)
else:
    print("name is empty")

# Since Python 3.8
if (name := input("Please type your name: ")):
    print(name)
else:
    print("name is empty")
```

### Operator Precedence

Operators have different precedences when they are used together in a single expression. For example, the expression `3 + 5 * 4` evaluates `5 * 4` before add them. Thus the result is `23`, not `32`.

The [Python document](https://docs.python.org/3/reference/expressions.html#evaluation-order) gives a list of operator precedences. You don't need to remember it - you even don't need to read it. The best practices are:

- break long expression into short expressions with only one or two operators
- use parenthesis to make the precedence explicit.

Using the best practices, `3 + 5 * 4` should be written as `3 + (5 * 4)`.

### Conditional Expression

Python provides a conditional expression syntax to make it easy to choose a value from two conditions.

For example, you want to set a message to `odd` or `even` based on oddness of a number. Without conditional expression, it needs a four-line statements. With conditional expression, it is one line.

```python
number = int(input('Pease type an integer: '))
if number % 2:
    message = "odd"
else:
    message = "even"

print(message)

# conditional expression
message = "odd" if number % 2 else "even"
print(message)
```

## Statement

A Python program consists of instructions to be executed by the Python interpreter. Those instructions are called statements.

All expressions are executed by the Python interpreter and generate values. Expressions are statements. But a program needs more than expressions.

The assignment `name = expression` is not an expression. It is a statement that bind a variable with the value on the RHS.

There are two types of statements: simple statement and compound statement.

### Simple Statements

Statements that are short and usually written in one line are _simple statements_.

Simple statements include

- assignment statement `name = expression`
- return statement: `return expression`
- import statement: `import module_name`
- ...

### Compound Statements

A compound statement contains multiple statements that usually span multiple lines.

Compound statements are used to control program flow or create new data types like functions and classes.

They are not expressions.

They give the "high level" abstractions that make Python more flexible and expressive. Conditional statements, loop statements, function definition are compound statements.

### Why Statements?

Typically a Python program consists of one or more statements.

All expressions are simple statements. Python has two types of expressions

- those generate a value: all operators, except the assignment operator `=`, act on their operands and create a value.
- those don't generate a value. They handle I/O or change program states. For example: `print()`, assignment.

Expressions that generate values are useless if the result is not used in a statement that stores the value in memory/disk, or sends it over network, or displays it in a terminal.

For example, you can write an expression `x + 1` as a valid statement in a Python program. But it is a waste of CPU cycles because its result is discarded. A statement like `y = x + 1` is useful because the result can be used later.

Similarly, a function call `math.sqrt(x)` is useless by itself. But`print("Hi")` is useful because it displays the string in a console.

### Walrus Operator Syntax

Walrus operator `:=` is interesting because it highlights the difference between a value-generation expression and a statement. Because `:=` generate a value, it is useless if its value is not used. You cannot write it in a single line.

For example, it is an `SyntaxError` to write the expression `x := 5` in a line. Because the evaluated value `5` is not used. If you only need assignment, use an assignment statement.

The following code shows a valid use.

```python
import math

if (x := math.sqrt(5)) > 2:
    print(x)
```
