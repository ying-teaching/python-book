# Module

- Module File
- Import a Module
- Package
- Module and Path

## Module File

A Python source code file with a `.py` postfix is called a **script** file.

Each script file is called a **module**.

According to [Python Naming Convention](https://github.com/naming-convention/naming-convention-guides/tree/master/python), use `snake_casing` (lowercase words delimited by underscore) for file names.

### Module Content

Inside a module, you can define

- functions
- classes
- global variables (not recommended)

You need to import these identifiers before use them in different modules.

## Import a Module

To use a function from a different module, you `import` the module.

The `import` statement loads and **executes** the code in the script file, therefore the function/variable definitions of the imported module are available in the importing module.

If a module is imported by many modules, it is executed only in the first `import`.

### Import Syntax

If a module has a filename of `my_module.py`, use `import my_module` to import the module.

Then you access its variables and functions using the dot notation: `my_module.foo()`.

Alternatively, you can import identifiers directly using the syntax: `from my_module import foo`. Then you can use the identifier without the module name like `foo()`. You can import one or more identifiers.

You can give imported identifier an alias like `from my_module import foo as bar`, then you can use `bar` in place of `foo`.

### `__name__`

When a module is imported, the `__name__` is the filename.

If a module is executed as a script, the `__name__` is `__main__`.

To test a file named `my_file.py`, you can import the file `import my_file` or run it from command line like `python my_file.py` to see the difference.

```python
# my_file.py

if __name__ == "__main__":
    print("Run as a script.")
else:
    print("run as imported module.")

```

### An Import Example

There are two files in this example:

- `utils.py` defines a global constant `PI` and a function `factorial`
- `main.py` imports and uses the identifier defined in `utils.py` module.

When you run the `main.py` script, it shows the printed message in `utils.py` because the `print` function is executed by the `import` statement, that is before other statements in the `main.py` module.

```python
# utils.py
print("show message when this is first imported")

PI = 3.14

def factorial(number):
    result = 1
    for count in range(2, number + 1):
        result *= count

    return result

# main.py
from utils import PI, factorial

if __name__ == "__main__":
    print(PI)
    print(factorial(5))

```

## Package

A non-trivial application has many modules. It is a best practice to put relevant modules into a directory and create an `__init__.py` file in the directory.

A directory with an `__init__.py` file defines a package that consists of many files (modules). Like a directory, a package can have nested packages.

The `__init__.py` can be empty or has `import` statements to import its modules. If it is not empty, `import my_package` executes the code in `my_package/__init__.py` file.

### A Package Example

```text
my_package/
    __init__.py
    module1.py
    module2.py
    ...
    nested_package/
        __init__.py
        sub_module1.py
        sub_module2.py
        ...
```

### Import a Package

You can import a module define in a package using the directory path.

For example, for the previous package example, you can use

- `import my_package.module1` or `from my_package import module1`
- `import my_package.nested_package.sub_module2` or `from my_package.nested_package import sub_module2`

### Relative Import in Package

Inside a package, you can also use relative path to import a module. A relative import must use the `from ... import ...` syntax and start with a `.` for modules in the current directory, or `..` for parent directory, or `...` for parent's parent directory.

- in `my_package.module1`, you can use `from .nested_package import sub_module1`
- in `nested_package.sub_module2`, you can use `from .. import module1` or `from ..module1 import something`.
- in `nested_package.sub_module2`, you can use `from . import sub_module1` or `from .sub_module1 import something`.

The last example is special for a package, i.e., a directory with a `__init__.py` file.

If a module is the program entry or is not in a package, to import modules in the same directory, you use `import sub_module1` or `from sub_module1 import something`, as shown in the previous example code `from utils import PI, factorial`.

### Module and Path

There are different types of modules:

- Built-in module: pre-installed with Python, just `import module_name`.
- Modules in installed packages. You can use `pip` to install Python packages.
- Local modules: Python source files in the same folder or using relative path.

Except the built-in modules, Python searches a set of paths to find a module file.

You can read the search paths using `sys.path` variable. Usually you don't need to change it.

```python
import sys

print(sys.path)

# a sample output in MacOS
# ['', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python311.zip', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages'

```
