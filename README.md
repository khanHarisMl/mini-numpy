# Mini NumPy v1.0

A lightweight NumPy-inspired array library written in Python to strengthen my understanding of object-oriented programming, data structures, algorithms, and numerical computing fundamentals.

This project recreates a small subset of NumPy functionality from scratch without relying on the NumPy library itself. The emphasis is on understanding how array operations work internally rather than building a complete replacement.

---

## Features

### Core Class

- Custom `MiniArray` class
- Custom object representation (`__repr__`)
- Length support (`__len__`)
- Indexing support (`__getitem__`)
- Append operation for 1D arrays

---

### Aggregate Operations

- `sum()`
- `mean()`
- `min()`
- `max()`

Supports both:

- 1D arrays
- 2D matrices

---

### Element-wise Operations

Performs operations between arrays or matrices of equal shape.

- `add()`
- `subtract()`
- `multiply()`
- `divide()`

Built-in validation includes:

- Empty array detection
- Shape validation
- Array length validation
- Division-by-zero protection

---

### Matrix Support

Mini NumPy supports both one-dimensional arrays and two-dimensional matrices.

Additional helper methods include:

- `is_2d()`
- `shape()`

---

## Example Usage

### Creating Arrays

```python
from mini_numpy.array import MiniArray

arr = MiniArray([1, 2, 3])

matrix = MiniArray([
    [1, 2],
    [3, 4]
])
```

### Aggregate Operations

```python
arr.sum()
# 6

matrix.mean()
# 2.5
```

### Element-wise Operations

```python
a = MiniArray([1, 2, 3])
b = MiniArray([4, 5, 6])

print(a.add(b))
# MiniArray([5, 7, 9])
```

### Matrix Operations

```python
matrix1 = MiniArray([
    [1, 2],
    [3, 4]
])

matrix2 = MiniArray([
    [5, 6],
    [7, 8]
])

print(matrix1.multiply(matrix2))
# MiniArray([[5, 12], [21, 32]])
```

---

## Testing

The project includes test functions covering:

- Core class functionality
- Aggregate operations
- Element-wise operations
- 1D arrays
- 2D matrices
- Shape detection
- Edge cases including invalid dimensions and division by zero

---

## Future Improvements

Potential future enhancements include:

- Matrix transpose
- Matrix multiplication
- Array slicing
- Reshape operations
- Automated testing using `pytest`
- Additional NumPy-inspired functionality

---

## Purpose

The goal of this project was to gain a deeper understanding of how numerical array libraries work internally by implementing common operations from scratch.

Rather than relying on existing libraries, every feature was designed and implemented manually to strengthen problem-solving skills, Python proficiency, and software engineering fundamentals.