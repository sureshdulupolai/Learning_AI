# Rename Suggestions: Trigger Automatically

# rows × columns
import numpy as np

arr1d = np.array([
    1,2,3,4,5
])

print(arr1d.shape)

array2d = np.array([
    [1,2],
    [4,5],
    [5,6]
])

print(array2d.shape)


array3d = np.array([
    [ # 1 blocks
        [1,2], # 1 rows har rows ke andar 2 column h
        [4,5] # 2 rows
    ], [ # 2 blocks
        [4,5],
        [6,7]
    ],[ # 3 blocks
        [34,34],
        [35, 56]
    ]
])

print(array3d.shape)