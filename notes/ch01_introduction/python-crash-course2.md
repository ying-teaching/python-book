# Python Crash Course

This is a crash course of Python that shows the essential computation constructs in Python. Most other programming languages also have these basic constructs. This section gives you a basic idea of what programs look like. Don't worry if it raises more questions (it should), more details will be covered in the following sections.

## **1. Hello World**

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


## **2. Computation and Execution Modes**

We all know that a machine that can compute is called as the "Computer". Now for python, it has two execution modes:

### 1. Interactive Mode

In interactive mode, the Python interpreter reads and executes Python statements one at a time. The Python interpreter starts by reading a line of input from the user. If the line of input is a statement, the Python interpreter executes the statement. The user can enter any Python statement or expression at any time.

- The result is displayed directly in the console
- Convenient for small code snippets


```python
>>>2 + 3
5
```
### 2. Script Mode

In script mode, the Python interpreter reads and executes a single script file. The script file can be a Python script, a module, or a package. The Python interpreter starts by reading the first line of the script file. If the first line of the script file is a comment, the Python interpreter ignores it. If the first line of the script file is a statement, the Python interpreter executes the statement. If the first line of the script file is a function definition, the Python interpreter defines the function. If the first line of the script file is a class definition, the Python interpreter defines the class.

- Good for non-trivial code and real applications
- To see the result, you need the built-in “print” function to display it in the console like “print(2 + 3)


## **3. Variables (Literals Are Not Enough!)**

In Python, variables play a crucial role in managing and manipulating data. While we've been working with literal values like numbers (e.g., 5, 3) and text ("Hello World!"), there comes a point where we need to:

- **Name Data:** Assign meaningful names to data for easy reference.
- **Store Results:** Capture and store the outcome of operations for future use.
- **Create References:** Use concise references in multiple parts of our code.
- **Handle Non-existing Data:** Manage scenarios where data might not exist initially.

Let's delve into how variables can help us achieve these goals.

Storing Results
Variables allow us to hold the results of computations. For example:

```python
x = 10
y = 5
sum_result = x + y  # Store the result of the addition
```

Creating References
Variables help us avoid redundancy. If we're using the same value in multiple places, it's more efficient to use a variable:

```python
tax_rate = 0.15
income = 1000
tax_amount = income * tax_rate
```
By using tax_rate and income variables, our code becomes clearer and easier to maintain.

Handling Non-existing Data
Variables can also represent data that doesn't exist initially, such as user input:

```python
user_input = input("Enter your name: ")
print("Hello, " + user_input)
```
Here, user_input initially holds no value until the user provides input. We can then use it within our program.

Now, we can use sum_result to access the sum of x and y.



## **4. Arithmetic and Logic Operations**

### Arithmetic Operations in Python

Python, like many programming languages, supports various arithmetic operations that allow you to perform mathematical calculations. In this guide, we'll cover the common arithmetic operations and the order of operations.

### Common Arithmetic Operations

Python supports the following arithmetic operations:

- **Addition (`+`)**: Adds two numbers together.
  
  ```python
  result = 5 + 3  # result will be 8
  ```

- **Subtraction (`-`)**: Subtracts the second number from the first.
  
  ```python
  result = 10 - 4  # result will be 6
  ```

- **Multiplication (`*`)**: Multiplies two numbers.
  
  ```python
  result = 6 * 7  # result will be 42
  ```

- **Division (`/`)**: Divides the first number by the second, resulting in a floating-point number.
  
  ```python
  result = 10 / 3  # result will be 3.3333333333333335
  ```

- **Floor Division (`//`)**: Divides the first number by the second and rounds down to the nearest integer.
  
  ```python
  result = 10 // 3  # result will be 3
  ```

- **Modulus (`%`)**: Computes the remainder when dividing the first number by the second.
  
  ```python
  result = 10 % 3  # result will be 1
  ```

- **Exponentiation (`**`)**: Raises the first number to the power of the second.
  
  ```python
  result = 2 ** 3  # result will be 8
  ```

### Order of Operations

When multiple arithmetic operations are combined in a single expression, Python follows the standard order of operations (also known as PEMDAS/BODMAS):

1. **P**arentheses/Brackets: Expressions within parentheses are evaluated first.

2. **E**xponents/Orders (i.e., Powers and Square Roots): Exponents are calculated next.

3. **M**ultiplication and **D**ivision (from left to right): Multiplication and division operations are performed before addition and subtraction.

4. **A**ddition and **S**ubtraction (from left to right): Finally, addition and subtraction operations are carried out.

Here's an example illustrating the order of operations:

```python
result = 2 * (3 + 4) ** 2 / 8 - 1
```

1. Parentheses: `(3 + 4)` is evaluated first, resulting in `7`.
2. Exponentiation: `7 ** 2` equals `49`.
3. Multiplication and Division: `2 * 49 / 8` simplifies to `98 / 8`, which equals `12.25`.
4. Subtraction: `12.25 - 1` results in the final value of `11.25`.

### Logic Operations in Python

Logic operations, often referred to as boolean operations, are fundamental in programming for making decisions and controlling the flow of your code based on conditions. Python provides several logical operators that allow you to work with boolean values (`True` or `False`) and make comparisons. Here are the key logical operators in Python:

**1. Comparison Operators:**
   Comparison operators are used to compare values and evaluate expressions. They return boolean values (`True` or `False`).

   - `==`: Equal to
   - `!=`: Not equal to
   - `<`: Less than
   - `>`: Greater than
   - `<=`: Less than or equal to
   - `>=`: Greater than or equal to

   ```python
   x = 5
   y = 10
   print(x == y)   # False
   print(x < y)    # True
   ```

**2. Logical Operators:**
   Logical operators are used to combine and manipulate boolean values.

   - `and`: Returns `True` if both operands are `True`.
   - `or`: Returns `True` if at least one operand is `True`.
   - `not`: Returns the opposite boolean value (negation).

   ```python
   a = True
   b = False
   print(a and b)  # False
   print(a or b)   # True
   print(not a)    # False
   ```

**3. Membership Operators:**
   Membership operators are used to test if a value is a member of a sequence (like a list, tuple, or string).

   - `in`: Returns `True` if the value is found in the sequence.
   - `not in`: Returns `True` if the value is not found in the sequence.

   ```python
   fruits = ["apple", "banana", "cherry"]
   print("apple" in fruits)       # True
   print("pear" not in fruits)    # True
   ```

**4. Identity Operators:**
   Identity operators are used to compare the memory locations of two objects.

   - `is`: Returns `True` if both variables point to the same object.
   - `is not`: Returns `True` if both variables point to different objects.

   ```python
   x = [1, 2, 3]
   y = [1, 2, 3]
   print(x is y)       # False
   print(x is not y)   # True
   ```

Logical operations are crucial for creating branching (using `if`, `elif`, and `else` statements) and loop conditions (using `while` and `for` loops), enabling you to create dynamic and responsive programs.



## **5. Branches and Loops**

Branches and loops are fundamental control structures in programming that allow you to make decisions and repeat actions based on certain conditions. In Python, you can use if statements for branching and various loop constructs for repetition.

### **Branching with if Statements:**

### Syntax of an if Statement:
```python
if condition:
    # Code to execute if the condition is true
```

### Example:
```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are not yet an adult.")
```

### **Loops:**

### 1. For Loop:
Used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

#### Syntax of a for Loop:
```python
for element in sequence:
    # Code to execute for each element
```

#### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2. While Loop:
Executes a block of code repeatedly as long as a certain condition is true.

#### Syntax of a while Loop:
```python
while condition:
    # Code to execute while the condition is true
```

#### Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 3. Loop Control Statements:
Python provides loop control statements like `break` and `continue`:

- `break`: Terminates the loop prematurely.
- `continue`: Skips the current iteration and moves to the next one.

#### Example:
```python
for num in range(10):
    if num == 5:
        break  # Exit the loop when num becomes 5
    print(num)
```

### **Nested Loops:**

You can nest loops within each other to perform more complex iterations.

### Example of Nested Loop:
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

In this example, the inner loop will run twice for each iteration of the outer loop, resulting in a total of 6 iterations.

These control structures (if statements and loops) are essential for creating dynamic and interactive programs, allowing you to execute different code paths and repeat actions as needed.

## **6. Composite Data**

In Python, composite data types are used to group together multiple values of different or similar types into a single unit. These data types help in organizing and manipulating more complex data structures. Some of the primary composite data types in Python are:

1. **Lists:**
   A list is an ordered collection of items, and each item can be of a different data type. Lists are created using square brackets `[]`.

   ```python
   numbers = [1, 2, 3, 4, 5]
   names = ["Alice", "Bob", "Charlie"]
   mixed_list = [10, "hello", 3.14]
   ```

2. **Tuples:**
   Similar to lists, tuples are ordered collections, but unlike lists, they are immutable (cannot be changed after creation). Tuples are defined using parentheses `()`.

   ```python
   coordinates = (10, 20)
   person_info = ("Alice", 25, "Engineer")
   ```

3. **Dictionaries:**
   A dictionary is an unordered collection of key-value pairs. Each key must be unique, and it's used to access its corresponding value. Dictionaries are defined using curly braces `{}`.

   ```python
   student = {"name": "Bob", "age": 21, "major": "Math"}
   contact_info = {"email": "bob@example.com", "phone": "123-456-7890"}
   ```

4. **Sets:**
   A set is an unordered collection of unique elements. Sets are useful for tasks like finding unique values in a list. Sets are defined using curly braces `{}`.

   ```python
   unique_numbers = {1, 2, 3, 4, 5}
   unique_letters = {"a", "b", "c"}
   ```

5. **Nested Data Structures:**
   You can create more complex structures by nesting one composite data type within another. For example, a list of dictionaries or a dictionary of lists.

   ```python
   student_records = [
       {"name": "Alice", "age": 23},
       {"name": "Bob", "age": 21}
   ]
   
   course_data = {
       "course_name": "Python Programming",
       "students": ["Alice", "Bob", "Charlie"]
   }
   ```

Composite data types allow you to model and manage data in a way that mirrors real-world scenarios more accurately. They enable you to represent relationships between different pieces of information and provide tools to manipulate these structures efficiently.

## **7. Functions**

In Python, a function is a named block of code that performs a specific task. Functions allow you to organize code into reusable modules, making your code more modular, readable, and maintainable. Here's how you can define and use functions in Python:


### **1. Syntax of Function Definition:**
```python
def function_name(parameters):
    """
    Docstring: Description of the function.
    """
    # Function code
    return result  # Optional, returns a value
```

### Example:
```python
def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")
```


### **2. Syntax of Calling a Function:**
```python
function_name(arguments)
```

### Example:
```python
greet("Alice")  # Calling the greet function
```

### **3. Function Parameters:**

Functions can accept input data, known as parameters or arguments. Parameters provide a way to pass data to functions.

### Positional Arguments:
```python
def add(a, b):
    return a + b

result = add(5, 3)  # result will be 8
```

### Default Arguments:
```python
def power(base, exponent=2):
    return base ** exponent

square = power(4)       # square will be 16 (4^2)
cubed = power(3, 3)     # cubed will be 27 (3^3)
```

### **4. Return Values:**

Functions can return a value using the `return` statement. If no `return` statement is used, the function returns `None`.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)  # result will be 20
```


### **5. Scope and Lifetime of Variables:**

Variables defined within a function have local scope and are only accessible within that function. Variables defined outside functions have global scope and can be accessed from anywhere in the code.

Functions are essential building blocks of programming. They help you encapsulate logic, promote reusability, and improve code organization. By defining and using functions effectively, you can create well-structured and efficient programs.


## **8. More Functions: `math` Module and Standard Library**

Python's standard library provides a wide range of built-in modules that offer various functionalities. One such useful module is the `math` module, which provides mathematical functions and constants. Let's explore some functions from the `math` module and discuss the concept of standard libraries.

### Using the `math` Module:

To use the `math` module, you first need to import it:

```python
import math
```

Here are some commonly used functions and constants from the `math` module:

- `math.sqrt(x)`: Returns the square root of `x`.
- `math.ceil(x)`: Returns the smallest integer greater than or equal to `x`.
- `math.floor(x)`: Returns the largest integer less than or equal to `x`.
- `math.pow(x, y)`: Returns `x` raised to the power of `y`.
- `math.pi`: A constant representing the value of π (3.141592...).
- `math.e`: A constant representing the base of the natural logarithm (2.718281...).

```python
import math

print(math.sqrt(25))      # 5.0
print(math.ceil(5.3))     # 6
print(math.floor(5.8))    # 5
print(math.pow(2, 3))     # 8.0
print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045
```

### Standard Library:

Python's standard library is a collection of modules that come pre-installed with Python and cover a wide range of functionalities. These modules provide tools for various tasks, such as file handling, data manipulation, networking, and more. The standard library is a powerful resource that can save you time and effort by providing well-tested solutions to common programming challenges.

To use a module from the standard library, you typically start by importing it using the `import` keyword, just like with the `math` module:

```python
import module_name
```

For example, the `random` module allows you to generate random numbers and make random choices:

```python
import random

random_number = random.randint(1, 100)  # Generates a random integer between 1 and 100
print(random_number)
```

Similarly, the `datetime` module provides functions for working with dates and times:

```python
import datetime

current_time = datetime.datetime.now()
print(current_time)
```

These are just a couple of examples. Python's standard library offers hundreds of modules, each with its own set of functionalities. You can explore the Python documentation to learn more about the modules available and how to use them effectively.

Using modules from the standard library can significantly simplify your programming tasks, as you can leverage existing solutions rather than reinventing the wheel.


## **9. Summary**

This crash course covers the fundamental concepts of Python programming, providing you with a solid foundation to build upon. Keep in mind that this summary is an overview, and each topic can be explored in greater depth as you continue your Python learning journey.
