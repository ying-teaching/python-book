# Function

- What and Why
- Function Definition
- Function Call
- Functions and Methods are Objects
- Variable Scope
- Call Stack
- Recursive Function

## What is a Function

A function is a group of statements that performs a specific task. Though there is no limit in the number of statements that you can write inside a function, it is important that a function consists of a group of closely related statements to serve a single purpose. It will make your code easy to read and maintain.

## Why Function?

Programmers use functions primarily for two purposes

- to reuse code
- to organize code

When you define a function, it can be used in many places. Code reuse improves productivity and quality because you only need to write and maintain a single copy of the function.

Organization is about divide and conquer. Instead of writing a long list of statements of a complex application, you can divide the application into a set of subtasks such that each task is relatively easy to be solved.

### Divide and Conquer

In the following diagram, instead of a long list of statements on the left, you can organize statements into a set of functions that each function perform a single subtask. It helps you to design the program because at one moment you only need to solve a relatively simpler subtask.

![subtask](../images/subtask.png)

### An Example of Divide and Conquer

| A list of statements                                                                                                                                                                                                                                                  | Statements in Functions                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1. unplug from charger <br> 2. walk to the house door <br>3. open the house door <br>4. walk out the house door<br>5. close the house door<br>6. walk to the car<br>7. open the car door<br>8. sit in the car<br>9. close the car door<br>10. drive the car to school | 1. leave home (this function has the statements 1 to 5)<br><br>2. go to school (this function has the statements 6 to 10) |

### Function Benefits

- Small tasks are easy to write, easy to test/debug, and easy to maintain.

- The function version is also easy to share, you can share both small tasks in different situations.

- Another big benefit is that a function name summarizes the task. It is easy to understand the two function calls by their names if you don't care about the implementation details. You can image the pain when you have to figure out the purpose of 1,000 lines of code.

- Furthermore, it is easy to replace a function with a new function that implements new method. For example, one can take a Uber or ride a bicycle for the 2nd task, either can achieve the goal of going to school.

### Multiple Levels

If a subtask is too complex, you can divided it into a set of subtasks again. A function represents a subtask can be be divided into more functions. Eventually you may have a program structured as the following:

![structure](../images/structure.png)

The structure is a payroll application. You can see the five subtasks at the first level. The first function and the third function uses two other functions to perform their tasks. If you replace all functions with their statements, it will be a big mess and it is hard to figure out the purpose of a list of detail operations.

Therefore divide and conquer using functions let you deal with easy-to-solve subtasks. It also makes the program structure easy to understand.

### Don't Repeat Yourself (DRY)

An important principle in programming is Don't Repeat Yourself (DRY). Function reuse not only reduces the number of statements, it also make it easy to change the code in one place. If there is a bug in a function, you only need to fix the function definition in one place and all function calls use the revised version.

There are many other benefits in testing, collaboration etc. Following is an example that three systems share a function.

![reuse](../images/reuse.png)

## Defining a Function

The syntax to define a function is rather simple in Python. Following are examples of function definitions.

```python
# define a function: no parameter, no return value
def function_name1():
    """Document for this function."""
    # statement
    # statement
    ...
```

```python
# define a function: two parameters, no return statement
# returns None as default value
def function_name2(parameter1, parameter2):
    """Document for this function."""
    # statement
    # statement
    ...
```

```python
# define a function: two parameters, has a return value
def function_name3(parameter1, parameter2):
    """
    Summary for this function followed by a blank line.

    Detail description about the input, process and output
    of the function.
    """
    # statement
    # statement
    ...
    return ...
```

### Function Header

The first line is the `function header`. It begins with the keyword `def`, followed by a function name, an optional list of parameters enclosed in parentheses, and ends with a colon. Below is an example:

`def function_name3(parameter1, parameter2):`

### Function Name Rules

Python has a set of identifier rules and recommended styles for function names. Python uses so called _Python Enhancement Proposal (PEP)_ to define language features and recommended practices. [PEP8](https://peps.python.org/pep-0008/) defines style guide for Python code.

- A function name must be an valid identifier.
- Python suggests snake_casing as function name: lower case words separated by an underscore.
- It is a best practice to use a verb or a verb pluses a none for a function name. For example, `prepare`, `do_homework`, `print_message`.

### Function Parameters

A function header may have zero, one, or more `parameters` enclosed in parentheses. If there is no parameter, the function header just has a pair of parentheses. If there are two or more parameters, they are separated by a comma `,`. In the above function headers, they are:

- `function_name1()`
- `function_name2(parameter1, parameter2)`
- `function_name3(parameter1, parameter2)`

You can have as many parameters as you want, but it is not a good idea to have more than five parameters. You way want to split your function into small functions or compose parameters when there are too many parameters.

Similar to the naming of variables and functions, you should give meaningful names to the function parameters because they are used as variables in the function code.

### Default Argument

When you call a function, you pass values to the parameters. These values are called `arguments`. Python supports `default argument`. You can define default values for parameters. In function definition. The default arguments must be at the end of the parameter list.

When a function has a default argument, during a function call you can use the default argument or pass a new value. For example:

```python

def greet(first_name, last_name, prefix='Hello'):
    print(f'{prefix} {first_name} {last_name}')

greet('Alicia', 'Keys')
greet('Bob', 'Dylan', 'Hi')
```

### Positional Argument

Normally, arguments are passed to functions based on their position and without parameter names are called `positional arguments`. The following calls use positional arguments.

```python

def greet(first_name, last_name, prefix='Hello'):
    print(f'{prefix} {first_name} {last_name}')

greet('Alicia', 'Keys')
greet('Bob', 'Dylan', 'Hi')
```

### Keyword Argument

You can use parameter names when you call a function with some arguments, these are called _keyword arguments_. It let you specify arguments in any order.

However, if you mix positional arguments and keyword arguments, you must specify positional arguments first.

```python

def greet(first_name, last_name, prefix="Hello"):
    print(f"{prefix} {first_name} {last_name}")

greet(first_name="BoB", last_name = "Dylan")
greet("Bob", prefix="hi", last_name = "Dylan")
```

### Five Parameter Types

- positional-or-keyword: this is default and the most common parameter type. An argument passed positionally or as a keyword argument. For example: `def greet(message, name='alice')`
- var-positional: prepending a `*` with a parameter makes it _variable positional parameter_. It can take an arbitrary sequence of positional arguments. For example: `def func(foo, *args)`.
- var-keyword: prepending the `**` with a parameter makes it _variable keyword parameter_. It can take an arbitrary sequence of keyword arguments. For example: `def func(foo, **kwargs)`.
- positional-only: you can specify that arguments can only be passed by position, i.e., cannot be a keyword argument, by putting a `/` in a function definition. For example, `def func(pos_only1, pos_only2, /, positional_or_keyword): ...`
- keyword-only: putting the `*` to mark following parameters are keyword-only. For example: `def func(arg, *, kw_only1, kw_only2): ...`.

### Var-Positional and Var-keyword Parameters

You often need var-positional and var-keyword parameters because it makes the code very flexible.

For example, the built-in `print()` function can print an arbitrary sequence of values.

You will see more examples.

### Function Body

The **function body** is the code block indented (4 spaces, per Python coding style) below the function header. The statements in the function body are just regular statements. You can use all control statements (`if`, `for`, and `while`) in the function body.

A non-indented statement below the function header marks the end of the function body. You should use a blank line separate a function and the statements before and after it.

For example:

```python
def greet(name, prefix = 'Hello'):
    '''Greet with a prefix and name'''

    print(prefix, name)

print('Done')

```

### Docstring for Functions

Except for trivial functions, you should write a docstring for the function. It can be a single line doc string, as shown in the above examples, or it can be a multi-line doc string: a summary line, followed by a blank line and detail description.

Docstring format is defined in [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/). The following is an example from the document.

```python
def complex(real=0.0, imaginary=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imaginary -- the imaginary part (default 0.0)
    """

    if imaginary == 0.0 and real == 0.0:
        return 0
    ...
```

### Empty Function Body

When you design a program, you divide your application into several functions but don't know the implementation details for some of you functions. You can use the `pass` keyword or `...` value as a temporary function body to write a **function stub** -- you can also print a message or return some value in the stub. You replace it with real code when you are ready to implement it.

```python
# recommended
def do_homework():
    pass

def do_homework2():
    ...

def do_homework3(): ...
```

### Returning Value

Some functions perform operations without returning a value, they are called `void functions`. The `void` means **nothing**. A function that only prints a message is a void function. The function `exit()` takes no argument and is a void function. It exits the program execution.

Many functions perform some computation and return a value as its result. These are `value-returning` functions. You use the `return expression` in a function to return a value and complete the function. A function body may have multiple `return` statements. Following are two examples of function definition.

```python
def add(number1, number2):
    return number1 + number2


# ugly but works
def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False

    # unreachable statement
    print('unreachable')

# Actually, the above code is not a good example because `number % 2 == 1` is a boolean expression and can be returned directly.
# isOdd can be simplified as:

def isOdd(number):
    return number % 2 == 1
```

### Returning Multiple Values

It is possible to return multiple values using the `return` statement. You list the variables to be returned after the `return` keyword and use `,` to separate the multiple values. The statement `return first, second` actually returns a data type of `tuple`.

The following is an example:

```python
def get_name():
    first = input('First name? ')
    second = input('Second name? ')
    return first, second

first_name, second_name = get_name()

print(first_name, second_name)
```

## Function Call

To use a function is to `call` a function. To call a parameterless function, append parentheses to the function name.

To call a function that has parameters, you need to pass an argument for each parameter in the parentheses, in the same order as they are defined. These arguments are called `positional arguments`.

You can also use the parameter name to pass an argument to the function call. This is a so-called `keyword argument`. You don't need to follow the order as defined in the function header. The keyword argument is helpful when there are several parameters and you want make them more readable.

Following are some examples:

```python
def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}')

# positional arguments
greet('Alicia', 'Keys')

# keyword arguments, the order doesn't matter
greet(first_name='Alicia', last_name='Keys')
greet(last_name='Keys', first_name='Alicia')

```

### Keyword Arguments are After Positional Arguments

If you use a keyword argument, it must be after positional arguments.

```python
def greet(first_name, last_name, prefix='Hello'):
    print(f'{prefix} {first_name} {last_name}')

greet(prefix='Hi', first_name='Elton', last_name='John')
greet('Alicia', prefix='Hi', last_name='Keys')
```

### Variable Positional Argument

Inside a function call, the var-positional argument, often named as `*args`, is a tuple that support two common operations of a tuple:

- iterate using `for item in args`
- unpack using assignment: `val1, val2, *rest = args`. Here `*rest` is a tuple that has the rest of elements in `args`.

You can pass a number of arguments.

Alternatively, you can pass a list, a tuple, or any sequential object as the argument of `*arg`. However, you need to put a `*` before the object.

```python
# here the number is a mandatory argument
# followed by a var-argument args
def average(number, *args):
    size = len(args) + 1

    if size >= 3:
        v1, v2, *rest = args
        print(f"first two: {v1}, {v2}")

    return (number + sum(args)) / size

# call with a single argument
# *args is an empty tuple ()
result = average(7)
print(result) # 7.0

# call with multiple arguments
result = average(2, 20, 30, 40)
print(result) # 23.0

numbers = [4, 5, 6]
# call with a list
# be careful to put * before a sequence (list)
result = average(*numbers)
print(result) # 5.0

numbers = 7, 8, 9
# call with a tuple
# be careful to put * before a sequence (tuple)
result = average(*numbers)
print(result) # 8.0
```

### Variable Keyword Argument

Similarly, inside a function call, the variable keyword argument, often named as `**kwargs`, is also a tuple that support iteration and unpacking. However, each item is a tuple of `(keyword, value)`.

- iterate using `for keyword in kwargs` or `for key, value in kwargs.items()`
- unpack using assignment: `(keyword1, value1), (keyword2, value2) = args`

You can pass a number of keyword arguments.

Alternatively, you can pass a dictionary as the argument of `*arg`. However, you need to put a `**` before the dictionary object.

```python
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(
            name1="Alice",
            name2="Bob",
            name3="Cindy",
            name4="David",
        )

## use a dictionary argument
names = {"name1": "Alice", "name2": "Bob"}
print_values(**names)
```

## Functions Are Objects

A function is an object that has a type (class `function`), an identity (the function name) and a value (the definition of the function).

As an object, it can be assigned to another variable or can be passed as an argument in function call.

A function takes another function as its parameter is called a **high-order function**. The name is fancy but the concept is rather simple.

### A High-Order Function Example

The following is an example of higher-order function. Python's `map` function takes a function as its first parameter and a list as the 2nd parameter. The result is a `map` object that can be converted into a list using `list(m)`.

Be careful that you use `double`, not `double()` in `map`. `double()` is a function call -- it is invalid because it misses its argument.

```python
def double(num):
    return num * 2

items = [1, 2, 3]
list(map(double, items))

# this also works
operator = double
list(map(operator, items))
```

### Methods are Function-like Objects

When you bind a function with a specific data type, it becomes a method. It helps organize functions into a group of operations that are closely related to a data type. Method is an object-oriented programming concept that will be covered later.

For now, it is enough to know an important difference between a method and a function:

- You call a function using a function name followed by arguments in a pair of parentheses `function(arg1, arg2)`
- You call a method using a dot notation like `my_object.method(arg1, arg2)` because the function is bind with some object `my_object`. Conceptually, you can think `my_object.method(arg1, arg2)` as `method(my_object, arg1, arg2)` -- the `my_object` is always the first argument for a method.

### The `main` Function

There is a convention in Python coding: you want to use the `main` function name as the entry point of a program. A non-trivial program has many functions, however, there must be a function working as the entry point of the program.

The `main` contains the mainline logic of a program that calls other functions to perform top level tasks. Each top level task may call other functions to perform subtasks. Following is an example of function organization.

![structure](../images/structure.png)

### An Application Example

You should use `main` as the entry of your program as the following - it shows that you can use a function in a function body and define it later.

```python
def main():
    number = 42
    print_triple(number)

def print_triple(number):
    triple = number * 3
    print(f'Triple of {number} is {triple}.')

main()
```

## Variable Scope

Every Python variable has a scope -- it is only visible in the region it is defined. Python has three scopes:

- Built-in scope: Python has some built-in names such as `int()`, `str()`, `list()` etc.
- Local scope: variables in a function. There are many local scopes because there are many functions.
- Global scope: variable outside any function.

Python use a dictionary for each scope. Such a dictionary is called a **namespace** but it is an implementation detail that you can learn more in the future.

### Local Variable

A variable defined inside a function can be used in the function after it is defined. This is called a `local variable`. The function is the scope of the local variable. Outside the function, it is invisible and cannot be used.

The function parameters are also local variables. You can use them inside the function as locally defined variables. Assigning a parameter to another value doesn't affect the corresponding argument.

### A Local Variable Example

In the following code, the `number` in `main` is a local number and is passed to `print_triple` function. Inside the `print_triple` function, the `number` is a local variable -- a totally different one from the `number` in `main`. The program assigns it to a different value of `126`. In the `main` function, it still has a value of `42`.

```python
def main():
    number = 42 # a local variable
    print_triple(number)
    print(f'The number in main is {number}')

# the number parameter is in a different namespace
def print_triple(number):
    number *= 3
    # you shouldn't change the parameter to avoid subtle bugs
    print(f'Tripled number is {number}')

main()
```

### Global Variable

A variable defined in the main body of a file, i.e, not defined in a function, is called a `global variable`. It is visible and accessible to all statements inside or outside the functions.

Because a global variable is shared by all functions, you should not define and use global variables in your program because it is hard to tell where it is changed. The only reasonable situation for global variable is to define constant values that is shared by all function.

```python
PI = 3.1416

def main():
    radius = 42
    print_area(radius)

def print_area(radius):
    area = radius * radius * PI
    print(f'The area is {area: .2f}')

main()
```

### Control Statements Don't Create a Namespace

The scope for variables defined in control statements `if`, `for` and `while` is its enclosing function.

If they are not defined in a function (very rare), they are in the global scope. Below is an example where the `number` is created in the `for` loop but its scope is the `main` function. Therefore it can be used by the `print(number)` statement in the `main` function.

```python
def main():
    for number in range(3):
        print(number)

    print(number)

main()
```

## Call Stack

Usually your program has a entry point function and the function calls other functions which call more other functions. When a function calls another function, Python interpreter saves the status of the current function in a data structure called a **call frame**, then executed the callee function.

Similarly, the callee function may call another function and more and more, eventually, we have a so-called call stack.

![call stack](../images/call-stack.png)

```python
def foo():
  x = "foo"
  print(f"foo line 2. x is {x}")
  print("foo line 3")
  print("foo line 4")

def fum():
  print("fum line 1")
  print("fum line 2")
  print("fum line 3")

def bar():
  x = 21
  print(f"bar line 2. x is {x}")
  fum()
  foo()
  print(f"bar line 5. x is {x}")

def main():
  x = 42
  bar()
  print(f"main line 3. x is {x}")

main()
```

### An Example of Call Frames

The `main` function calls the `bar` function that calls three more functions: `print`, `fum`, `foo`.

When the `bar` calls `foo`, there are three functions in the stack: at the bottom, `main`, then `bar`, then, at the top, `foo`.

You can debug the code to see the call stack. When a function returns, its call frame is popped up from the stack and its caller becomes the top function in the call stack.

The variable `x` is a local variable in its function scope and may have different values at different time.

## Recursive Function

A function calls itself with different (usually smaller) arguments is call a recursive function.

All loops (iterations) can be coded with recursive functions. Actually some programming languages only have recursive functions for iteration.

There are cases where recursive functions are easier to write and maintain then loops. Sometimes, the difference is not clear.

Similarly to loops, it is critically important to define the termination conditions. Usually termination conditions are checked at the beginning of a recursive function.

```python
# the recursive version
def count_down(number):
    if number == 0:
        print('Done.')
    else:
        print(f'Count {number}')
        count_down(number - 1)

count_down(3)


# the loop version
def count_down2(number):
    for current_number in range(number, 0, -1):
        print(f'Count {current_number}')

    print('Done.')

count_down2(3)
```
