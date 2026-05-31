import numpy as np

# to check numpy version and location
# print(np.__version__)
# print(np.__file__)

# creating a numpy array
a = np.array([1, 2, 3, 4, 5])
print(a)

# creating a 2D numpy array
b = np.array([
    [1, 2, 3], [4, 5, 6]
])
print(b)

print()
"""
📚 Ek Book

Page 1
Page 2

Har page par rows aur columns hain.

Page 1
[1 2 3]
[4 5 6]

Page 2
[7 8 9]
[10 11 12]

Yahan:

2 Pages
Har page mein 2 Rows
Har row mein 3 Columns

Isliye ye 3D Array hai.
"""
# creating a 3D numpy array
c = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(c)

"""
RCB
| Virat | Patidar | Jitesh |
| ----- | ------- | ------ |
| 80    | 50      | 30     |
| 90    | 60      | 40     |

MI
| Rohit | SKY | Hardik |
| ----- | --- | ------ |
| 70    | 65  | 20     |
| 100   | 80  | 50     |

ipl = np.array([
    [ # Team RCB
        [80,50,30], # Match 1
        [90,60,40] # Match 2
    ],
    [ # Team MI
        [70,65,20], # Match 1
        [100,80,50] # Match 2
    ]
])


(Team, Match, Player)

"""





"""
1D Array
[1, 2, 3]
Ek line of data.

2D Array
[[1, 2, 3],
 [4, 5, 6]]
Table (Rows × Columns).

3D Array
[[[1, 2, 3],
  [4, 5, 6]],

 [[7, 8, 9],
  [10, 11, 12]]]
Book (Pages × Rows × Columns).

4D Array
Socho kai books ek shelf mein:
Shelf
 ├─ Book 1
 │   ├─ Page
 │   └─ Page
 └─ Book 2
     ├─ Page
     └─ Page

     5D Array

Kai shelves wali library.

5D Array
Kai shelves wali library.

6D+
Machine Learning, Deep Learning, Image Processing, Scientific Computing mein use hote hain.



NumPy Dimensions (Axes) Table:
| Dimension | Name   | Shape Example  | Axes Ka Meaning                        | Real-Life Example   |
| --------- | ------ | -------------- | -------------------------------------- | ------------------- |
| 1D        | Vector | `(5,)`         | 1 Axis                                 | Students ke 5 marks |
| 2D        | Matrix | `(3,4)`        | Rows, Columns                          | Excel Table         |
| 3D        | Tensor | `(2,3,4)`      | Pages, Rows, Columns                   | Book                |
| 4D        | Tensor | `(10,2,3,4)`   | Books, Pages, Rows, Columns            | Library             |
| 5D        | Tensor | `(5,10,2,3,4)` | Libraries, Books, Pages, Rows, Columns | Multiple Libraries  |
| nD        | Tensor | `(...)`        | n Axes                                 | Complex AI/Data     |

"""

# 6. Dimension (ndim)
# Dimension batata hai array kitne level ka hai.

arr = np.array([1,2,3,4])
print(arr.ndim) # 1 => 1D

arr = np.array([
    [1,2],
    [3,4]
])

print(arr.ndim) # 2 => 2D Array