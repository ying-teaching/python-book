# Modules

A Python source code file is called a **script**. For a large application, you put different functions in different files (scripts). Each file is called a **module**.

## `import`

A module is a Python source code file with `.py` suffix. Please follow [Python Naming Convention](https://github.com/naming-convention/naming-convention-guides/tree/master/python) for names. Packages, modules, functions, methods, global/class/local variables use `lower_with_under` (lowercase snake casing). Classes, exceptions and constants uses `CAP_WITH_UNDER` (uppercase snake casing).

To use a function from a different module, you `import` the module. The `import` **executes** the code in the file, therefore the function/variable definitions of the imported module are available in the importing module. If a module is imported by many modules, it is executed only in the first `import`.

If a module has a filename of `my_module.py`, use `import my_module` to import the module. Then access its variables and functions using the dot notation: `my_module.foo()`.

An example, in `utils.py`, define a function:

```python
def factorial(number):
    """Calculates and returns the factorial (num!)"""
    x = 1
    for i in range(2, number + 1):
        x *= i

    return x
```

Then in `main.py`:

```python
import utils

n = 7
result = utils.factorial(n)
print(f'Factorial of {n} is {result}.')
```

You can also import several functions directly like `from utils import factorial`, then you can call `factorial(n)` without the module name prefix.

## Modules and Packages

There are different types of modules:

- Built-in module: pre-installed with Python, just `import module_name`.
- Modules in installed packages. You can use `pip` to install Python packages.
- Local modules: Python source files in the same folder or using relative path.

When a module is imported, the `__name__` is the filename. If a module is executed as a script, the `__name__` is `__main__`.

A directory with an `__init__.py` file defines a package that consists of many files (modules). The `__init__.py` can be empty or has `import` statements to import its modules.

The `PYTHONPATH` environment variable and `sys.path` are used to specify the searching paths when Python imports packages or modules.
