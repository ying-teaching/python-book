# Chapter 3 Notes

This is lecture note for Chapter 3.

## 3.1 String Basics

- A string is a sequence of characters.
- A programmer creates a string literal by surrounding text with single or double quotes, such as `'MARY'` or `"MARY"`.
- An empty string is a sequence type with 0 elements, created with two quotes. Ex: `my_str = ''`.
- The `len()` built-in function can be used to find the length of a string (and any other sequence type).
- A programmer can access a character at a specific index using `alphabet[index]`. `index` starts from `0` and ends with `len(alphabet) - 1`.
- Strings are immutable.
- Use `+` to concatenate two strings.

## 3.2 List Basics

A **list** is a sequential container (similar to a string) that composites values.

- Use `my_list = ['foo', 'bar' ]` to create a list of two elements.
- Use `my_list[index]` to access a single element at the `index`, starting from `0`.
- A list is **mutable**:
  - `my_list[1] = 'b'`.
  - `append`, `pop`, `remove`
- Functions working with a list: `len`, `+`, `min` etc.
- List methods: `index(val)`, `count(val)`

## 3.3 Tuple Basics

- Tuple is an unnamed immutable composite value: `(1, 3, 5)`
- Import `namedtuple` to use a named tuple allows the programmer to define a new simple data type that consists of named attributes.

There are functions and methods working with a tuple.

## 3.4 Set Basics

A set is an unordered collection of unique elements. Sets have the following properties:

- Elements are **unordered**: Elements in the set do not have a position or index.
- Elements are **unique**: No elements in the set share the same value.

There are functions and methods working with a set. Using `in` operator to check memebership is probably the most used operation in set.

## 3.5 Dictionary Basics

A dictionary is a Python container used to describe associative relationships. A dictionary associates (or "maps") **keys** with **values**.

Two important observations:

- List is a special type of dictionary, can you see the link?
- It can be the base of OO programming.

There are functions (**CRUD**) and methods working with a tuple.

## 3.8 Type Conversion

An implicit conversion is a type conversion automatically made by the interpreter, usually between numeric types.

Explicit Conversion functions: `int()`, `float()`, `str()`.

## 3.9 String Formatting

Please use a formatted string literal, or **f-string** for most of string formatting. Understand but there is no need to remember the format specifications and presentation types.
