# Chapter 2 Notes

This is lecture note for Chapter 2.

## 2.1 Variable and Assignment

### 2.1.1 Why variable?

You can use string literals and number literals to run some tasks. Number literals are integers (such as `5`) or floats (such as `17.5`). For example: `print('Hi')` or `10 / 5`.

However, in many situations

- you don't know the values when you write the program. You need to read the data from a file or from a user input.
- When you define a function that consumes inputs and generates outputs, you need to refer to the input values and output values.
- Even you have the values used in computation, you still should give it a meaningful name to make the code easier to understand. For example, it is unclear what's the meaning of `17.5` and `5`.

You learned from middle school that algebra uses symbols to represent values and symbols are more powerful in solving problems than pure numbers. The variables in Python serves the same purpose.

### 2.1.2 What is a variable?

Variable is a name item (a container) used to hold a value. What’s a variable in computer? Memory address.

A variable is a name that represents a value stored in the compute memory (RAM).

### 2.1.3 Assignment

You use an assignment statement to bind a value to a name -- also called variable declaration or variable definition:

`variable = expression`

In this statement:

- `variable` is the name of the variable. The name must be in the left hand side (LHS) of the statement.
- `=` is the **assignment operator**. It binds/defines the LHS name to a value. There is a space before and after the operator for better code format.
- `expression` is a value or an operation that produces a value. It is in the right hand side (RHS) of the statement.

![variable](images/variable.png)

Here are some variable declarations:

```python
# declare variables using value literals
name = 'Alice'
answer = 42
course_name = 'Programming in Python'

total_score = 17.5
number_of_courses = 5

# declare a variable using an expression
gpa = total_score / number_of_courses

print(gpa)
```

As you can see from the output, an assignment doesn't generate any visible output. It just binds a value to a name. The expression `total_score / number_of_courses` performs a division and the result is bound to the name `gpa`. It has the correct value of `3.5`.

The variable name must be on the left hand side (LHS). The right hand side (RHS) can be a value, an expression or another variable. The following statement is invalid Python code and generates `SyntaxError` when you run it.

```python
3.5 = gpa
```

You cannot use a variable without defining it using an assignment statement first. You will get a `NameError` for `x + 1` if `x` is not defined before and your code crashes.

## 2.2 Identifiers

According to the [Two hard things blog](https://martinfowler.com/bliki/TwoHardThings.html):

> There are only two hard things in Computer Science: cache invalidation and naming things.
>
> -- Phil Karlton

It might be exaggerated, but naming is really one of the most important decisions in programming. You should think hard to give a variable the most meaningful name thus you and other people can understand the value behind it.

Python has simple but strict rules for variable names:

- A name must be started with a letter in the range of `a` through `z`, or `A` through `Z`, or an underscore character `_`.
- The rest of the name can be any letters in the range of `a` through `z`, `A` through `Z`, 0 through 9, or an underscore character `_`.
- The variable name is case sensitive. `score`, `scorE` and `Score` are all different names.
- Python keywords such as `if`, `for` cannot be used as variable names because they have special meaning.

`x`, `x9`, `_proxy`, `__all__`, `i18n`, `ohmygod`, `course_name` are all valid names because they obey the naming rules. However, `9x`, `42`, `@name`, `My**key`, `price$` are invalid names because they don't start with a valid letter or have invalid letters in the name.

### Multi-word Names

As you can see, names such as `studentname`, `roomnumber` are clumsy to read and write. Programmers use special terms to describe the multi-word naming mechanism:

- `snake_case`: use underscore to separate each lower case word. It is recommended for naming multi-word variables and source code files in Python.
- `kebab-case`: use a dash to separate lower case words.
- `PascalCasing`: each word starts with an uppercase letter.
- `camelCasing`: only the first word start with a lower case letter, others start with an uppercase letter.

Python uses underscore letter `_` to separate words in names. The naming conventions are defined in [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

### Magic Numbers

A number literal such as `3.1` in an operation such as `3.1 * diameter` is called a **magic number** because it is hard to know the meaning of these numbers. Python style guide recommends constants are

> written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

You should avoid using number literals in your code. Whenever it appears, give it a name. For example,

```python
INTEREST_RATE = 0.072
balance = 100
interest = balance * INTEREST_RATE
```

Another benefit of defining constant variables is that you only need to change one place and all its usage will be changes. For example, if the Pi value is used in many places and you define it as `PI = 3.1`. Later you want to use the value of `3.14`, you only need to change the definition as `PI = 3.14` in one place. It is called **single point of control**.

## 2.3 Objects

An object represents a value and is automatically created in memory by the interpreter when executing a line of code. This is a different perspective of values.

Deleting unused objects is an automatic process called **garbage collection** that helps to keep the memory of the computer less utilized.

**Name binding** is the process of associating names with interpreter objects.

Each Python object has three defining properties: value, type, and identity.

- Value: A value such as "20", "hello", or 55.
- Type: The type of the object, such as integer or string.
- Identity: A unique identifier that describes the object.

The most important concept for type is that a type has a certain set of operations.
