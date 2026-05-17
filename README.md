# BigNumber.py

BigNumber.py is a Python library for handling extremely large numbers using layers, pentation and hexation.
The current version is 1.0.5, download ```BigNumber version 1.0.5.py```.

## Features

- Huge number support
- Scientific notation
- Layer system
- Pentation support
- Hexation support
- Infinite values
- Incremental game style notation

---

# Installation

Download:

```text
BigNumber.py
```

Then import:

```python
from BigNumber import *
```

---

# Creating Numbers

```python
a = BigNumber(5, 10)
print(a)
```

Output:

```text
5.000e10
```

---

# Layers

```python
a = BigNumber(1, 10, 2)
print(a)
```

Output:

```text
ee10
```

---

# Pentation

```python
a = BigNumber(1, 0, 0, 3)
print(a)
```

Output:

```text
G3(0)
```

---

# Hexation

```python
a = BigNumber(1, 0, 0, 0, 2)
print(a)
```

Output:

```text
H2(0)
```

---

# Addition

```python
a = BigNumber(5, 10)
b = BigNumber(2, 10)

print(a.add(b))
```

---

# Subtraction

```python
a = BigNumber(9, 5)
b = BigNumber(2, 5)

print(a.sub(b))
```

---

# Multiplication

```python
a = BigNumber(2, 5)
b = BigNumber(3, 5)

print(a.mul(b))
```

---

# Division

```python
a = BigNumber(8, 10)
b = BigNumber(2, 5)

print(a.div(b))
```

---

# Power

```python
a = BigNumber(2)
b = BigNumber(10)

print(a.power(b))
```

---

# Infinity

```python
print(BigNumber.INFINITY)
print(BigNumber.NEG_INF)
```

---

# Comparison

```python
a = BigNumber(1, 100)
b = BigNumber(1, 200)

print(a.lessThan(b))
print(a.greaterThan(b))
```

---

# tostring()

```python
a = BigNumber(1, 50)

print(a.tostring())
```

Output:

```text
1.000e50
```

---

# Example Incremental Game

```python
points = BigNumber.ONE

gain = BigNumber(5, 2)

while True:

    points = points.add(gain)

    print(points.tostring())
```

---

# Number Formats

| Type | Example |
|---|---|
| Scientific | `1.000e50` |
| Layer | `ee10` |
| Pentation | `G5(3)` |
| Hexation | `H2(10)` |

---

# Limits

| System | Limit |
|---|---|
| Float | `1e308` |
| Layer | `ee308` |
| Pentation | `G308(308)` |
| Hexation | `H308(308)` |

---

# Roadmap

- Tetration
- Hyper operators
- Arrow notation
- Omega notation
- Conway chained arrows
- Better formatting
- Decimal support
- Performance improvements

---

# License

MIT License
