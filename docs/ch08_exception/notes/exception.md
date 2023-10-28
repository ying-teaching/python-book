# Exception

- Two Error Types
- Traceback
- Error Handling Strategy
- `try` Statement
- `else` and `finally`
- `raise` Exception

## Two Kinds of Errors

Python has two kinds of program errors: syntax errors and exceptions.

- Syntax Error: the program violates the Python grammar.
- Exception: The program grammar is correct but has other errors that Python cannot run the program.

### Syntax Errors

When you learn Python, you often make many syntax errors because you are not familiar with the Python syntax (grammar). Typos and incorrect grammars are common reasons for syntax errors.

```python
for element in [1, 2, 3] # Expected :
    print(element)

iff 6 > 5: print('hi') # unknown identifier iff

```

### Exception Error

Even if all statements in a program are syntactically correct, Python may still fails to execute the program because something is wrong.

These execution time errors are called `exceptions`, `runtime exceptions` or `runtime errors`.

When an exception happens and you don't handle it, the program crashes with an error message printed.

### Common Exception Types

- `ZeroDivisionError`: divide by zero exception.
- `NameError`: unknown variable identifier or function names, most likely cause by a typo.
- `ImportError`: unable to import a specified module.
- `AssertionError`: the boolean expression in an `assert` is false.
- `FileNotFoundError`: unable to find the specified file when read a file.
- `ValueError`: the value data is not expected. For example, unable to convert a string `"abc"` to an integer because the string value is not a valid number.
- You can find more exception in [exception document](https://docs.python.org/3/library/exceptions.html).
- User defined exception types.

### Exception Example 1

In Python, a statement **`raises`** an exception when something is wrong in execution. The code after the statement is not executed.

```python
dividend = 42
divisor = 0
quotient = dividend / divisor
print(quotient)

```

The statement `dividend / divisor` is syntactically correct. However, dividing by 0 is undefined in math therefore a `ZeroDivisionError` happens. Python prints a message `ZeroDivisionError: division by zero` and stops execution at the statement that causes the exception.

### Exception Example 2

If you don't define a `prin` function, the following syntactically correct function call statement raises an exception:

`prin("hi")`

The `prin("hi")` statement raises a `NameError` exception because it could't find the the function named `prin` -- in this case it might be a typo for the built-in function `print`.

## Traceback

A non-trivial Python program usually has many functions. Starting from the `main` function, a function calls one or more functions that call other functions, and so on and so forth. The calls are represented like a call stack where a caller is below the called function.

An exception might be raised deeply in a function call. Python tries to give a list of functions involved in the exception, from the top most function to the exception location.

Because the trace message shows the call stack in a reverse order, it is called **traceback**.

```python
def multiplyBy7():
    # it may get this string from a file or user input
    number_str = "Six"
    number = int(number_str)

result = multiplyBy7()

```

### Stack Trace Message

```text
ValueError        Traceback (most recent call last)
exception.ipynb Cell 12 line 6
      3     number_str = "Six"
      4     number = int(number_str)
----> 6 result = multiplyBy7()

exception.ipynb Cell 12 line 4
      1 def multiplyBy7():
      2     # it may get this string from a file or user input
      3     number_str = "Six"
----> 4     number = int(number_str)

ValueError: invalid literal for int() with base 10: 'Six'
```

## Error Handling Strategy

Because an exception represents a runtime error, the best error handling strategy is to avoid exceptions. If you design a program carefully, you can avoid many exceptions thus there are no need to handle them.

For example, to avoid `ZeroDivisionError`, check the divisor first before a division computation. If the divisor is zero, display an error message and ask the user to correct the problem.

To avoid `FileNotFoundError`, check the existence of a file before read from it. Following is a code example.

```python
import os

READ_MODE = 'r'

filename = input('Please type the filename: ')

if os.path.isfile(filename):
    with open(filename, READ_MODE) as file:
        print(f'Process {filename}')
        # process the file content here
else:
    print(f'{filename} is not a valid file, please check that you input the correct filename.')

```

### For Unexpected

You should avoid runtime errors if possible.

Sometimes it is hard to check a runtime error or to display user-friendly error message, you can use the built-in exception handling mechanisms.

## The `try` Statement

Python's `try` statement allows you to enclose a code block and to catch/handle specific or all exceptions in its `except`/`else`/`finally` clauses. With `try` statement, you can:

- Catch all exceptions
- Catch a specific exception type
- Catch multiple exception types
- Only execute some statements if no exception raised
- Execute some statement regardless of exception raised or not

## Built-in Exception Handling

When an exception raise in a statement, Python handles it as the following:

- if the statement is in a `try` statement, Python uses its `except` clause to handle the exception.
- if there the statement is not inside a `try` statement or the exception doesn't match the `except` clause, Python checks the call stack to find if any caller function has a matched `try` statement.
- if no caller function handles the exception, Python stops the program and prints traceback error message. This is a so-called **crash**.

### Catch All

A `try` statement has a `try` clause and an `except` clause.

Below the `try:` clause, you can write statements in a code block that is protected by the try-clause.

The statements in the `except` clause will be executed when an exception is raised in the protected clause.

If there is no exception in the try-clause code block, the except-clause is skipped.

```python
try:
    # all statements in this block is protected
    print('test exceptions')
    1 / 0 # raise an exception
except:
    print(f'Unexpected exception, blame its developer.')

```

### Catch One Type

You can only catch a specific type of exceptions in the except-clause. You can have an optional `as variable_name` to bind the caught exception instance to a variable.

If there is an exception raised, Python will check if the exception matches with the exception type specified in the `except ExceptionType as variable_name:` clause. If there is a match, the code block in the except clause will be executed. Otherwise, the exception is uncaught and Python uses its built-in exception handling mechanism.

```python
FILENAME = 'test.txt'

try:
    with open(FILENAME) as file:
        pass # process file data here
except OSError as error:
    print(f'Unable to open file {FILENAME}. Error message: {error}')

print('After the handling code, program keeps running')

```

### Optional `as`

A file cannot be opened for many reasons: not found, no permission, time out errors etc. The `OSError` can be used to catch these errors and display a user friendly message. If you don't need the error message, you can ignore the `as variable_name` in the except clause. The code will be the following:

```python
FILENAME = 'test.txt'

try:
    with open(FILENAME) as file:
        pass # process file data here
except OSError:
    print(f'Unable to open file {FILENAME}')

```

### Catch Multiple Types

If the code block in a try-clause has many operations, it could raise many different exceptions. You can use multiple except-clause to catch different exception types.

```python
try:
    # all statements in this block is protected
    number_str = "abc"
    number = int(number_str)
except OSError as error:
    print(f"Unable to process {number_str}. Error message: {error}")
except ValueError:
    print(f"Value error message")

```

### Catch Multiple Types and All

Often the error handling is a mix of catching specific types and a catch-all.

The order matters. Python will try to match the exception sequentially.

You can use `sys.exc_info()` to get error information.

```python
import sys

try:
    # all statements in this block is protected
    print('test exceptions')
    1 / 0 # raise an exception
except OSError as error:
    print(f'Unable to open file {FILENAME}. Error message: {error}')
except ValueError as error:
    print(f'Value error message: {error}')
except:
    error = sys.exc_info()[0] # to get error info
    print(f'Unexpected error: {error}')

```

## `else` and `finally`

In addition to catching exception, you want to run some statements for two scenarios:

- if there is no exception: for example, write to success message only if there is no exceptions.
- regardless of exception raised or not: it is very common that you want to do some cleanup tasks regardless no matter an exception is raised or not. For example, you should always close a file after use.

```python
try:
    print('normal code, no exception.')
    1 / 0
except:
    print('skipped if no exception.')
else:
    print('executed when there is no exception.')
finally:
    print('always execute the finally code block.')

```

## `raise` An Exception

Python allows you to raise an exception if your code couldn't continue due to some run-time errors.

If you cannot find an appropriate built-in exception type for the error, you can define customized exception classes.

For example, in a division computation, you detect a divisor is `0` or an invalid number string, you may want to raise an exception because the program cannot run with this input.

```python
def demo(count):
    if count == 0:
        raise ValueError("The count cannot be zero")
    else:
        # continue process
        ...

```

### Customize Exception

You define an exception type for an application-specific error. If you write a library used by other code, it is often a good idea to define customized error type to hide the implementation details.

You should define a subclass of `Exception` for exception types. The type should have the `Exception` as its name postfix.

For Example, if the correct argument must be positive in your function, you can define an exception type for error values not in the range.

```python
class PositiveException(Exception):
    """ The value should be between One and Ten inclusive """

    def __init__(self, message = "Value must be positive"):
        self.message = message
        super().__init__(self.message)


def demo(count):
    if count <= 0:
        raise PositiveException()
    else:
        # continue process
        ...

demo(-1)

```

## Summary

As a beginner programmer, you need to understand the `try` statement and read other people's code.

When you gain more experience, you will use it more.

Nonetheless, the best exception handling strategy is

- check the possible errors to avoid exceptions.
- if you don't know how to handle an exception in a function, ignore it.
- catch all exceptions in UI code to give user-friendly error message. For API, wrap an exception to hide internal implementation details.
