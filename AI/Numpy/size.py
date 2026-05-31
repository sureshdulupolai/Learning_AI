""" Size Kya Hota Hai?

Size = Array ke andar total kitne elements hain.

NumPy mein:

arr.size
Formula

Size = Shape ke sabhi numbers ka multiplication

Size = Shape[0] × Shape[1] × Shape[2] × ...
1D Array
arr = np.array([10,20,30,40,50])

Shape:

(5,)

Size:

5

Visual:

10
20
30
40
50

Total elements = 5

✅ Size = 5

2D Array
arr = np.array([
    [10,20,30],
    [40,50,60]
])

Shape:

(2,3)

Size:

2 × 3 = 6

Visual:

10 20 30
40 50 60

Count karo:

10
20
30
40
50
60

Total = 6

✅ Size = 6

3D Array
arr = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

Shape:

(2,2,2)

Size:

2 × 2 × 2 = 8

Visual:

Page 1
1 2
3 4

Page 2
5 6
7 8

Total elements:

1 2 3 4 5 6 7 8

✅ Size = 8

4D Array

Shape:

(2,3,4,5)

Size:

2 × 3 × 4 × 5
= 120

✅ Total elements = 120

5D Array

Shape:

(2,3,4,5,6)

Size:

2 × 3 × 4 × 5 × 6
= 720

✅ Total elements = 720"""


"""
print(arr.shape) 
ko munliply karne ko size bolte h total value found karna
"""