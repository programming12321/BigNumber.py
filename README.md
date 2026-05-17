# BigNumber.py

BigNumber.py is a Python library for handling extremely large numbers using layers, pentation, hexation, and hyperoperations.

Current version: `1.0.6`

Download:

```text
BigNumber version 1.0.6.py
```

The limit is:
```text
10{1e308}1e308
```

---

# Features

- Huge number support
- Scientific notation
- Layer system
- Pentation support
- Hexation support
- Hyperoperation support
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

print(a.tostring())
```

Output:

```text
5.000e10
```

---

# Layers

```python
a = BigNumber(1, 10, 2)

print(a.tostring())
```

Output:

```text
ee10
```

---

# Pentation

```python
a = BigNumber(1, 0, 0, 3)

print(a.tostring())
```

Output:

```text
G3(0)
```

---

# Hexation

```python
a = BigNumber(1, 0, 0, 0, 2)

print(a.tostring())
```

Output:

```text
H2(0)
```

---

# Hyperoperations

```python
a = BigNumber(1, 0, 0, 0, 0, 5)

print(a.tostring())
```

Output:

```text
10{5}0
```

---

# Addition

```python
a = BigNumber(5, 10)
b = BigNumber(2, 10)

print(a.add(b).tostring())
```

---

# Subtraction

```python
a = BigNumber(9, 5)
b = BigNumber(2, 5)

print(a.sub(b).tostring())
```

---

# Multiplication

```python
a = BigNumber(2, 5)
b = BigNumber(3, 5)

print(a.mul(b).tostring())
```

---

# Division

```python
a = BigNumber(8, 10)
b = BigNumber(2, 5)

print(a.div(b).tostring())
```

---

# Power

```python
a = BigNumber(2)
b = BigNumber(10)

print(a.power(b).tostring())
```

---

# Infinity

```python
print(BigNumber.INFINITY.tostring())
print(BigNumber.NEG_INF.tostring())
```

---

# Comparison

```python
a = BigNumber(1, 100)
b = BigNumber(1, 200)

print(a.lessThan(b))
print(a.greaterThan(b))
print(a.equalTo(b))
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

# rounded()

```python
a = BigNumber(1.234567, 5)

print(a.rounded())
```

---

# tofloat()

```python
a = BigNumber(5, 2)

print(a.tofloat())
```

---

# tointeger()

```python
a = BigNumber(5, 3)

print(a.tointeger())
```

---

# absValue()

```python
a = BigNumber(-5, 3)

print(a.absValue().tostring())
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
| Hyperoperations | `10{5}3` |

---

# Limits

| System | Limit |
|---|---|
| Float | `1e308` |
| Layer | `ee308` |
| Pentation | `G308(308)` |
| Hexation | `H308(308)` |
| Hyperoperation | `10{1000000}1000000` |

---

# Constants

```python
BigNumber.ZERO
BigNumber.ONE
BigNumber.PI
BigNumber.E
BigNumber.INFINITY
BigNumber.NEG_INF
```

---

# Roadmap

- Arrow notation
- Conway chained arrows
- Better formatting
- Decimal layer precision
- Performance improvements
- Custom notation systems

---

# License

MIT License
