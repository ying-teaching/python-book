# Data Analysis

This tutorial is based on the following resources:

- [Python for Data Analysis, 3E](https://wesmckinney.com/book/)
- [LLM: From Zero to Hero](https://waylandzhang.github.io/en)

## Introduction

- Data
- Why Python
- Libs
- Installation

### What Kinds of Data

The focus here is the analysis of structured data that include:

- Two dimmensional (tabular or spreadsheet-like) data that has rows and columns. Each column may be a different type.
- Multidimensional Arrays: also called matrices.
- Multiple tables of data interrated by foreign keys. It is the data structure for relatioinal database.
- Time series data.

### Why Python

- Most data analysis consist of a small portiion and time-consuming computing and a large amount of "glue code" that doesn't run often. Python integrates well with C, C++ and Fortran code.
  - Computational intensive code should be implemented in C or C++.
- Python can be used for both prototyping and production.
- Python has rich libraries for data manipulation, numeric computing, machine learning, visualization, and nutural language processing (NLP).

### Essential Python Libraries

- Numpy (Numerical Python): matrix and numerical computing.
- pandas: high-level data structures, tabular and time series data processing functions. It borrows the dataframe idea from R.
- metplotlib: data visualization.
- SciPy: scientific computing includes calculus, linear algebra, signal processing, statistics, and more.
- scikit-learn: machine learning tookit includes classification, regression, clustering, and more.
- statsmodels: classical statistics and econometrics.
- TensorFlow (Google) and PyTorch (Facebook): two popular deep learning libraries.

### Installation

```sh
pip install jupyter # for Jupyter Notebook
pip install numpy matplotlib pandas seaborn statsmodels
pip install scipy scikit-learn  patsy pyarrow numba
pip install lxml beautifulsoup4 html5lib openpyxl requests sqlalchemy 
```

## NumPy

NumPy stands for Numerical Python. It is a foundation for many Python numeric computation packages.

- `ndarray` an array data type
- Array data operations
- Tools for reading/writing disk or memory files
- Linear algebra, random numbers, and Fourier tranform
- A C API for connecting NumPy with C, C++, or Fortran

### Basic Functions

- Array operations
- Array algorithms like sorting, unique, and set operations
- Data alignment and relatioinal data manipulation for heterogeneous datasets
- Conditional logic
- Group-wise data manipulations (aggretation, transformation, and function applications)

### `ndarray`

- `ndarray` is a fast, flexible data type for large datasets.
- Operations are on whole dataset.


```python
import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

print(data * 10)
print(data + data)
print(data.shape)
print(data.dtype)
```

### Creating Arrays

- `array`: Convert input data (list, tuple, array, or other sequence type) to an ndarray either by inferring a data type or explicitly specifying a data type; copies the input data by default.
- `ones`, `zeros`: Produce an array of all 1s with the given shape and data type;
- `ones_like`, `zeros_like`: takes another array and produces a ones/zeros array of the same shape and data type.
- `empty`, `empty_like`, `full`, `full_like`: no data or filled data.
- `eye`, `identity`: `N x N` identity matrix with `1`s on the diagonal and `0`s elsewhere

### Data Types and Arithmetic Operations

- Types: `int8/16/32/64`, `uint8/16/32/64`, `float16/32/64`, `complex64/128/256`, `bool`, `object`, `string_`, `unicode_`.
- Conversion:  `astype`.
- Vector arithmetic operations: `+`, `-`, `*`, `/`, `**`, `>` etc.
- Element-wise and Binary Operations
- Indexing and Slicing: like list.
- Boolean indexing
- Reshape



```python
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
data[names == "Bob"]  # selecting rows
data[names == "Bob", 1:]  # selecting rows and columns
data[~(names == "Bob")]  # negate selection

# mutiple conditions
mask = (names == "Bob") | (names == "Will")
data[mask]

# selecting and setting
data[data < 0] = 0
```


```python
arr = np.arange(32).reshape((8, 4))  # reshape
print(arr)
print(arr.T)  # transposing
print(arr.T @ arr)  # dot multiplication

arr.swapaxes(0, 1)  # transposing is a specical case of swapping axeses
```

### Pseudorandom Number Generation

The `numpy.random` module has many random number generation functions.

- `standard_normal`
- `permutation`
- `shuffle`
- `uniform`
- `integers`
- `binomial`

### Array-Oriented Programming

- The `numpy.meshgrid` function takes two one-dimensional arrays and produces two two-dimensional matrices corresponding to all pairs of `(x, y)` in the two arrays.
- Array statistical methods: `sum`, `mean`, `std`, `var`, etc
- Linear algebra: `diag`, `dot`, `trace`, `eig`, `solve`, etc

## `pandas`

- `pandas` is based on `NumPy` and contains data structures and data manipulation tools.
- It is designed to work with tabluar or heterogeneous data.


### Data Structures

- `Series`: one dimensional array with labels.
- `DataFrame`: tabular data with row and column labels

## Visualization

`matplotlib` is a  library for creating static, animated, and interactive visualizations in Python. It integrates with the `numpy` array data types.

Seaborn is a library for making statistical graphics in Python. It builds on top of `matplotlib` and integrates with `pandas` data structures.

- [`matplotlib` Quick Start](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start)
- [`seaborn` Tutorial](https://seaborn.pydata.org/tutorial.html)

