# Collection

People often need to deal with a collection of objects in a consistent way.

Python provides three types of language constructs to support collection operation:

- built-in collection types that can contain multiple elements
- creating new collections from existing ones
- creating classes that contain data collection

## Data Types
- sequence
  - `str`: an immutable sequence of characters.
  - `list`: a mutable sequence of any objects.
  - `tuple`: an immutable sequence of objects.
- set
  - `set`: a mutable unordered collection of unique objects.
- mapping
  - `dict`: a mutable mapping of key and value pairs.

## Comparison

| Features | List	| Tuple | Dictionary |	Set |
| --- | --- | --- | --- | -- |
| Eample	| [1, 2, 3] | ('apple', 3) | {'name': 'Alice', 'age': 7} | {2, 4} |
| Mutable? |	Mutable	 | Immutable |	Mutable |	Mutable |
| Mutable element? | Yes | Yes | Key: No, Value: yes | No |
| Ordered? |	Ordered	 | Ordered | Preserves order since Python 3.7 | Unordered |
| Search time |	O(n) |	O(n) |	O(1) |	O(1) | 

## When to use which?

- List: a mutable sequence of ordered data
- Tuple: an immutable sequence of ordered data
- Dictonary: accessing data by its key
- Set: a collection of unique, unordered data

## Creating New Collections From Existing Ones

Python provides two convenient constructs to create new collections:

- List/set/dictionary comprehension
- Generator expression

Many times, these constructs make your program simple and efficient.

## 1 String

A string is a sequence of characters.

A string is an immutable object. 

A programmer creates a string literal by surrounding text with single or double quotes, such as `'MARY'`, `"MARY"`, `'41'`, or `"41"`.

An empty string is a sequence type with 0 elements, created with a pair of single/double quotes. Ex: `my_str = ""` or `my_str=''`.

Python use backslash `\` to escape special characters. For example: `"\n"` represents a newline character. It is also used to escape a slash or quotation symbols. For example: `"a slash \\ and an escaped \" double quotation mark.`

### 1.1 Built-in String Operations

A programmer can access a character at a specific index using `alphabet[index]`. `index` starts from `0` and ends with `len(alphabet) - 1`.

The `len()` built-in function can be used to find the length of a string (and any other sequence type).

Use `+` to concatenate two strings.

Use `in` to determine if a character or a substring exists in a string. It returns `True` or `False`

Use `for` loop to iterate every character.


```python
text = "Hello World"

print(len(text))  # 11

print (text + " to every one.") # Hello World to every one.

print("H" in text, "hi" in text) # True False

for char in text:
    print(char, end=" ")    
# H e l l o   W o r l d 

```

### 1.2 Slicing

Python has a special slicing syntax `sequence[start:stop:step]` to get a subset of a sequence.

- `start`: optional, starting index of the slice.
- `stop`: the last index (exclusive) of the slide or the number of items to get. It is optional with a default to `len(sequence)` if the `start` argument is specified.
- `step`: optional, the step value with a default of `1`.

You can slice a string to get another string. 

You can also use slicing syntax in other sequence types that works similarly.


```python
text = "hello world"

print(text[2]) # regular index: "l"
print(text[2:]) # from index 2 to end: "llo world"
print(text[0:3]) # first three: "hel"
print(text[::4]) # every fourth character: "hor"
print(text[3::2]) # from index 3, every other characters: "l ol"

```

### 1.3 Common String Methods

Because string is an immutable object, any method that changes the string content will create a new string.

Following are some examples:


```python
hi = "Hi"
text = "hello world"

# find the index of the first occurrence of a substring, -1 if not found
print(text.find('o')) # 4
print(text.find("alice")) # -1

# Lower case, upper case and title case
print(hi.lower()) # hi
print(text.upper()) # HELLO WORLD
print(text.title()) # Hello World

# split a string into a list by the specified separator string
# default is white space
print(text.split()) # ["hello", "world"]
print(text.split("ll"))  # ["he", "o world"]

# replace a substr with another substr
print(hi.replace('i', 'a')) # Ha
print(text.replace("world", "alice")) # hello alice

# join a list of strings together with the desired separator string
print(", ".join(["alice", "bob", "cindy"])) # alice, bob, cindy

```

## 2 List

A _list_ is a sequential container (similar to a string) object that contains a number of elements. The objects in an list are called _elements_ or _items_ of the list. 

It is a mutable object whose value is changed in place.

List elements can be in different types, but it is a best practice to put same-type elements into a list.

### 2.1 Creating A List

There are two common ways to create a list. 

First, you can create a list literally by listing elements in brackets and separating by commas.

Second, Python has a built-in `list()` function that can convert certain types of objects to lists.


```python
# create a list from literals
some_numbers = [3, 5 ,7]
names = ['Alice', 'Bob', 'Cindy']
# elements can be of different types - not recommended
some_data = [3, 'Alice', 12.5] 

# use list() function
generated_numbers = list(range(3, 8, 2))
letters = list('abc')

# print can print a list directly
print(generated_numbers)
print(letters)

```

### 2.2 Basic Operations

A list has a sequence of elements. A basic requirement is to access one element, all elements or some elements.

- one element: index
- all elements: loop
- some elements: slice

### 2.2.1 Index

Each element in a list has an index associated with it, starting from `0`.

The first element has an index of `0`, the second element has an index of `1`, and so on and so forth. 

If the index is out of range, Python raises an `IndexError` exception.

The last element has an index of the list length minus `1`.

You can use negative index numbers to access elements from the end of the list. For example, `-1` identifies the last element in a list, `-2` identifies the next to last element, and so on an so forth.

The index syntax is to put an index in a pair of brackets, right after the list variable name.


```python
numbers = [3, 5 ,7]

print(numbers[0], numbers[1], numbers[2])

print(numbers[-1], numbers[-2], numbers[-3])

# oops, IndexError if the index is out of range
print(numbers[5])

```

### 2.2.2 Unpack a List

You can unpack a tuple and assign its elements to different variables.

You can prefix the last variable with a `*` to match multiple elements of a list.

Use `_` if you don't need the elements.


```python
numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first, second, rest) # 1 2 [3, 4, 5]

first, _, third, *_ = numbers
print(first, third) # 1, 3

first, second, *_ = numbers
print(first, second) # 1, 2

first, *_, last = numbers
print(first, last) # 1, 5

```

### 2.2.3 Accessing All Elements

You can loop (iterate) over a list to access all its elements.

Both `for` and `while` loops can be used, but the Pythonic way is using `for` because it is less error-prone and simpler than `while` loop.

When you need the element index, the Pythonic way is to use built-in `enumerate()` functions.


```python
numbers = list(range(3, 8, 2))

# use for
for number in numbers:
    doubled = number * 2
    print(f'Double element {number} is {doubled}')

# use enumerator if you need the index
for index, number in enumerate(numbers):
    print(f'Index: {index}, Value: {number}')

# Not recommended
length = len(numbers)
for index in range(length):
    print(f'Index: {index}, Value: {numbers[index]}')

# Not recommended
index = 0
while index < len(numbers):
    print(f'Index: {index}, Value: {numbers[index]}')
    index += 1

```

### 2.2.4 Slicing a List

A `slice` is a span of items taken from a list. It is used to select some elements from a list. To slice a list, you use the `list_name[start : end : step]` to specify the start index and end index of a list. Like the `range` syntax, it doesn't include the `end` index. Following are some examples:


```python
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# index from 0 to 5, excluding 5
weekday = days[0:5] 
print(f'Weekdays are: {weekday}')

# default start is 0
weekday2 = days[:5] 
print(f'Weekdays version 2 are: {weekday}')

weekends = days[5:7]
print(f'Weekends are {weekends}')

# default end is the length
weekends2 = days[5:] 
print(f'Weekends version 2 are {weekends}')

odd_days = days[::2] 
print(f'Odd days are {odd_days}')

```

### 2.3 List and Built-in Operations

Python has several built-in operators and functions working with a list.

- Operators
  - `in`: check if an item is a list element.
  - `not in`: check if an item is not a list element.
  - `+`: combine two lists
  - `*`: repeat a list for a number of times
  - `del`: delete an element from a list
- Functions
  - `len`: get the length of a list
  - `min`: get the minimum element of a list
  - `max`: get the maximum element of a list
  - `sum`: get the sum of number elements of a list


```python
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekday = days[:5] 
today = 'Thu'

is_weekday = today in weekday
print(f'Today is {today}. Is weekday: {is_weekday}')
is_weekend = today not in weekday
print(f'Today is {today}. Is weekend: {is_weekend}')

tens = [10, 20, 30]
hundreds = [500, 600, 700]
all = tens + hundreds
print(all)

repeated_tens = tens * 3
print(repeated_tens)

numbers = [3, 5, 7]
length = len(numbers)
smallest = min(numbers)
biggest = max(numbers)
total = sum(numbers)
print(f'Length: {length}, Min: {smallest}, Max: {biggest}, Sum: {total}')

```

### 2.4 List Methods

Lists have numerous methods that you can use to manipulate a list.

You use `list_name.method_name()` to call a method that work on a list.

It is important to differentiate an in-place modification and an operation that returns a new list. Both `+` and slicing return a new list.

### Method Examples

- `list_name.append(element)`: add an element to the end of the list. 
- `list.extend(iterable)`: extend the list from an iterable object. An `iterable` object is a collection object that you can apply the `for` loop. For example, `range(5)` is an iterable object.
- `list_name.index(element)`: find the first index of an element, raise a `ValueError` if the item is not found. To avoid exception, use `element in list_name` to check the existence first.
- `list_name.insert(index, element)`: insert an item at the specified index.
- `list.pop()`: remove the last element, `list.pop(index)`, remove the element at the `index` position.  
- `list_name.sort()`: sort the items in the list.

You can find more list methods in [Python List Document](https://docs.python.org/3/tutorial/datastructures.html).


```python
numbers = [3, 5, 7]
n2 = numbers
n3 = numbers[:2]
numbers.append(42) 
print(numbers) # [3, 5, 7, 42]

if (5 in numbers):
    print(numbers.index(5)) # 1


numbers.insert(1, 50)
print(numbers) # [3, 50, 5, 7, 42]

numbers.sort()
print(numbers) # [3, 5, 7, 42, 50]
print(n2)
print(n3)

```

### 2.5 Nested List

A list can have other lists as its elements. There is nothing special for nested lists, you just use the index to access each element in a list. For example:


```python
numbers = [1, [2, 3], [4, 5, 6]]
numbers[1].append(42)
del numbers[2][2]
print(numbers)

```

### 2.6 List as Mutable Argument

Be _careful_ when you pass a list as an argument to a function because the list is a mutable object.

If the function changes the list value in the function body, the passed-in object changes because an argument is just an alias to the object.

It is a best practice that you should not change a mutable argument in a function body. If there is a need, make a copy of the object.

However, if elements of a list are mutable, for example, nested lists, you need a deep copy. Check [Python copy document](https://docs.python.org/3/library/copy.html?highlight=deep%20copy) for more details.


```python
def report_sum(numbers):
    numbers.append(10)
    print(sum(numbers))

scores = [3, 5, 7]
print(f"before call scores are {scores}")

report_sum(scores)
print(f"after call scores are {scores}")

def report_sum2(numbers):
    new_numbers = numbers.copy()
    new_numbers.append(10)
    print(sum(new_numbers))

scores = [3, 5, 7]
print(f"before call scores are {scores}")

report_sum2(scores)
print(f"after call scores are {scores}")

```

### 2.7 A Stack

A stack is a data structure that stores elements in an last in, first out (LIFO) manner. For example, Python runtime uses stack to manage calls -- named as a _call stack_. A stack supports two basic methods: 

- `append` that adds an element to the top of a stack. The operation is often called `push`
- `pop` that pops an element from the top of a stack.

When using a list to implement a stack, the _top_ is the end of a list. You can `append` (also called push in stack) an element and `pop` an element. Both operate at the end of a list.


```python
numbers = [1, 2, 3]
numbers.append(37)
numbers.append(42)
top = numbers.pop()
print(top)

```

## 3 Tuple

A tuple consists of a number of values separated by commas.

A tuple is an immutable object.

Tuple is often used to represent a short sequence of data that have different data types. For example, returning multiple values as a tuple.

### Tuple Operations

The tuple operations are similar to the list operation, except that it doesn't support any write operation because it is immutable.

You access tuple by index or slicing.

You can unpack a tuple and assign its elements to different variables.

You can use built-in operator (such as `+`, `==` etc) and built-in functions (such as `len()`, `max()`) and so on with tuple.


```python
# create a tuple 
person1 = "Alice", 19
print(person1[0]) # Alice

# you can create a tuple in parentheses
person2 = ("Bob", 20)

person1 == person2 # False

name, age = person1
print(name, age) # Alice, 19

# an empty tuple
empty = ()

# a tuple with one element
one = 1,

numbers = 1, 2, 3, 4, 5
print(numbers[0]) # 1
print(numbers[::2]) # (1, 3, 5)
print(max(numbers)) # 5

first, second, *rest = numbers
print(first, second, rest)

first, _ = numbers
print(first) # 1

```

### Tuple Is Immutable, But

Tuple is a collection of elements.

Actually it contains a collection of element _references_. The number and the position of references are immutable.

However, if the reference points to a mutable object such as a list, the list data can be changed.

You can see that a tuple is an immutable structure, but its value may change.


```python
alice = "Alice", [3, 4, 5]
alice[1].append(42)
print(alice) # ('Alice', [3, 4, 5, 42])

# however, you cannot using the assignment to change tuple element
# both give TypeError:  you cannot using the assignment to change tuple element
alice[0] = "Bob"
alice[1] += 42

```

## 4 Set

A set is an _unordered_ collection of _unique_ elements. Sets have the following properties:

- unordered: Elements in the set do not have a position or index.
- unique: No elements in the set share the same value.
- immutable elements: all elements are immutable.

Built-in operators and functions work with a set like a list or tuple.

You can use `for` loop to iterate all elements of a set, though the order might change for different runs.

But you don't access individual set elements as you do with a list or a tuple.

You often use `in` operator to check membership. Set is unique in its support of many set operations like union, intersection, difference, and symmetric difference.

### 4.1 Create a Set

There are two ways to create a set:

- using a `{}` to include a sequence of object separated by `,`
- using `set()` operation to create a set from another sequential data like a list or a tuple.
  - you can only use `set()` to create an empty set because `{}` is used for empty dictionary.


```python
fruits = {"apple", "orange", "banana"}

numbers = {1, 2, 3, 2, 3, 5}  # set removes duplicated elements
print(numbers) # 1, 2, 3, 5

odds = set(range(1, 6, 2))
print(odds) # 1, 3, 5

```

### 4.2 Immutable Elements in Set

Set is kind of special because it is an mutable object but all its elements must be immutable.

For example, the following code raises a `TypeError` because a list is a mutable object. Technically, Python cannot run `hash` operation on an mutable object.

The tuple version works because a tuple is immutable. 


```python
odds = [1, 3, 5]
evens = [2, 4]

# TypeError because mutable object
my_set = {odds, evens}

```


```python
# now it works
odds_2 = (1, 3, 5)
evens_2 = (2, 4)
my_set = {odds_2, evens_2}

```

### 4.3 Set Operations

Using `in` or `not in` operator to check membership.

You can add or remove elements.

Set supports most set operations like like union, intersection, difference, and symmetric difference.


```python
fruits = {"apple", "orange", "banana"}
print("apple" in fruits) # True
print("kiwi" in fruits) # False

fruits.add('kiwi') 
fruits.add("apple") # redundant, ignored 
fruits.remove("apple")

more_fruits = {"kiwi", "pear"}

print(fruits) # {'banana', 'kiwi', 'orange'}
print(more_fruits) # {'pear', 'kiwi'}

# union
print(fruits | more_fruits) # {'orange', 'banana', 'pear', 'kiwi'}
# difference
print(fruits - more_fruits) # {'orange', 'banana'}

```

## 5 Dictionary

A dictionary is an _unordered_ collection of elements where each element has two parts: a key and a value. Or you can say that an element is a key-value pair.

The key can be any object as long as it is _immutable_. Common key types include `int` and `string`.

People use dictionaries to store key-value pairs thus it is easy to find out a value. For example, you use `student_id` to retrieve a student object.

### 5.1 Create a Dictionary

You use `{}` to create a dictionary. The `{}` creates an empty dictionary. You can use a dictionary variable as a boolean expression to check if it is empty. To create elements, create a sequence of `key: value` pairs separated by `,`.

Another approach to create a dictionary is using the built-in `dict()` function. The argument is a sequence of key-value pairs. If the keys are simple string, you can call it using keyword arguments. 


```python
empty_dict = {}
print(empty_dict)

students = {90: 'Alice', 27: 'Bob', 50: 'Cindy'}
print(students)

more_students = {90: 'Alice', 27: 'Bob', 90: 'Cindy', 200: 'Mike'}
print(more_students)


# use the dict() built-in function
students = dict([(90, 'alice'),  (27,  'bob')])
print(students)

my_dict = dict(A='alice', B='Bob')
print(my_dict)

```

### 5.2 Read or Write a Dictionary Element

You uses the `dictionary_name[key]` to access an individual element.

You can read or update the value in the key-value pair. There is no way to change the key because it is immutable.

Be careful, there are two cases that could be wrong in using dictionaries: 

- A non exist key throws a `KeyError` exception. To avoid it, use `get` method with a specified default value. For example: `students.get(42, 'Unknown')`
- when the `dictionary_name[key]` is on the left hand side, you set a new value for an existing key or create a new key-value pair if the key doesn't exist. Any typo in the key name could be a big bug.


```python
students = {90: 'Alice', 27: 'Bob', 50: 'Cindy'}

# read a value for a key
name_with_id_90 = students[90]
print(name_with_id_90)

# change a value for a key
students[90] = 'Mike'
print(students[90])

# add a new key-value pair because 97 doesn't exist
students[97] = 'Bill'
print(students)

# reading a value for a non-exist key throws a KeyError exception
name_nobody = students[404]

```

### 5.3 Other Operations

The built-in `len` function tells how many elements in a dictionary.

The `in` and `not in` operators test whether a key exists in a dictionary.

The `del` operator delete a key-value pair from a dictionary if the specified key exists, otherwise, it throws a `KeyError` exception. The syntax is `del dictionary_name[key]`. To avoid exception, use `in` to make sure the key is there before `del`.


```python
month_days = {'Jan': 31, 'Apr': 30, 'Jul': 31}

print(f'It has {len(month_days)} elements')

if 'Jan' in month_days:
    print('Jan is in the dictionary')

if 'Feb' not in month_days:
    print('Feb is not in the dictionary')


if 'Jan' in month_days:
    del month_days['Jan']
    print(month_days)

# throw a KeyError exception because the key doesn't exist
del month_days['Jan']
print(month_days)

```

### 5.4 Iterate a Dictionary

- You can use `for key in dictionary_name:` to iterate over all keys of a dictionary. Then you use `dictionary_name[key]` to access each value.
- The `items` method returns a sequence of key-value pairs. Therefore, you can use `for key, value in dictionary_name.items():` to iterate over a dictionary.
- The `values()` method returns all values. Don't assume any order of the return values!
- The `keys()` method returns all keys.


```python
month_days = {"Jan": 31, "Apr": 30, "Jul": 31}

for month in month_days:
    print(f'{month} has {month_days[month]} days')


for month, days in month_days.items():
    print(f'{month} has {days} days')

days_sequence = month_days.values()
for days in days_sequence:
    print(days, end=' ')
print()

for key in month_days.keys():
    print(f'Month key is {key}', end='; ')
print()

```

### 5.5 More Methods

The dictionary has more methods. The following is a list of commonly-used methods. Try them.

- `clear`: clear all elements
- `pop`: return the value and remove the key-value pair. For example: `month_days.pop("Jan")`.
- `popitem`: remove the latest inserted element the dictionary, return the removed element. For example: `month_days.popitem()`.

You can also use built-in `del` operator to remove a key-value pair without return value. For example: `del month_days["Jan"]`

Exercise: please write a phone book program that lets users to input and query phone book by first name or phone number. The search should be case-insensitive. 

## 6 Creating New Collections From Existing Ones

Python provides two convenient constructs to create new collections:

- List/set/dictionary comprehension: create a list/set/dictionary from an iterable object.
- Generator expression: create an iterable object from a sequence object.

An `iterable` object is a collection object or something that you can apply the `for` loop. For example, `range(5)` is an iterable object.

The advantage of `iterable` is that it is __lazy__, generating one value at a time. `range(1_000_000_000)` doesn't create one billion numbers when it is initialized, it generate one number in each `for` loop. Thus it doesn't need memory for all numbers.

### 6.1 Motivation

When you want to create a list from a sequence with simple computation, you can use a list comprehension to simplify the code.

For example, to create a list of square roots from the first 5 integers, you can use either of the following code snippets:


```python
import math 

roots = []
for number in range(5):
    roots.append(math.sqrt(number))

print(roots)

```


```python
import math

numbers = range(5)

# you need to use list() to get the list result
roots = list(map(math.sqrt, numbers))
print(roots)

```

### 6.2 List Comprehension

Python let you use list comprehension to simplify the code. The list comprehension has a syntax like `[expression for member in iterable]`. 


```python
import math

roots = [math.sqrt(number) for number in range(5)]

print(roots)

```

### 6.3 Filtering Elements

You can use list comprehension with an additional `if condition` construct to filter out the elements.


```python
lower_letters = [char for char in "Hello World" if char.islower()]
print(lower_letters) # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

```

### 6.4 Set and Dictionary Comprehensions

Similar to a list comprehension, you can create a set or a dictionary from an iterable object.

Just replace the square bracket `[]` with the curly braces `{}`.


```python
lower_letters = {char for char in "Hello World" if char.islower()}
print(lower_letters) # {'d', 'e', 'r', 'l', 'o'}


squares = { number: number * number for number in range(5)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```

## 7 Generator Object

A generator object is an iterable object that you can use in a `for` loop.

Python has a keyword `yield` that creates a _generator object_ that returns one value in each iteration of the `for` loop.

The following function is a _generator function_ that returns a generator object.


```python
def squares(size):
    for number in range(size):
        yield number * number


five_squares = [square for square in squares(5)]
print(five_squares) # [0, 1, 4, 9, 16]

```

### 7.1 Why Generator?

The reason for having generator function and generator objects is the so-called _lazy_ computation.

Suppose that you have one billion data records, it is impossible or inefficient to load all records into the computer memory. The lazy computation that load and process one record at a time has many benefits:

- you can show some result/progress when the first item is processed.
- you don't need a large memory to hold all records.
- you might stop processing the rest of data for certain conditions.

### 7.2 Generator Expression

Instead of using a generator function, you can use a generator expression to create a generator object from an iterable object.

The syntax is similar to list/set comprehension, just use `()` in place of `[]`.

If the source iterable object is a generator object, the iterator expression is also a generator object that is computed one at a time - a **lazy** operation.


```python
squares = (number * number for number in range(5))
for square in squares:
    print(square, end=", ") 

# output: 0, 1, 4, 9, 16, 

```
