# The Big Picture

Draw a big picture for Python PL

Programs = Data Structures + Algorithms

## 1 Data

Three views of Data:

- Scalar and Composite (data organization)
  - Scalar types (single, atomic): int, float, bool
  - Composite types (multiple values): sequence (String, List, Tuple), mapping (dictionary), Set
- Primitive and non-primitive (what are essential data)
  - Primitive (basic building block): int, float, bool, String
  - Non-primitive (sophisticated data structure built on primitives): others
- Immutable and mutable (why? multi-threading)
  - Immutable: int, float, bool, String, Tuple
  - Mutable: others

## 2 Algorithms

Algorithms are a set of operators and functions working on data.

Functions may be independent (function) or be associated with data (method).

An algorithm is written in variables, expressions, and statements.

Program has three types of structures: sequential, branch and loop.

When program is getting bigger or to be shared: function.

When there are too many functions: modules.

When there are many modules: library or packages.

Functional programming, OO programming, Logic programming, data-oriented programming, just ways/abstractions to organize algorithm and data in a high level. The foundations are above concepts. These abstractions are more about how to view the problem domain than view the programming.

## 3 PL types

- DSL: SQL, R, Excel
- High-level general programming
  - Simple and without static types: Python, JavaScript, Lisp.
  - Complex and static types: C#, Kotlin, Java, Golang
- System: C, C++, Rust
- Native: Assemble

But a real project often requires multiple PLs. Please give an example.
