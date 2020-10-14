
### [\*] Numpy

* Module used for scientific and mathematical computation.
* Much faster than traditional python list as:
  1. It stores data of same type, unlike python list(because of which python list has to store the object type as well which increases size), so no type-checking in Numpy.
  2. The data stored is in contigous format, so faster access time. (SIMD instruction + More cache hit than cache miss)
* Pandas relies on numpy for internal computation.

#### [\*] Code Intro

##### 1. Create & Dimensions
```python
>>> import numpy as np
>>> a = np.ones((2,3))  # Mention the dimensions as tuple
>>> a
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> np.array([[1,2,3],[4,5,6]])
array([[1, 2, 3],
       [4, 5, 6]])
>>> a = np.array([[1,2,3],[4,5,6]])
>>> print (a)
[[1 2 3]
 [4 5 6]]
>>> a.ndim      # number of dimensions
2
>>> a.shape     # rows and columns 
(2, 3)
>>> a.data
a.data
>>> a.data      # data object location
<memory at 0x7fb283153558>
>>> a.dtype     # data-type stored in array
dtype('int64')

# Can specify data-type explicitly, for precise memory usage
>>> b = np.array([1,2,3,4],dtype='int16')
>>> b.dtype
dtype('int16')
```

##### 2. Access data & update

```python
>>> a = np.array([[1,2,3,4,5,6,7],[7,6,5,4,3,2,1]])
>>> a
array([[1, 2, 3, 4, 5, 6, 7],
       [7, 6, 5, 4, 3, 2, 1]])
>>> a[0,0]
1
>>> a[0,6]
7
>>> a[0,1:]
array([2, 3, 4, 5, 6, 7])
>>> a[0,1:5]
array([2, 3, 4, 5])
>>> a[0,1:5:2]
array([2, 4])

# Update value
>>> a[1][2]     # or a[1,2]
5
>>> a[1,2] *= 100
>>> a[1,2]
500
>>> a
array([[  1,   2,   3,   4,   5,   6,   7],
       [  7,   6, 500,   4,   3,   2,   1]])

# Which means [] operator return value by reference
>>> for i in range(a.shape[0]):
...     for j in range(a.shape[1]):
...             a[i,j] += 10
... 
>>> a
array([[ 11,  12,  13,  14,  15,  16,  17],
       [ 17,  16, 510,  14,  13,  12,  11]])
```

##### 3. Other Functions

```python
>>> a = np.array([[1,2,3,4,5,6,7],[7,6,5,4,3,2,1]])

# Creates array of same shape with value passed
>>> b = np.full((3,2),2)
>>> b
array([[2, 2],
       [2, 2],
       [2, 2]])
>>> np.full_like(a,100)     # Creating array of same dimensions as other.
array([[100, 100, 100, 100, 100, 100, 100],
       [100, 100, 100, 100, 100, 100, 100]])

# Random array
>>> np.random.rand(4,2,3)       # 3D array with random values
array([[[0.62118815, 0.14472012, 0.43594259],
        [0.39794111, 0.07332652, 0.188229  ]],

       [[0.09735537, 0.30565586, 0.50399315],
        [0.26949172, 0.55125504, 0.08887944]],

       [[0.63856717, 0.44299177, 0.51256025],
        [0.1037059 , 0.58851134, 0.61270937]],

       [[0.74946221, 0.69184351, 0.75467418],
        [0.89182178, 0.47037403, 0.12459108]]])

# Int values b/w given range
>>> np.random.randint(-700,700,size=(3,3))
array([[-435,  389,  635],
       [ 143,  473, -107],
       [-349,  632, -129]])

>>> id(a)
140404678552752
>>> b = a   # Assignment is shallow-copy
>>> id(b)
140404678552752
>>> b[0][1] = -1
>>> a
array([[ 11,  -1,  13,  14,  15,  16,  17],
       [ 17,  16, 510,  14,  13,  12,  11]])

>>> b = a.copy()
>>> id(b)
140405078718224
```

##### 4. Mathematical Operations
* Arithmetic operations
```python
# The operators operates on the values inside the array.
>>> a = np.array([[1,2,3],[4,5,6]])
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
>>> a + 2
array([[3, 4, 5],
       [6, 7, 8]])
>>> a - 2
array([[-1,  0,  1],
       [ 2,  3,  4]])
>>> a * 2
array([[ 2,  4,  6],
       [ 8, 10, 12]])
>>> a/2
array([[0.5, 1. , 1.5],
       [2. , 2.5, 3. ]])
>>> np.sin(a)
array([[ 0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ]])
>>> a ** 2
array([[ 1,  4,  9],
       [16, 25, 36]])
```

* Linear Algebra 
```python
>>> a = np.ones((2,3))
>>> a
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> b = np.full((3,2),2)
>>> b
array([[2, 2],
       [2, 2],
       [2, 2]])
# Matrix multiplication
>>> np.matmul(a,b)     # Will throw exception if unable to multiply
array([[6., 6.],
       [6., 6.]])
```

* Statistics  

```python
>>> stats= np.array([[1,2,3],[4,5,6]])
>>> np.min(stats)
1
>>> np.max(stats)
6
>>> np.sum(stats)
21
>>> np.mean(stats)
3.5
>>> np.median(stats)
3.5
>>> np.var(stats)
2.9166666666666665
```

##### 5. Re-organising Array
* As long as the number of elements that can be stored in the dimension is same, it can easily re-shape the array.

```python
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
>>> new = a.reshape(6,1)
>>> new
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
>>> a.reshape(1,6)
array([[1, 2, 3, 4, 5, 6]])

# Stacking multiple arrays together
>>> v1 = a.copy()
>>> v2 = a.copy()+5
>>> v1
array([[1, 2, 3],
       [4, 5, 6]])
>>> v2
array([[ 6,  7,  8],
       [ 9, 10, 11]])
>>> np.vstack([v1,v2,v2,v1])
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [ 1,  2,  3],
       [ 4,  5,  6]])
>>> np.hstack([v1,v2,v2,v1])
array([[ 1,  2,  3,  6,  7,  8,  6,  7,  8,  1,  2,  3],
       [ 4,  5,  6,  9, 10, 11,  9, 10, 11,  4,  5,  6]])
```

##### 6. Miscellaneous
```python
# Read from file
    # Assume file content csv of numbers, number of columns in every row must be same
>>> filedata = np.genfromtxt("data.txt",delimiter=',')
>>> filedata
array([[ 24.,  58., -13., -51.,  16.,  15., -13.,  61.,  -3.,  63.,  45.,
         93.],
       [-47., -55., -49., -45.,  -4., -78., -58.,  -8., -30., -92.,  -6.,
         23.],
       [-57., -78., -50., -20.,  50., -43., -68.,  87.,  69., -94.,  48.,
         14.]])
>>> int_data = filedata.astype('int32')
>>> int_data
array([[ 24,  58, -13, -51,  16,  15, -13,  61,  -3,  63,  45,  93],
       [-47, -55, -49, -45,  -4, -78, -58,  -8, -30, -92,  -6,  23],
       [-57, -78, -50, -20,  50, -43, -68,  87,  69, -94,  48,  14]],
      dtype=int32)
>>> int_data > 50   # values greater than 50
array([[False,  True, False, False, False, False, False,  True, False,
         True, False,  True],
       [False, False, False, False, False, False, False, False, False,
        False, False, False],
       [False, False, False, False, False, False, False,  True,  True,
        False, False, False]])


>>> np.all(int_data > 50, axis=0)  # axis=0 means column-wise
array([False, False, False, False, False, False, False, False, False,
       False, False, False])
>>> np.all(int_data > -100, axis=1)  # axis=1 means column row-wise
array([ True,  True,  True])
>>> np.any(int_data > 90, axis=1)  # axis=1 means column row-wise
array([ True, False, False])
```
