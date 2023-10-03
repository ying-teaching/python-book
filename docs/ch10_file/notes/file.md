# File

- Introduction
- File Operation
- Binary Data
- Record Operation
- More File Operations

## Introduction

Variables represent memory data that will be lost when the computer turns off. The memory is considered `primary storage` because it is manipulated by CPU instructions (programs) directly. To permanently store data, you use `secondary storage`, a hard driver or solid state disk (SSD).

There are two common ways to store data in secondary storage:

- file: store data in any structure/format you like.
- database: store data that follows a certain well-defined structure.

The boundary between the two is not clear because databases use files to store its data and enforce a structure. Recently, the [document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database) allows more flexibility in data structure.

### File Types

Files can be categorized by the access mode (`random` or `sequential`) or data encoding (text or binary). Access mode is the order mechanism used by Python to access file data.

- Random Access: you can go to any position and access the data there inside a file.
- Sequential Access: you read/write files sequentially from the beginning to the end. We cover the sequential access method because most large secondary storage devices support the sequential access.

### Data Encoding

Data encoding is the method Python uses to interpret the file data.

- Text: a text file contains data encoded as a sequence of characters. The actual character can be represented by different coding format such as `ascii` or `Unicode`. Many text files use first two or three bytes to mark the encoding type. Python will handle this for you automatically and it works correctly most of the time.
- Binary: a binary file is treated as a sequence of bytes. It is up to the program to interpret the meaning of the data. Multi-media data such as video/audio/picture often use binary file.

### Files are Resources

Files and databases are stored in secondary storage.

To access files or databases, Python creates some data objects in memory to represent a file or a database connection.

These objects uses system resources such as memory, process (a running program is a process), file descriptor etc. Therefore files and databases are often called resources in programming language.

### Resource Management

The resource concept is important because each computer only has a limited amount of any resources. A typical computer has 1GB to 1TB memory, a maximum of `32_767` (x86) or `4_194_303` (x86_64) processes in Linux and a limit of `65_535` file descriptors in Linux.

A program should return a resource after use to let other programs to use the resource. In terms of file operation, you should `close` a file after you `open` and use the file. It is easy to forget to `close` a file after using it and cause resource-leak.

To prevent this from happening, you shouldn't manually `close` a file. Use the Python `with` statement when you open a file and Python will close the file automatically.

## File Operations

- Open
- Write
- Read

### Open a File

There are two ways to open a file.

```python
file_variable = open(filename, mode)
with file_variable:
    # read/write file operations
    ...
```

Or combine the `with` and `open` using:

```python
with open(filename, mode) as file_variable:
    # read/write file operations
    ...
```

### Open Multiple Files

Similarly, there are two ways to open multiple files:

```python
file_variable1 = open(filename1, mode)
file_variable2 = open(filename2, mode)
with file_variable1, file_variable2:
    # read/write the two files
    ...
```

```python
with open(filename1, mode) as file1, open(filename2, mode) as file2:
    # read/write the two files
    ...

```

### Filename

The `filename` can be a filename with or without a path. If the filename doesn't have a path prefix, the path is the current path that you run the Python program.

The path prefix is different in Windows and Linux/MacOS.

- In Windows, a path uses backslash to separate folders and is like `"C:\Users\Alice\tmp\data.txt"`.
- In Linux/MacOS, a path uses slash to separate folder and is like `"/users/alice/tmp/data.txt"`.

### Open Mode

There are several `mode` values in Python but the three most used modes are:

- `'r'`: reading-only. You can only read data from the file. This is the default mode if you don't provide a `mode` argument.
- `'w'`: writing. If the file already exits, erase its content. Otherwise, create a new file with the specified filename.
- `'a'`: appending. All data written to the file will be appended to the end.

**Warning**: be careful when you use the `'w'` mode because it alway starts with an empty content. If the file already exists, the existing content will be erased.

## Write

Use the `write(data)` method of a file object to write `data` to a file. You write strings to a text file as the following.

```python
FILENAME = 'names.txt'
WRITE_MODE = 'w'

with open(FILENAME, WRITE_MODE) as names_file:
    names_file.write('Alice\n')
    names_file.write('Bob\n')
    names_file.write('Cindy\n')
```

### Manual Close (Not Recommended)

The the above `with` statement will close the file automatically after the three write operation in its code block.

If you don't use `with` statement, you must close the file in a `finally` clause.

It is not recommended because the code will be more complicated and easy to introduce bugs. Following is an example:

```python
FILENAME = 'names.txt'
WRITE_MODE = 'w'

# not recommended
names_file = None
try:
    names_file = open(FILENAME, WRITE_MODE)

    names_file.write('Alice\n')
    names_file.write('Bob\n')
    names_file.write('Cindy\n')
finally:
    if names_file != None:
        names_file.close() # to prevent leaking resource
```

## Read

There are different ways to read text file content.

- Use `for` loop
- Use `readline`
- Use `readlines`

### Read with a `for` loop

To read the text file content whose lines are separated by `\n`, use a `for` loop that assigns each line to a variable. The line includes the ending `\n` character.

```python
FILENAME = 'names.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
    for line in names_file:
        print(line)
```

### `readline()`

The method returns an empty string `""` when it reaches the end of the file.

To read the whole file, you read first and check the content in a `while` loop. Following the an example:

```python
FILENAME = 'names.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
    line = names_file.readline()
    while line != '':
        print(line.rstrip('\n'))
        line = names_file.readline()
```

### `readlines()`

The `readlines` method of a file object returns a list containing all lines of the file.

```python
FILENAME = 'names.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
    lines = names_file.readlines()
    for line in lines:
        print(line.rstrip('\n'))
```

### Which is the best?

`readline()` is more complicated and is not recommended.

The `readlines()` is similar to the `for line in name_file:` version, there is an important difference: the `readlines()` read all lines in one operation. If the file is very big, it may take a while before you can see the first print output. On the other side, `for line in name_file:` reads the text file line by line. It is often more efficient because you can start processing data once you have the first line.

Therefore, it is recommended to use the first method: the `for` loop method to read text files that have many lines.

## Binary Data

Python uses **bytes** to represent binary values. A bytes object is a sequence of byte values. There are many ways to create a bytes object:

- `bytes1 = bytes('hello world', 'ascii')`: a sequence of bytes from ascii chars.
- `bytes2 = b'hello world'`: created from string literal, same as the above.
- `bytes3 = b'hello \x31\x32`: from string and hexadecimal literals.
- `bytes(100)`: a sequence of 100 bytes of `0`.
- `bytes([1, 2, 3])`: three bytes from integers.

The following is a script that reads a binary file:

```python
READ_BINARY = 'rb'
filename = 'sample.jpg'

with open(filename, READ_BINARY) as file:
    contents = file.read()
    print(f'Contents of binary file {filename}:\n')
    print(contents)
```

## Record Operation

It is a convention for a text file to use `records` and `fields` to organize data. A `record` is a complete set of data that describe an entity. A record consists a single piece or multiple pieces of data. A single piece of data is called a `field`. For example

- an employee entity has `id`, `name`, `department` to describe an employee information. The `id`, `name`, `department` are fields of a record. Each record has data for each employee.
- a student may have `name`, `score` to describe the testing score for a student. A course has multiple records and each record represents one student. The `name`, `score` are fields of a student record.

### Processing Records

There are many ways to process record data in a text file. Two popular options are:

- a line as a record: each line represents a record. Use field delimiter to separate different files in a record.
- a line as a field: each line represents a field. Use the number of fields to determine the record boundary. For example, for the above employee record that has three fields of `id`, `name` and `department`, three lines form a record.

Most applications use the method of `a line as a record` because it is more compact and easy to process.

### Fields

there are many different ways to delimit the fields in a line. The two most popular methods are:

- white space delimiter: it uses a white space character to separate different fields. The white space characters include ` ` (space), `\t` (horizontal tab), `\v` (vertical tab), `\f` (feed), `\r` (carriage return). The string method [`split()`](https://docs.python.org/3/library/stdtypes.html#str.split) can be used to split fields of a line. `\n` (new line) is also a white space character but it is used for record delimiter.
- comma separated value (CSV): this is the most common import and export format for spreadsheets and database. Python has a built-in [`csv` module](https://docs.python.org/3/library/csv.html) to process csv files.

### Writing Records

Writing is simple because all you need is to write a string that has all the fields and ends with a new line using `write` method. You can separate fields using any white space character but one or more spaces are common.

```python
FILENAME = 'scores.txt'
WRITE_MODE = 'w'

with open(FILENAME, WRITE_MODE) as names_file:
    names_file.write('Alice 97\n')

    # demo of writing variable data
    name = 'Bob'
    score = 93
    names_file.write(f'{name} {score}\n')

    names_file.write('Cindy 95\n')
```

### Reading Records

Reading a record needs to get the fields from a record. The `str.split()` makes the task simple.

```python
FILENAME = 'scores.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
    for line in names_file:
        name, score = line.split()
        print(f'Name: {name}, Score: {score}')
```

## More File Operations

- Removing and Renaming Files
- UPdating Text Files

### Removing and Renaming Files

The built-in [`os` module](https://docs.python.org/3/library/os.html) is used to provide operating system functions such as removing, renaming and checking existence of a file. Following is an example.

```python
import os # first import the module

FILENAME1 = 'test1.txt'
FILENAME2 = 'test2.txt'
WRITE_MODE = 'w'

def checkExistence(location):
    """check the existence of the two files"""
    isExist1 = os.path.exists(FILENAME1)
    isExist2 = os.path.exists(FILENAME2)
    print(f'[{location}] {FILENAME1} exists: {isExist1}, {FILENAME2} exists: {isExist2}')

# create a file first
with open(FILENAME1, WRITE_MODE) as names_file:
    names_file.write('test message\n')
checkExistence('After create')

os.rename(FILENAME1, FILENAME2)
checkExistence('after rename')

os.remove(FILENAME2)
checkExistence('after remove')
```

### Updating Text Files

Update existing file content is tricky because the file content is stored in disk in a fixed format. The following three records:

```text
Alice 97
Bob 93
Cindy 95
```

They are stored in a disk as `Alice 97\nBob 93\nCindy 95\n`. It is easy to change a field with a shorter one and leave some spaces. But changing a field to a longer one will move all later content to a different place.

### Updating Pattern

the pattern to update file is a multi-step task:

- open a source file for read
- open a temp file for write
- read data from the source file, make required changes and save to the temp file
- remove the source file
- rename the temp file to the name of the source file

The following is an example to change Bob's score to `90` and change the name `Cindy` to `Cynthia`.

```python
import os

FILENAME = 'scores.txt'
TEMP_FILE = 'temp'
READ_MODE = 'r'
WRITE_MODE = 'w'

source_file = open(FILENAME, READ_MODE)
temp_file = open(TEMP_FILE, WRITE_MODE)
with source_file, temp_file:
    for line in source_file:
        name, score = line.split()

        if name == 'Bob':
            score = 90

        if name == 'Cindy':
            name = 'Cynthia'

        temp_file.write(f'{name} {score}\n')

os.remove(FILENAME)
os.rename(TEMP_FILE, FILENAME)
```
