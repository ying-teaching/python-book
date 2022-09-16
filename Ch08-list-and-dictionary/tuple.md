# Tuples

## Basic Concept

A `tuple` is an immutable sequence. It is similar to a list because both have a sequence of elements, however a tuple is immutable: once created, you can only read it but cannot change it. It is helpfule to represent a small set of data such as result data of a function call.

To create a tuple, just put the elements in a pair of parenthese: `a_tuple = (2, 3, 4, 5)`. If there is only one element (rarely used), put a comma after the element: `single = (2, )`. You can also use `tuple` function to create a tuple from a list or a range. For example: `a = tuple(range(5))` or `b = tuple([2, 3, 4])`.

A tuple support the same set operations of a list, except those change the contents of a list. The common operations are:

- indexing: `a_tuple[1]`
- slicing: `a_tuple[1:]`
- `in`, `+` and `*` operators
- built-in functions: `len`, `min`, `max`

The following code will throw an exception because a tuple is immutable: `a_tuple[0] = 42`.

## Tuple vs List

You can see that tuples and lists are very similar in there operations. There are two important differences between a tuple and a list:

- A tuple is immutable and a list is mutable. You can write `list[index] = value` but you cannot write `tuple[index] = value` because a tuple is immutable.
- A tuple has better performance than a list. For big data, it makes a big difference.

Two common ues case for tuples are:

- As a return value from a function. For example: `turtle.position()` returns a tuple of x and y coordinates.
- As a collection of data in big data analysis for its good performance.

For a small data set, the peformance is not a concern for both list and tuple. When you want to change a collection data in place, use a list. Otherwise, tuple is a good option.
