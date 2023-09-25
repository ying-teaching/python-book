# Loop

- `while`
- `for`
- Break and Continue
- Two Examples

## `while` Loop

This section introduces the concepts of `while` statement and infinite loop.

- The Concept
- The Statement
- Infinite Loop
- Sentinel

### The `while` Concept

It it a common scenario that you repeat some actions when a certain condition is true.

- You repeatedly "learn" while a topic that puzzles you.
- The rice cooker "cooks" rice for 30 minutes.
- Your program keeps asking a user to give an input if the current input is invalid.

The following diagram shows the concept.

![while](../images/while.jpg)

### The `while` statement

As depicted in the above diagram, the `while` statement has a `while` clause and a code block. The syntax is as the following:

```python
while condition:
    statement
    statement
    ...

statement // after-while statement
```

When the condition is true, it repeatedly executes the statements in the code block. Each execution of the loop body (code block) is called an **iteration**. Looping is also called **iterating**. If the condition becomes false, it skip the code block and runs the statements below it. Below is an example:

### Initial Value

Because the `while` clause first checks a condition, the code needs to set a certain value make the condition `True`. Below we set the confirmation to `'yes'` thus when Python executes the `while` statement, the condition is `True` and the statements in the code block are executed. When the confirmation input is not `'yes'`, it skip the code block and run the statement(s) below the `while` statement.

```python
# a program to calculate the total of user inputs
total = 0
confirmation = 'yes'

while confirmation == 'yes':
    number = int(input('Please input an integer: '))
    total += number # += is an abbreviation of total = total + num
    confirmation = input('more numbers? yes for continue, otherwise stop.')

print(f'The total is {total}')

```

### Infinite Loop

It is very important to change the condition in the code block of a `while` statement. Following is a program that we want to calculate the sum from 1 to 10.

```python
total = 0 # don't use sum as the variable name because it is a built-in function name
number = 1
while number <= 10:
    total += number

print(f'The total from 1 to 10 is {total}')
```

If you run the above code, it never ends until the system fails to handle a big number or doesn't have enough memory. The program enters an infinite loop. The reason is the the `while` clause is always evaluate to `True`. To fix it, you should change the condition in the code block.

### Remember to Change Condition

Whenever you write a `while` statement, remember to change the condition inside the code block to avoid infinite loop.

```python
sum = 0
number = 1
while (number <= 10):
    sum += number
    number += 1

print(f'The sum from 1 to 10 is {sum}')
```

### Sentinel

The `while` clause checks a boolean expression to control the iteration. If you use a variable value to represent the `completion`/`end`/`stop` case, the value is called a _sentinel_. It is important that a sentinel should not be a normal input value, otherwise the program can not tell the special end value from normal values. For example, if a program asks user to input positive numbers, it can use `-1` to mark the end of the while loop.

```python
# a program to calculate the total of user inputs
total = 0
number = int(input('Please input a positive number, input -1 to stop: '))
while number != -1:
    total += number # += is an abbreviation of total = total + num
    number = int(input('Please input a positive number, input -1 to stop: '))

print(f'The total is {total}')
```

### Exercise-1

In the above sentinel code example, the prompt message is repeated before and after `while`. Please change the code to call the `input` function only in one place.

### Exercise-2

The following code runs an infinite loop, can you tell what's wrong? Try to fix it.

```python
total = 0
confirmation = 'yes'

while confirmation == 'yes':
    number = int(input('Please input an integer: '))
    total += number # += is an abbreviation of sum = sum + num
    confirmation2 = input('more numbers? yes for continue, otherwise stop.')

print(f'The total is {total}')
```

## The `for` Loop

- Concept
- Statement
- Nested loops
- Range function
- Enumerate with Index

### The `for` Loop Concept

Like the `while` loop, the `for` loop has two parts: a `for` clause and a code block.

The `for` clause gets each element from a `sequence`, assigns each item to an variable and execute the code block. It completes when there is no more elements in the sequence.

The variable used in the `for` clause is called a `target variable` because it is assigned the value of each element in the sequence in each loop iteration. It is important to give it a meaningful variable name.

Conceptually, it works as the following flow chart:

![for](../images/for.jpg)

### The `for` Loop Syntax

The syntax of `for` loop is as the following:

```python
for variable_name in sequence:
   statement
   statement
   ...
```

Following are two examples that print out elements in a sequence -- you use the target variable to access each element:

```python
students = ['Alice', 'Bob', 'Cindy']
for student in students:
    print(student)
print('All students are printed\n')
```

### Nested Loop

In the code block of a loop statement, you can have another loop statement, this is called nested loop. Conceptually it is rather simple, just treat the nested loop as a regular statement and everything becomes clear. Following is an example. As you can see, the inner `for char` loop is repeated for each number in the outer `for number` loop. Practice more and you will have a better understanding.

```python
numbers = [1, 2, 3]
chars = ["A", "B", "C"]

print('Outside loop')
for number in numbers:
    print('Inside number loop')
    for char in chars:
        print('Inside char loop')
        print(number, char)
```

### Exercise

Exercise: change the following `for` loop code to use `while` loop.

```python
students = ['Alice', 'Bob', 'Cindy']
for student in students:
    print(student)
print('All students are printed\n')
```

### The `range` Function

Many time you want to repeat a block code for a number of times. Python has a built-in function `range` that generates a sequence of numbers.

`range(n)` generates a sequence of integers in the range of `0` up to, but not including, the number `n`. For example, `range(3)` generates a sequence of `0`, `1` and `2`.

```python
for item in range(10):
    print(f'Current item: {item}')
```

### More Parameters

The range function can take one, two, or three arguments.

- `range(m, n)`: generate a sequence of integers in the range of `m` up to, but not including, the number `n`. For example, `range(3, 7)` generates a sequence of `3`, `4`, `5`, and `6`.
- `range(m, n, step)`, generate a sequence of integers in the range of `m` up to, but not including, the number `n`, the generate numbers increase at the specified step. For example, `range(3, 7, 2)` generates a sequence of `3` and `5`. `7` is not in the generated list because numbers bigger than or equal to `7` are excluded.

It is possible to use a negative step in a `range` function to generate a list from high to low, in a reversed order. For example, `range(3, 0, -1)` generates a list of `[3, 2, 1]`.

```python
for item in range(3, 10, 2):
    print(f'Current item: {item}')
```

### The Index Idiom

You can compose the `len` and the `range` functions to generate a sequence of the index numbers for a list. For the above students list, the composed function `range(len(students))` generates a sequence of 0, 1 and 2.

Actually, it is an idiom in Python to use the composed function to access both the item and its index in a list. Following is an example to display students and there places in the list. For a typical business user, the index should starts from 1, not 0.

Using f-string, you can format the output as the following:

```python
students = ['Alice', 'Bob', 'Cindy']

for index in range(len(students)):
    print(f'Index {index}, Name: {students[index]}')
```

### The `enumerate` Function

When you need both the index and element value when iterating over a sequence, use `enumerate` function. In each iteration, it returns the current index and current value in a pair.

```python
students = ['Bob', 'David', 'Alice']

for (index, name) in enumerate(students):
    print(f'Index {index}: {name}')
```

### Which Version is Better?

What's the difference? To calculate the length of a list, you need load the whole list first into memory (_eager_ evaluation) while the `enumerate` process one element of the list at a time (_lazy_ evaluation).

Why the difference matters? In most cases, the lazy is better than the eager version because it

- starts quickly from the first element.
- requires less memory, just one element at a time.

```python
students = ['Alice', 'Bob', 'Cindy']

for index in range(len(students)):
    print(f'Index {index}: {name}')

for (index, name) in enumerate(students):
    print(f'Index {index}: {name}')
```

## Continue and Break

It is common that you don't want to perform a loop thoroughly. Two common cases are:

- Skip some statements in the suite
- Stop the loop before it completes

### The Continue Concepts

In the code block of a `for` or `while` loop, sometimes you want to skip the processing for certain data. For example, when you divide a number by every element in a list, you want to skip the `0` as a divisor because it crashes the program. You use the `continue` statement to continue to the next iteration of the loop. The following flow chart describes the continue control flow:

![continue](../images/continue.jpg)

### `continue` Statement

As stated above, you use `continue` statement in a certain condition to skip the current iteration and run the next iteration of the loop.

```python
dividend = 100
numbers = [3, 5, 7, 0, 9, 2]

for number in numbers:
    print(f'The element is {number}')
    if number == 0:
        print(f'oops, zero cannot be a divisor')
        continue

    quotient = dividend / number
    print(f'The quotient of {dividend}/{number} is {quotient: .2f}')

```

### The Break Concept

In another situate, in some conditions you want to exit the loop execution. For example, you read input from a user in a loop and the user types an `exit` to exit the loop. You use the `break` statement to break out of the loop. The following flow chart describes the break control flow:

![break](../images/break.jpg)

### The `break` Statement

Similar to the `continue` statement, you check a condition that you want exit a loop, if the condition is `true`, you use `break` to exit the loop and jumps to the next element after the loop structure.

```python
dividend = 100
numbers = [3, 5, 7, 0, 9, 2,]

for number in numbers:
    print(f'The element is {number}')

    # exits from the loop when it sees a `0`.
    if number == 0:
        print(f'oops, zero divisor, clean your data first')
        break

    quotient = dividend / number
    print(f'The quotient of {dividend}/{number} is {quotient: .2f}')

print('Done')
```

### Stop Loop with Sentinel

The following example stops when it the input is the sentinel value. It skips `0` to avoid division by zero error.

```python
SENTINEL = -1
dividend = 100
prompt = f'Please input an integer, input {SENTINEL} to exit: '

number = int(input(prompt))
while number != SENTINEL:
    print(f'The input number is {number}')
    if number == 0:
        print(f'Zero cannot be a divisor, ignored.')
        number = int(input('Please input an integer, input -1 to exit: '))
        continue

    # now the normal logic to process the data
    quotient = dividend / number
    print(f'The quotient of {dividend}/{number} is {quotient: .2f}')

    # must have code to change the number
    number = int(input(prompt))

print('Done')
```

### `while True:`

The code `while True:` looks weird if it is the first time you see it. It looks like an infinite loop because the condition is always true. For this clause, there must be a `break` statement in the code block to exit the loop at a certain condition. The code can be revised to get an input first and check the sentinel in the `while` clause. Following is a version that checks the sentinel in `while` clause.

```python
# a sentinel is a special value that marks the end.
SENTINEL = -1
dividend = 100

prompt = f'Please input an integer, input {SENTINEL} to exit: '
while True:
    number = int(input(prompt))
    print(f'The input number is {number}')
    if number == 0:
        print(f'Zero cannot be a divisor, ignored.')
        continue

    if number == SENTINEL:
        break

    # now the normal logic to process the data
    quotient = dividend / number
    print(f'The quotient of {dividend}/{number} is {quotient: .2f}')

print('Done')
```

### `while` Exercise

Exercise: write a program that prints the first 5 odd numbers from the list `[3, 8, 10, 5, 7, 0, 9, 2]`.

## Two Examples

- Factorial with `while` and `for`
- Draw spiral circles

```python
"""Calculate the factorial of a non-negative integer"""
number = int(input('Enter a positive number: '))

# calculate number!  factorial
factorial = 1

# 1 * 2 * 3 ... * number

# while loop is error-prone,
# - need variable to control the loop condition explicitly
# - often has missing-by-one bug or infinite loop
# index = 2
# while index <= number:
#     factorial *= index
#     index += 1

# for n in range(2, number + 1):
#     factorial *= n

# decremental
for n in range(number, 1, -1):
    factorial *= n

print(f'{number}! is {factorial}.')
```

```python
import turtle

# don't name the file a turtle.py -- it causes a name conflict error.

# Named constants
NUM_CIRCLES = 36  # Number of circles to draw
RADIUS = 100  # Radius of each circle
ANGLE = 10  # Angle to turn
ANIMATION_SPEED = 0  # Animation speed
COLORS = ["red", "green", "blue"]

t = turtle.Turtle()
t.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.
color_index = 0
for x in range(NUM_CIRCLES):
    t.pencolor(COLORS[color_index])
    t.circle(RADIUS)
    t.left(ANGLE)

    color_index += 1
    if color_index >= len(COLORS):
        color_index = 0

t.screen.mainloop()
```
