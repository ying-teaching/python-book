# Module

This section introduce the module concept, including its definition, why and how you use it.

## 1 Module: What and Why

A `module` is a Pyhon code file. Or you can say a Python file is a module. A module usually consists of a set of closely-related functions.

Python uses three constructs to organize an application:

- a funtion to group statements, in a source code file.
- a module to group functions in a Python source code file. One file is a module.
- a pacakge to group files, usually in one or more folders. A folder can be a package.

The reason is rather simple, putting all functions into a single file is not appropirate for big programs. Putting functions into diffrent files are easy to read/write and easy to collaborate. Packages are used to organize a large functional area. For example, all math functions or network requests.

## 2 Use Modules

To make it simple, we put all modules in the same folder. In real applications, you may want to use foders to organize files into packages. For beginners, a fold with multiple Python scripts files/modules should be enough to write a non-trivial program.

To use a module, you use `import module_name` to import a module. The module name is the Python script file name with the `.py` postfix. Then you can use `module_name.function_name` to call a function defined in the module.

For demo purpose, the following simple example uses several files to calculate an area of a circle.

```python
# constants.py
PI = 3.1416

# you can define many constants
```

```python
# circle.py
import constants

def area(radius):
    return radius * radius * constants.PI

def diameter(radius):
    return radius * 2

def circumference(radius):
    return diameter(radius) * constants.PI

# you can define many circle functions here
```

```python
# main.py
import circle

def main():
    radius1 = 3
    area1 = circle.area(radius1)
    print(f'area is: {area1: .2f}')

main()
```

Because a file is a module, if you Python file has a name such as `math`, then you cannot import the built-in `math` package. It is a common mistake made by beginners.

## 3 `from` and `import`

There is another way to import one or more specific functions using the `from moduel_name import function1, function2` statement. Once imported, these functions call be used without the module prefix.

For example, the `main.py` file can be written as the following:

```python
from circle import area, diameter

def main():
    radius1 = 3
    area1 = area(radius1)
    print(f'area is: {area1: .2f}')

    print(diameter(radius1))

main()
```

When you import a specific function, Python allows you to rename a function using the `as` keyword. For example: `from circle import area as calcuate_area`. Then you can use the renamed function name.

A wildcard syntax `from circle import *` allows you to use all functions defined in the `circle` module directly without the `circle.` prefix. Be careful because it may import too many functions. It is not recommended.

```python
# main.py
from circle import area as calcuate_area

def main():
    radius1 = 3
    area1 = calcuate_area(radius1)
    print(f'area is: {area1: .2f}')

main()
```

The feature is useful when there is a name conflict among different modules.

## 4 Import and Execution

When a module is imported, Python executes the statements in the module. For example, if you change the `constants.py` to the following:

```python
# constants.py
PI = 3.1416

print('PI is define')
```

Then the `import constants` will execute the two statemens: define a variable and print a message.

However, if you import a file multiple times, Python only executes it once.

## 5 Conditionally Execute `main`

In Python, it is common to define a `main` function in a module that is used to run testing code.

```python
# circle.py
import constants

def diameter(radius):
    return radius * 2

# for testing
def main():
    assert 6 == diameter(3)

main()
```

The `assert` is a Python keyword that checks the following boolean expression. If the expression is true, nothing happen. If the expression is false, it reports an error message. You often use an assertion when you want to test a function.

You want to run the `main` function in the command line but don't want to run the test code when a module is imported into another file. However, the above code will run `main()` when it is imported. What you need is a way to find out if a module is imported or is executed from a command line.

Python provides a mechanims to distinguish the two execution modes. When the Python interpreter processes a module, it creates a special variable named `__name__`. It is a convention in Python that variable names started with `_` or `__` are used by the system. The `__name_` has two possible values:

- If a module is imported by another module, its `__name__` has a value of the module name, i.e., the filename without the `.py` postfix. For example, if the `circle` module was imported, its `__name__` has a value of `circle`.
- If it is executed by Python interprete in command line, the `__name__` has a value of `__main__`.

Therefore we can change the above code as the following:

```python
# circle.py
import constants

def diameter(radius):
    return radius * 2

# for testing
def main():
    print('Test diameter function')
    assert 6 == diameter(3)

if __name__ == '__main__':
    main()
```

Try to run the file in a command line and import it from another module. You should see the test output in commandline but not in the imported file.

## 6 `random`, `math` and `statistics`

The `random`, `math` and `statistics` are commonly used built-in modules. You import them and call their functions.

### 6.1 `random` Module

Follwing are some commonly used functions in `random` module. Check the [`random` docuemnt](https://docs.python.org/3/library/random.html) for more functions.

- `random.randint(m, n)`: generate a random integer number between `m` and `n`, inclusively.
- `random.randrange(m, n)`: generate a random integer between `m` and `n-1`.
- `random.random()`: generate a random float number betwen `0.0` and `1.0`, exclusively.
- `random.random(x, y)`: generate a random float number between `x` and `y`, exclusively.
- `random.seed(n)`: set the random generator with a seed `n`. For the same `n`, it genereates a fixed sequence of numbers.

Below is an exmple:

```python
import random

MIN = 1
MAX = 6
SEED = 42

# after set a seed, it generates a fix sequnce in multiple run
# to see the difference, comment the following line and run multiple times
random.seed(SEED)

for count in range(10):
    number = random.randint(MIN, MAX)
    print(f'random number is {number}')
```

### 6.2 `math` Module

Follwing are some commonly used functions in `math` module. Check the [`math` docuemnt](https://docs.python.org/3/library/math.html) for more functions.

- `math.pi`: the mathematical constant π = 3.141592…, to available precision.
- `math.e`: the mathematical constant e = 2.718281…, to available precision.
- `math.sqrt(x)`: return the square root of `x`.
- `math.ceil(x)`: return the ceiling of `x`, the smallest integer greater than or equal to x.
- `math.abs(x)`: return the absolute value of `x`.

### 6.3 `statistics` Module

Follwing are some commonly used functions in `statistics` module. Check the [`statistics` docuemnt](https://docs.python.org/3/library/statistics.html) for more functions. The `data` parameter in the following examples is a sequence of data such as a list or a range.

- `statistics.mean(data)`: the mean of data.
- `statistics.median(data)`: the median (middle value) of data.
- `statistics.stdev(data)`: the standard deviation of data.

For example, `statistics.mean([1, 2, 3, 4, 4])` returns a value of `2.8`.
