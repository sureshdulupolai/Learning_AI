# 7. Datatype (dtype)
# Datatype batata hai array ke andar kis type ka data store hai.

import numpy as np

arr = np.array([10,20,30])
print(arr.dtype) # int64 => Integer Data

arr = np.array([1.5,2.5,3.5])
print(arr.dtype) # float64 => Decimal Number

arr = np.array(["Ram","Shyam","Mohan"])
print(arr.dtype) # <U5 => String Data
# U = Unicode String
# 5 = Maximum length

# | Category         | Example dtype                 | Use                   |
# | ---------------- | ----------------------------- | --------------------- |
# | Integer          | int8, int16, int32, int64     | Whole numbers         |
# | Unsigned Integer | uint8, uint16, uint32, uint64 | Positive numbers only |
# | Float            | float16, float32, float64     | Decimal values        |
# | Complex          | complex64, complex128         | Complex numbers       |
# | Boolean          | bool_                         | True / False          |
# | String           | str_, `<U`                    | Text                  |
# | Bytes            | bytes_                        | Binary/Text bytes     |
# | Datetime         | datetime64                    | Date & Time           |
# | Timedelta        | timedelta64                   | Time Difference       |
# | Object           | object_                       | Mixed Python objects  |


"""
| Type  | Range Approx        |
| ----- | ------------------- |
| int8  | -128 to 127         |
| int16 | -32768 to 32767     |
| int32 | Large integers      |
| int64 | Very large integers |

float16
float32
float64

uint8
uint16
uint32
uint64

| Type        | Real-Life Use        |
| ----------- | -------------------- |
| int64       | IDs, Age, Quantity   |
| float64     | Salary, Price, Marks |
| bool        | Active/Inactive      |
| str         | Name, Email          |
| datetime64  | Created Date         |
| timedelta64 | Days Difference      |
| object      | Mixed Data           |

Most User Datatype:
Integer
Unsigned Integer
Float
Complex
Boolean
String
Bytes
Datetime
Timedelta
Object
"""

# 4. Complex Numbers
# Maths aur scientific calculations mein use hote hain.

arr = np.array([1+2j, 3+4j])
print(arr.dtype) # complex128


# 5. Boolean
# Sirf True/False.

arr = np.array([True, False, True])
print(arr.dtype) # bool

# 7. Bytes
# Raw binary data.

arr = np.array([b"hello", b"world"])
print(arr.dtype) # |S5

# 8. Datetime
# Date store karne ke liye.

arr = np.array(
    ["2026-05-30","2026-05-31"],
    dtype="datetime64"
)

print(arr.dtype) # datetime64[D]

"""
Order Date
Joining Date
Invoice Date
"""

# 9. Timedelta
# Date difference.

arr = np.array([5,10], dtype='timedelta64[D]') # timedelta64[D]
# to get output like this : 5 Days, 10 Days

# 10. Object
# Mixed data.

arr = np.array(
    [10, "Ram", True],
    dtype=object
)

print(arr.dtype) # object


"""

Datatypes Most Used by Developers

| Type        | Real-Life Use        |
| ----------- | -------------------- |
| int64       | IDs, Age, Quantity   |
| float64     | Salary, Price, Marks |
| bool        | Active/Inactive      |
| str         | Name, Email          |
| datetime64  | Created Date         |
| timedelta64 | Days Difference      |
| object      | Mixed Data           |


"""

# Datatype Convert 
# Converting Int to Float Datatype
arr = np.array([1,2,3])
arr = arr.astype(float)
print(arr.dtype) # float64



# ==========================================
# NUMPY UNSIGNED INTEGER (uint) COMPLETE DEMO
# ==========================================

import numpy as np

# --------------------------------------------------
# UNSIGNED INTEGER (uint) KYA HOTA HAI?
# --------------------------------------------------
# uint = Unsigned Integer
#
# ❌ Negative Numbers Allowed Nahi
# ✅ Sirf 0 aur Positive Numbers
#
# Example:
# 0, 1, 2, 3, 100, 255
#
# uint ka use tab karte hain jab hume pata ho
# ki value kabhi negative nahi hogi.
#
# Real Life Examples:
# - Age
# - Product Quantity
# - Stock
# - Image Pixels
# - Marks
# --------------------------------------------------


# --------------------------------------------------
# uint8
# --------------------------------------------------
# Size: 8 bits (1 byte)
# Range: 0 to 255
# --------------------------------------------------

arr_uint8 = np.array([10, 20, 30], dtype=np.uint8)

print("uint8 Array:")
print(arr_uint8)
print("Datatype:", arr_uint8.dtype)
print("Min Range: 0")
print("Max Range: 255")
print()


# --------------------------------------------------
# uint16
# --------------------------------------------------
# Size: 16 bits (2 bytes)
# Range: 0 to 65,535
# --------------------------------------------------

arr_uint16 = np.array([1000, 2000, 3000], dtype=np.uint16)

print("uint16 Array:")
print(arr_uint16)
print("Datatype:", arr_uint16.dtype)
print("Min Range: 0")
print("Max Range: 65,535")
print()


# --------------------------------------------------
# uint32
# --------------------------------------------------
# Size: 32 bits (4 bytes)
# Range: 0 to 4,294,967,295
# --------------------------------------------------

arr_uint32 = np.array([100000, 200000, 300000], dtype=np.uint32)

print("uint32 Array:")
print(arr_uint32)
print("Datatype:", arr_uint32.dtype)
print("Min Range: 0")
print("Max Range: 4,294,967,295")
print()


# --------------------------------------------------
# uint64
# --------------------------------------------------
# Size: 64 bits (8 bytes)
# Range:
# 0 to 18,446,744,073,709,551,615
# --------------------------------------------------

arr_uint64 = np.array(
    [1000000000, 2000000000, 3000000000],
    dtype=np.uint64
)

print("uint64 Array:")
print(arr_uint64)
print("Datatype:", arr_uint64.dtype)
print("Min Range: 0")
print("Max Range: 18,446,744,073,709,551,615")
print()


# --------------------------------------------------
# MEMORY CHECK
# --------------------------------------------------
# itemsize batata hai ek element kitne bytes le raha hai
# --------------------------------------------------

print("Memory Usage Per Element")
print("uint8  =", arr_uint8.itemsize, "byte")
print("uint16 =", arr_uint16.itemsize, "bytes")
print("uint32 =", arr_uint32.itemsize, "bytes")
print("uint64 =", arr_uint64.itemsize, "bytes")
print()


# --------------------------------------------------
# REAL LIFE EXAMPLE 1
# PRODUCT STOCK
# --------------------------------------------------

stock = np.array(
    [100, 250, 50, 75],
    dtype=np.uint16
)

print("Product Stock:")
print(stock)
print("Datatype:", stock.dtype)
print()


# --------------------------------------------------
# REAL LIFE EXAMPLE 2
# IMAGE PIXELS
# --------------------------------------------------
# Image pixels usually uint8 hote hain
#
# 0   = Black
# 255 = White
# --------------------------------------------------

pixels = np.array(
    [0, 128, 255],
    dtype=np.uint8
)

print("Pixel Values:")
print(pixels)
print("Datatype:", pixels.dtype)
print()


# --------------------------------------------------
# IMPORTANT DIFFERENCE
# --------------------------------------------------
# int  = Positive + Negative
# uint = Only Positive
# --------------------------------------------------

signed = np.array(
    [-10, 20, 30],
    dtype=np.int16
)

print("Signed Integer Example:")
print(signed)
print("Datatype:", signed.dtype)
print()


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
#
# uint8  -> 0 to 255
# uint16 -> 0 to 65,535
# uint32 -> 0 to 4,294,967,295
# uint64 -> 0 to 18,446,744,073,709,551,615
#
# int  = Negative + Positive
# uint = Only Positive
#
# Most Common Uses:
# - Image Processing
# - Stock Quantity
# - Age
# - Marks
# - Counts
#
# --------------------------------------------------