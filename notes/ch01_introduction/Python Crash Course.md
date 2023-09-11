# Python Crash Course

This is a crash course of Python that shows the essential computation constructs in Python. Most other programming languages also have these basic constructs. This section gives you a basic idea of what programs look like. Don't worry if it raises more questions (it should), more details will be covered in the following sections.

## 1 Hello World

It is a tradition from C programming language to say "Hello World!" as the first program in learning a new programming language.

In Python, it is a single line:

```python
print("Hello World!")
```

Without any programming experience, you can guess that it prints the "Hello World!" message, though not to a printer but to a computer console. In the above code, `print` is a function. A function, like a computer, process its input and performs some tasks. A function name followed by a pair of parentheses is a function call – the computer runs/executes the function. The string `"Hello World!"` is the input to the print function.
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

Almost everything except `println("Hello World")` is a distraction.

The `print("Hello World!")`

## 2 Computation and Execution Modes
Computation in Python refers to the process of performing calculations, operations, and data manipulations using Python code.
```python
2 + 3
```
To make easier to understand, it is a good idea to add spaces before and after the + operator.
It supports standard arithmetic operations.
These operations can be used with numeric data types such as integers and floating-point numbers.

Addition
```python
1 + 2
```
Subtraction
```python 
5 - 3
```
Multiplication
```python
3 * 5 
```
Division
```python
7 / 5
```
Exponential
```python
2**10
```
Quotient
```python
7 // 3
```
Modulus or Remainder
```python
7 % 5
```

There are two primary modes: Interactive mode and Script Mode
Interactive Mode:
Interactive mode allows you to execute Python statements one at a time in an interactive manner. You can type and execute code directly in the Python interpreter, and the interpreter will immediately provide you with the output.

To start the Python interpreter in interactive mode, 
simply open a terminal or command prompt and type python or python3, depending on your setup. Once in the interactive mode, you can start entering Python statements and get instant feedback.
Example in interactive Mode:
```
>>> 2 + 3
5
```
Script Mode:
Script mode involves creating a Python script or program file with a .py extension.
You write your code in the file 
Execute the entire script by running the Python interpreter followed by the script filename.

Example:
write a script file such as “calculate.py” and  run it with “python3 calculate.py".
you need to use the built-in “print” function to display it in the console like "print()"
```python
x = 2
y = 3
result = x + y
print("The result is:", result)
```
We can use the Interactive mode is for quick testing and experimentation(Individual commands), while script mode is for creating more structured and complete programs(Commands on group of files).

Orders of Operations:
The order of operations is important in python to ensure that expressions are evaluated correctly. 
You need to follow Order of precedence PEMDAS stands for Parentheses, Exponents, Multiplication and Division, Addition and Subtraction.
Examples:
Use parenthesis for operation order
they are optional here but better
```python
(3 * 5) - 2
```
Subtraction before multiplication
```python
3 * (5 - 2)
```
Not clear
```python
2**3**2
```
No ambiguity, pay attention to code format
```python
(2**3) ** 2
```
No ambiguity
```python
2 ** (3**2)
```
## 3 More Functions: `math` Module and Standard Library
In Python you have a standard library which provides a wide range of math-related functions through the math module
This module is part of the standard library and offers various mathematical operations and constants.
To use these functions, you need to import the `math` module in your Python script.
Examples:
Square Root` (math.sqrt())`: This function returns the square root of a given number.
```python
import math
num = 25
sqrt_value = math.sqrt(num)
print(sqrt_value)
```
Exponential `(math.exp())`: This function returns the value of e raised to the power of the given number.
```python
import math
num = 2
exp_value = math.exp(num)
print(exp_value)
```
Logarithms (`math.log()` and math.log10()): These functions are used to calculate the natural logarithm and base-10 logarithm of a number, respectively
```python
import math
num = 10
ln_value = math.log(num)       
log_value = math.log10(num)
print(ln_value)
print(log-value)
```
## 4. Python Functions
Python functions are categorized based on the purpose and behaviour.
##### Built- in Functions:
These are functions that are already available in Python, so you can use them without defining them.
Built-in functions that cover a wide range of operations
Example: `Input`,`Sort`,`Sum`,`abs`,`Print`etc
You can find complete list of Buil-in functions:
`https://docs.python.org/3/library/functions.html `

##### Standard Library:
The Python standard library contains modules and packages that come with Python itself. These modules and packages provide a wide range of functionality, from working with data types and performing mathematical operations to interacting with the operating system and implementing advanced features.
You need to import the module first to use it functions.
They save you time by offering pre-built tools and functionality. So that you dont waste time.
Example:
1. Built-in Functions: 
These are functions that are always available without any imports.
`print(), len(), range()` etc.
2. Math and Numbers: 
The `math` module offers various mathematical functions, and the 
`random` module is used for random number generation.
3. File I/O and OS Interaction: 
Modules like `os`, `io` help with file and directory operations, while `subprocess` allows running system commands.

##### Comparison
1. Comparisons are used to compare values and determine their relationships.
2. Comparisons are usually performed using comparison operators, which result in Boolean values `True or False` based on the outcome of the comparison.
3. These comparison operators can be used with various types of data, including numbers, strings, and other objects that support comparisons.
4. These are the comparisons that we use in python `>`,`<`,`==`,`!=`,`>=`,`<=`,`and`,`or`

Examples:
```python
3 > 2
```
```python
3 == 2
```
```python
3 != 2
```
```python
(7 / 5) >= 1
```
```python
math.sqrt(3) > 2
```
Can be chained

```python
 2 > math.sqrt(3) > math.sqrt(2)
 ```

```python
a = 10
b = 20
c = 30
result = (a < b) and (b < c)  # True, because both comparisons are true
```
##### Boolean (Logical) Operations
Boolean logical operations are used to combine or manipulate boolean values (True and False). 
There are three primary boolean logical operators: `and`,` or`, and `not`.
not Operator:

The not operator returns the opposite boolean value of its operand.
```Python
not (3 == 2)
```
```python
not (3 != 2)
```
The and operator returns True if both operands are True, and False otherwise.
```python
(3 > 2) and ((7 / 5) > 3)
```
The or operator returns True if at least one of the operands is True, and False if both operands are False.
```python
(3 == 2) or (3 >= 2)
```
The logical operations follow certain precedence rules (not > and > or), but you can use parentheses to control the order of evaluation when necessary.

## 5 Variables
1. Variables are used to store and manage data values.
2. A variable is a named location in memory where you can store a value, and you can later reference that value by using the variable's name. 
3. Variables allow you to work with data and manipulate it in your programs.

Variable Naming Rules:
1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. Avoid using Python keywords and built-in function names as variable names.

Data Types:
1. Variables in Python can hold various data types, including integers, floats, strings, booleans, lists, dictionaries, and more. 
2.Python is dynamically typed, meaning you don't need to explicitly declare the variable's type.
```python
num = 42               # integer
pi = 3.14159           # float
message = "Hello"      # string
```
Use a short reference in multiple places: 
```python
circumference = pi * diameter
```
## Simple Program:

```python
pi = 3.14159
```
display a message and take user input
```python
radius_input = input("Please input radius: ")
```
convert input string into a float number
```python
radius = float(radius_input)
diameter = 2 * radius
circumference = pi * diameter
print(circumference)
```
#### Better Output
For the above simple program, we can make some changes and make it as a better Output,By adding `f-string`(formatted String Literals).
Formatted string literals are a convenient way to embed expressions inside string literals in Python. 
They provide a concise and readable way to interpolate variables and expressions into strings.
F-strings are particularly useful when you want to create strings with dynamic content without the need for explicit concatenation or formatting functions.

###### Syntax:
To create an f-string, prefix the string literal with an 'f' or 'F', and then enclose expressions in curly braces {} within the string.
The expressions inside the curly braces will be evaluated and inserted into the string.
For example: 
```python
f"The circumference of radius {radius} is {circumference}."
```
You can also add format modifiers:
That means you can specify the number of decimal places for floats, the width of the field, and more.
```python
f"The circumference of radius {radius:.2f} is {circumference:.4f}."
```
The :2f is a format modifier that shows 2 places after the decimal.

## Python Program
1. Creating Programs by writing Code:
You create programs by writing code in a file, typically referred to as a script or code file. These files have a .py extension, indicating that they contain Python code.
2. Structure of Script Files:
A script file often contains multiple lines of code. These lines collectively define the logic, functionality, and behavior of your program.
3. Execution Line by Line:
Python runs the code in a script file sequentially, from top to bottom. Each line of code is executed in the order it appears in the file.
4. IDEs and Syntax Highlighting:
Integrated Development Environments (IDEs), such as VS Code, provide a user-friendly environment for writing, editing, and managing code. IDEs often offer features like syntax highlighting, which visually distinguishes different elements of the code, making it easier to read and spot errors.

## 6 Branches and Loops
These are fundamental programming topics that allow you to control the flow of execution in your Python programs.
It make decisions and repeat actions, making your code more flexible.
##### Branches(Conditional Statements):
Branches allow you to execute different code blocks based on conditions. 
In Python, you can use the `if`, `elif`, and `else` statements to create branching logic.
``` python
if condition:
    # Code to run if condition is True
elif another_condition:
    # Code to run if another_condition is True
else:
    # Code to run if none of the conditions are True
```
Example:
```Python
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
In the above code, you evaluate multiple conditions sequentially and execute the corresponding code block for the first condition that is true. If none of the conditions are true, the else block is executed.
##### Loops:
Loops allow you to repeat a block of code multiple times.
In Python, you have two primary types of loops:
1. While Loops
2. For Loops

##### While Loops:(You repeat yourself a lot)
While loops repeatedly execute a block of code as long as a certain condition is `True`.
It's essential for scenarios where the number of iterations is uncertain and depends on runtime conditions.
Syntax:
```python
while condition:
    # Code to execute while the condition is True
```
Example:
Flow for the example,
1. The condition is evaluated. If it's True, the code block inside the loop is executed.
2. After the code block execution, the condition is re-evaluated.
3. If the condition is still True, the code block is executed again.
4. This process continues until the condition becomes False. At that point, the loop exits, and the program continues executing the next line of code after the loop.
```python
score_input = input("Please input your score: ")
score = int(score_input)
while score < 900:
    print("Plese keep studying and practing....")
    score_input = input("Please input new score: ")
    score = int(score_input)
print("Great, you made it!")
```
Be cautious when using while loops. If the condition never becomes False, you'll end up with an infinite loop, which means the loop will keep running indefinitely. This can freeze your program and potentially crash your computer.

##### Loop Control Statements
You can use loop control statements like break and continue within a while loop to modify its behavior.
`break`: Terminates the loop prematurely.
`continue`: Skips the current iteration and proceeds to the next.
Example(break):
```python
count = 0
while count < 5:
    if count == 3:
        break
    print(f"Count is {count}")
    count += 1
```
Example(Continue):
```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(f"Count is {count}")
```
##### For Loops(Acess every list item)
The `for` loop is a fundamental control flow statement in Python used for iterating over sequences, such as lists, strings, dictionaries, and more.
Syntax:
```python
for element in sequence:
    # Code to execute for each element
```
Flow:
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
## 7 Composite Data
Composite data in Python refers to the combination of multiple data elements into a single data structure.
This allows you to represent complex structures and relationships more effectively.
Python provides several built-in data structures to work with composite data, including lists, dictionaries, tuples, and sets. These structures allow you to organize, store, and manipulate related data in a coherent manner.
#### Lists: (Real world data is complex)
A class has 50 students.
Each student has name, age, major, and GPA.
An AI model may use billions of record.
…
..
You want to represent the above `compound` data.
In the above described scenario, using `lists` is a practical and effective way to represent compound data.
1. Lists allow you to store collections of items, which can be of the same or different data types. 
2. Lists are ordered, meaning the order of elements you add to the list is maintained.
3. They are mutable, so you can add, remove, or modify elements within a list.

Creating Lists:
You can create a list by enclosing a comma-separated sequence of values within square brackets `[]`
Examples:
```python
scores = [930, 790, 367, 827]
grades = ["A", "B", "C", "D", "F"]
mixed_types = [10, "hello", True, 3.14]
empty_list = []
```
Accessing List Elements:
List elements are accessed using index values, starting from 0 for the first element.
```python
print(scores[0])
print(grades[4])
```
Modifying Lists:
You can modify individual elements or change their values.
```python
scores = [930, 790, 367, 827]
scores[1] = "246"
# Scores in row [930,246,367,827]
```
Adding Elements:
You can add elements to a list using the `append()` method to add to the end, or the `insert()` method to add at a specific position.
```python
scores = [930, 790, 367, 827]
scores.append("246")
# scores is now [930, 790, 367, 827,246]
```
Removing Elements:
Use methods like` remove()`, `pop()`, and `del` to remove elements from a list.
```python
scores = [930, 790, 367, 827]
scores.remove(790)
# scores is now [930,367,827]
```
Looping Through Lists:
Lists are iterable, meaning you can loop through their elements using a for loop.
```python
scores = [930, 790, 367, 827]
for sc in scores:
    print(f"My score {sc}")
```
List Length:
The `len()` function gives you the length (number of elements) in a list.
```python
scores = [930, 790, 367, 827]
length = len(scores)  # 4
print(length)
```
#### Dictionaries(Associate a key with a value)
Dictionaries are another important data structure in Python. Unlike lists, which use numerical indices to access elements, dictionaries use keys to access their values. 
This makes dictionaries highly efficient for looking up and storing data associated with specific identifiers. Dictionaries are often referred to as `"key-value" pairs`, where each key is associated with a corresponding value.

Creating Dictionaries:
Dictionaries are created using curly braces `{}`. Each key-value pair is separated by a colon : and individual pairs are separated by commas `,`.
```python
student = {"Name": "Alice", "Age": 20, "Major": "IS"}
```
```python
# use a key to read or change a dictionary value
print(student["Name"])
student["Age"] = 21
print(student["Age"])
```
Accessing Dictionary Values:
Dictionary values are accessed using their keys.
```python
for key in student.keys():
    message = f"Key {key} has a value of {student[key]}"
    print(message)
```
## 8 Functions
Functions are a fundamental concept in Python (and programming in general) that allow you to organize and reuse blocks of code.
A function is a self-contained block of code that can take inputs (arguments), perform a specific task, and return an output (return value).
1. Function Name: Describes the purpose or action that the function performs. It's used to call the function and execute its code.
2. Function Call: Involves executing the function by appending a pair of parentheses after the function name. This triggers the function's code to run.
3. Parameters: These are placeholders in the function definition that specify the type and order of inputs the function expects. They act as local variables within the function body.
4. Arguments: Actual values provided when calling a function. These values are passed to the function's parameters and used within the function's code.
5. Function Body: A code block within the function definition. It contains the instructions and logic that define the function's behavior.
6. Return Value: The result or output of a function call. It's the value that the function sends back to the caller when the function completes its execution.

## 9 Summary
##### Arithmetic and Logic Operations: 
Mathematical and comparison operations that manipulate and evaluate values.
##### Variables: 
Named containers for storing data, allowing referencing and manipulation.
##### Sequential Execution:
Code executed line by line, top to bottom, in the order written.
##### Branch:
Conditional statements enabling different paths based on conditions.
##### Loop: 
Repetitive execution of code as long as certain conditions are met.
##### Composite Data: 
Structures for combining multiple data elements into one, like lists and dictionaries.
##### Function:
A reusable block of code encapsulating a task, with parameters and return values.
