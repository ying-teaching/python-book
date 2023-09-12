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

### 8.1 Branches

Branches allow you to execute different code blocks based on conditions.
In Python, you can use the `if`, `elif`, and `else` statements to create branching logic.

```python
if condition:
    # Code to run if condition is True
elif another_condition:
    # Code to run if another_condition is True
else:
    # Code to run if none of the conditions are True
```

In the following code, you evaluate multiple conditions sequentially and execute the corresponding code block for the first condition that is true. If none of the conditions are true, the else block is executed.

```python
# display a message and take user input
score_input = input("Please input your score: ")
# convert input text into an integer
score = int(score_input)
if score >= 900:
    grade = "A"
elif score >= 800:
    grade = "B"
else:
    grade = "C"
result = f"Grade is {grade}."
print(result)
```

### 8.2 While Loop

While loops repeatedly execute a block of code as long as a certain condition is `True`. It's essential for scenarios where the number of iterations is uncertain and depends on runtime conditions.
Syntax:

```python
while condition:
    # Code to execute while the condition is True
```

The logic of the `while` statement is as the following:

1. The condition is evaluated. If it's True, the code block inside the loop is executed.
2. After the code block execution, the condition is re-evaluated.
3. If the condition is still True, the code block is executed again.
4. This process continues until the condition becomes False. At that point, the loop exits, and the program continues executing the next line of code after the loop.

Below is an example:

```python
score_input = input("Please input your score: ")
score = int(score_input)
while score < 900:
    print("Please keep studying and practicing....")
    score_input = input("Please input new score: ")
    score = int(score_input)

print("Great, you made it!")
```

Be cautious when using while loops. If the condition never becomes False, you'll end up with an infinite loop, which means the loop will keep running indefinitely. This can freeze your program and potentially crash your computer.

## 9 Composite Data

Composite data in Python refers to the combination of multiple data elements into a single data structure. Python provides several built-in data structures to work with composite data, including strings, lists, dictionaries, and so on. These structures allow you to organize, store, and manipulate related data in a coherent manner.

Following are data you often see in real world:

- A class has 50 students.
- Each student has name, age, major, and GPA.
- An AI model may use billions of record.
- and so on ...

### 9.1 Lists

Python provides several built-in data structures to work with composite data, `list` is often used as a collection of items. There are other composite types to be covered later.

You can create a list by enclosing a comma-separated sequence of values within square brackets `[]`. List elements are accessed using index values in a pair of square bracket, starting from `0` for the first element. If the index is out of range, your code crashes with an `IndexError` exception. An _exception_ gives the type of an error.

```python
scores = [930, 790, 367, 827]
grades = ["A", "B", "C", "D", "F"]

# access individual item
print(scores[0])
print(grades[4])

# oops, an IndexError
print(grades[6])
```

### 9.2 For Loop

The `for` loop is a fundamental control flow statement in Python used for iterating over sequences, such as lists, strings, dictionaries, and more.
Syntax:

```python
for element in sequence:
    # Code to execute for each element
```

The processing logic of the `for` loop is as following:

1. The for loop initializes the loop variable (element) with the first element of the sequence.
2. The code block inside the loop is executed using the current value of the loop variable (element).
3. After the code block execution, the loop variable is updated to the next element in the sequence.
4. Steps 2 and 3 are repeated for each element in the sequence until the loop reaches the end of the sequence.

```python
scores = [930, 790, 367, 827]
# in each iteration of this for loop
# the score is assigned the next value in the list
# starting from index 0 to the last one.
for score in scores:
    if score >= 900:
        print(f"Great, you got an A.")
else:
    difference = 900 - score
    print(f"You need {difference} points to get an A.")
print("Done.")
```

### 9.3 Dictionary

Dictionaries are another important data structure in Python. Unlike lists, which use numerical indices to access elements, dictionaries use keys to access their values. This makes dictionaries highly efficient for looking up and storing data associated with specific identifiers. Dictionaries are often referred to as `"key-value" pairs`, where each key is associated with a corresponding value.

Dictionaries are created using curly braces `{}`. Each key-value pair is separated by a colon : and individual pairs are separated by commas `,`.

You can use `dictionary[key]` to access the value of a key. Use `for` loop to access every key in a dictionary.

```python
student = {"Name": "Alice", "Age": 20, "Major": "IS"}

# use a key to read or change a dictionary value
print(student["Name"])
student["Age"] = 21
print(student["Age"])

# iterate every key
for key in student:
    message = f"Key {key} has a value of {student[key]}"
    print(message)
```

## 10 Functions

Functions are a fundamental concept in Python (and programming in general) that allow you to organize and reuse blocks of code.

You want define a function that can be reused for different reasons:

- No redundant code.
- Function name shows its purpose.
- It can be used in other places.

Following is a function definition and its use.

```python
import math
# define a function with a parameter radius
# the body is a code block to do the real work
def get_circumference(radius):
    diameter = 2 * radius
    circumference = math.pi * diameter
    return circumference

radiuses = [1, 5, 10]
for radius in radiuses:
    # here the radius is the argument of the function call
    circumference = get_circumference(radius)
    print(f"The circumference is {circumference:.4f}.")
```

A function is a self-contained block of code that can take inputs (_parameters_), perform a specific task, and return an output (_return value_). Following are key function concepts/terms used in this book:

1. Function Name: Describes the purpose or action that the function performs. It's used to call the function and execute its code.
2. Function Call: Involves executing the function by appending a pair of parentheses after the function name. This triggers the function's code to run.
3. Parameters: These are placeholders in the function definition that specify the type and order of inputs the function expects. They act as local variables within the function body.
4. Arguments: Actual values provided when calling a function. These values are passed to the function's parameters and used within the function's code.
5. Function Body: A code block within the function definition. It contains the instructions and logic that define the function's behavior.
6. Return Value: The result or output of a function call. It's the value that the function sends back to the caller when the function completes its execution.

## 11 Objects

In Python, all data are objects. Every object has a type that determines the valid operations of the object. You can use built-in function `type()` to get an object’s type. For example:

```python
type("hi") # <class 'str'>
type(3) # <class 'int'>
```

Function defined inside a type is called a _method_. You call a method using the _dot notation_.

An object may contain data that is called an _attribute_. You use a dot notation to access an attribute.

For example, the `math` module is an object that has an object called `pi`.

```python
print("hi".title())  # Hi

import math

print(math.pi)  # 3.141592653589793
```

## 12 Summary

This chapter gives a crash course of fundamental Python programming concepts.

- Arithmetic and Logic Operations: Mathematical and comparison operations that manipulate and evaluate values.
- Variables: Named containers for storing data, allowing referencing and manipulation.
- Control flow
  - Sequential Execution: Code executed line by line, top to bottom, in the order written.
  - Branch: Conditional statements enabling different paths based on conditions.
  - Loop: Repetitive execution of code as long as certain conditions are met.
- Composite Data:Structures for combining multiple data elements into one, like lists and dictionaries.
- Function: A reusable block of code encapsulating a task, with parameters and return values.

Everything else is nice/bad-to-have optional: they are there to provide handy functions.

Using these concepts/tools to solve problems is called _computational_ or _algorithmic_ thinking.
