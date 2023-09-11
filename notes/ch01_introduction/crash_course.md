# Python Crash Course

This is a crash course of Python that shows the essential computation constructs in Python. Most other programming languages also have these basic constructs. This section gives you a basic idea of what programs look like. Don't worry if it raises more questions (it should), more details will be covered in the following sections.

## 1 Hello World

It is a tradition from C programming language to say "Hello World!" as the first program in learning a new programming language.

In Python, it is a single line:

```python
print("Hello World!")
```

Without any programming experience, you can guess that it prints the `"Hello World!"` message, though not to a printer but to a computer console. In the above code, `print` is a function. A function, like a computer, process its input and performs some tasks. A function name followed by a pair of parentheses is a function call – the computer runs/executes the function. The string `"Hello World!"` is the input to the print function.
A string is written inside a pair of single or double quotes. Therefore, a pair of single quotes also works: `print('Hello World!')`.

Compare the Python code to a Java Version of "Hello World!":

```java
public class Main
{
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

Almost everything except `println("Hello World")` is a distraction -- a programming language implementation detail that is not intrinsic to the goal of displaying a message to a computer console.

## 2 Computation and Execution Modes

### 2.1 Computation

Computation in Python refers to the process of performing calculations, operations, and data manipulations using Python code.

```python
2 + 3
```

To make easier to understand, it is a good idea to add spaces before and after the + operator.

It supports standard arithmetic operations. These operations can be used with numeric data types such as integers and floating-point numbers.

```python

# addition
1 + 2

# subtraction
5 - 3

# multiplication
3 * 5

# division
7 / 5

# exponential
2**10

# quotient
7 // 3

# Modulus or Remainder
7 % 5
```

### 2.2 Execution Modes

There are two primary modes: Interactive mode and Script Mode

#### Interactive Mode

Interactive mode allows you to execute Python statements one at a time in an interactive manner. You can type and execute code directly in the Python interpreter, and the interpreter will immediately provide you with the output.

To start the Python interpreter in interactive mode, simply open a terminal or command prompt and type `python` or `python3``, depending on your setup. Once in the interactive mode, you can start entering Python statements and get instant feedback.

Example in interactive Mode:

```text
>>> 2 + 3
5
```

#### Script Mode

Script mode involves creating a Python script or program file with a `.py` extension. You write your code in the file. Execute the entire script by running the Python interpreter followed by the script filename.

For example, write a script file such as `"calculate.py"` and run it with `python3 calculate.py`. To see an output message, you need to use the built-in `print()` function to display it in the console.

```python
x = 2
y = 3
result = x + y
print("The result is:", result)
```

The interactive mode is often used for quick testing and experimentation(individual commands), while script mode is used for creating more structured and complete programs (many commands in one or more files).

### 2.3 Orders of Operations

The order of operations is important in python to ensure that expressions are evaluated correctly.

Python follows the mathematic order of precedence, the so-called `PEMDAS` rule that stands for Parentheses, Exponents, Multiplication and Division, Addition and Subtraction.

The best practice in programming is to use parentheses to make the order explicitly. Following are some examples:

```python
# Use parenthesis for operation order, they are optional here but better
(3 * 5) - 2

# Subtraction before multiplication
3 * (5 - 2)

# It is not clear which operation happens first
2**3**2

# No ambiguity, pay attention to code format
(2**3) ** 2

# No ambiguity
2 ** (3**2)
```

## 3 More Math Operations

Python put more math functions in its `math` module. A module is a Python file that provides multiple functions.

You need to import it first before use.

Following are some examples:

```python
import math

num = 25
sqrt_value = math.sqrt(num)
print(sqrt_value)

num = 10
ln_value = math.log(num)
log_value = math.log10(num)
print(ln_value)
print(log-value)
```

## 4 More Python Functions

There are three types of sources for Python functions:

- Built-in: they are essential functions that are part of the Python programming language. You can call these functions directly.
- Standard library: these are common functions that come with Python installation but you must import them before use them.
- Installation packages: you need to download and install them online first, then import them before use. For example, all AI packages.

### 4.1 Built- in Functions

These are functions that are already available as part of the Python programming language, so you can use them directly in your code.

Built-in functions cover a wide range of operations. For example: `input`,`sort`,`sum`,`abs`, and `print` etc.

You can find the complete list of Built-in functions in Python document [Built-in Functions](https://docs.python.org/3/library/functions.html).

### 4.2 Standard Library

The Python standard library contains modules and packages that come with Python itself. These modules and packages provide a wide range of functionality, from working with data types and performing mathematical operations to interacting with the operating system and implementing advanced features.

You need to `import` a module first to use its functions.

They save your time by offering pre-built tools and functionality. So that you don't waste time writing them from scratch. More importantly, new code may bring potential bugs.

Example:

- The `math` module offers various mathematical functions, and the
- The `random` module is used for random number generation.
- Modules like `os`, `io` help with file and directory operations, while `subprocess` allows running system commands.

## 5 Comparison and Logic Operations

### 5.1 Comparison

Comparisons are used to compare values and determine their relationships. They are performed using comparison operators, which result in Boolean values `True or False` based on the outcome of the comparison.

These comparison operators can be used with various types of data, including numbers, strings, and other objects that support comparisons.

Python provides following comparison operators: `>`,`<`,`==`,`!=`,`>=`,`<=`. Following are some comparison examples:

```python
3 > 2
3 == 2
3 != 2
(7 / 5) >= 1
math.sqrt(3) > 2

# comparison can be chained
2 > math.sqrt(3) > math.sqrt(2)

a = 10
b = 20
c = 30
result = (a < b) and (b < c)  # True, because both comparisons are true
```

### 5.2 Logical Operations

Logical operations, also called Boolean operations, are used to combine or manipulate boolean values (`True` and `False`). There are three primary boolean logical operators: `and`, `or`, and `not`.

```Python
# The not operator returns the opposite boolean value of its operand.
not (3 == 2)

not (3 != 2)

# The and operator returns True if both operands are True, and False otherwise.
(3 > 2) and ((7 / 5) > 3)

# The or operator returns True if at least one of the operands is True, and False if both operands are False.
(3 == 2) or (3 >= 2)
```

The logical operations follow certain precedence rules: `not` followed by `and` that is followed by `or`. You should use parentheses to make the order of evaluation explicit.

## 6 Variable

A Python variable is a symbolic name that is a reference to a data.

Variables are useful in different ways:

- Name a data: `pi = 3.141592653589793`
- Store the result of an operation: `diameter = 2 * radius`
- Use a short reference in multiple places: `circumference = pi * diameter`
- Refer a non-existing data from input: `radius_input = input("Please input radius: ")`

## 7 Program

You create programs by writing code in a file, typically referred to as a script or code file. These files have a `.py` extension, indicating that they contain Python code.

A script file often contains multiple lines of code. These lines collectively define the logic, functionality, and behavior of your program. Python runs the code in a script file sequentially, from top to bottom. Each line of code is executed in the order it appears in the file.

Integrated Development Environments (IDEs), such as VS Code, provide a user-friendly environment for writing, editing, and managing code. IDEs often offer features like syntax highlighting, which visually distinguishes different elements of the code, making it easier to read and spot errors.

### 7.1 A Simple Program

Following is a simple program

```python
pi = 3.14159

# display a message and take user input
radius_input = input("Please input radius: ")

# convert input string into a float number
radius = float(radius_input)
diameter = 2 * radius
circumference = pi * diameter
print(circumference)
```

### 7.2 `f-string`

For the above simple program, we can make some changes and make it as a better Output,By adding `f-string`(formatted String Literals).

Formatted string literals are a convenient way to embed expressions inside string literals in Python. They provide a concise and readable way to interpolate variables and expressions into strings.

F-strings are particularly useful when you want to create strings with dynamic content without the need for explicit concatenation or formatting functions.

To create an f-string, prefix the string literal with an `'f'` or `'F'`, and then enclose expressions in curly braces `{}` within the string.

The expressions inside the curly braces will be evaluated and inserted into the string. For example: `f"The circumference of radius {radius} is {circumference}."`

You can also add format modifiers that specify the number of decimal places for floats, the width of the field, and more. `f"The circumference of radius {radius:.2f} is {circumference:.4f}`. The `:2f` is a format modifier that shows 2 places after the decimal.

### 7.3 The Revised Program

The above program can be revised with formatted output like the following:

```python
import math
# display a message and take user input
radius_input = input("Please input radius: ")
# convert input text into a float number
radius = float(radius_input)
diameter = 2 * radius

# Python has a predefined pi variable in the math module
circumference = math.pi * diameter
print(f"The circumference of radius {radius:.2f} is {circumference:.4f}.")
```

## 8 Branches and Loops

## 9 Composite Data

## 10 Functions

## 11 Summary
