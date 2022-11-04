# Modules

A Python source code file is called a **script**. For a large application, you put different functions in different files (scripts). Each file is called a **module**.

To use a function from a different module, you `import` the module. The `import` **executes** the code in the file, therefore the function/varaible definitions of the imported module are available in the importing module.

If a module is imported by many modules, it is executed only in the first `import`. 

## `import`

A module is a Python source code file with `.py` suffix. Please follow [Python Naming Convention](https://github.com/naming-convention/naming-convention-guides/tree/master/python) for names. Modules, functions, methods, global/class/local variables use `lower_with_under` (lowercase snake casing). Classes, exceptions and constants uses `CAP_WITH_UNDER` (uppercase snake casing).

If a module has a filename of `my_module.py`, use `import my_module` to import the module. 