"""
# Module 1 — NumPy Introduction

## 1. NumPy Kya Hai?

**NumPy (Numerical Python)** Python ki ek library hai jo **arrays, mathematical calculations, data analysis aur scientific computing** ke liye use hoti hai.

Simple language mein:

👉 Agar Python List cycle hai, toh NumPy Array sports bike hai.

---

## 2. NumPy Kyu Use Karte Hain?

### Python List ki Problems

* Slow hoti hai large data par
* Mathematical operations difficult hote hain
* Zyada memory leti hai

### NumPy ke Benefits

✅ Fast execution

✅ Kam memory use

✅ Easy mathematical calculations

✅ Data Science, AI, ML mein widely use hota hai

---

## 3. Python List vs NumPy Array

### Python List

```python
numbers = [1, 2, 3, 4, 5]
```

### NumPy Array

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
```

### Difference

| Feature         | Python List | NumPy Array |
| --------------- | ----------- | ----------- |
| Speed           | Slow        | Fast        |
| Memory          | More        | Less        |
| Math Operations | Difficult   | Easy        |
| Data Type       | Mixed       | Same Type   |

---

## 4. Speed Example

### Python List

```python
a = [1,2,3,4,5]
b = [10,20,30,40,50]

result = []

for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)
```

Output:

```python
[11, 22, 33, 44, 55]
```

---

### NumPy Array

```python
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])

print(a + b)
```

Output:

```python
[11 22 33 44 55]
```

👉 NumPy mein loop likhne ki zarurat nahi.

---

## 5. Installation

CMD mein:

```bash
pip install numpy
```

Version check:

```python
import numpy as np

print(np.__version__)
```

---

## 6. First NumPy Array

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
```

Output:

```python
[10 20 30 40 50]
```

"""