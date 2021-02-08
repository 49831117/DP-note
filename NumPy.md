# NumPy

----

- **觀察資料**
    1. `.shape`
    2. `.ndim`
    3. `.dtype.name`
    4. `.itemsize`
    5. `.size`
    6. `type(a)`

- **row and column**
  1. n row, 1 column
    ```python
    np.arange(n)
    ```
  2. n row (axis = 0), m column (axis = 1)
    ```python
    np.array([
        [a11, a12, a13, ..., a1n], 
        [a21, a22, a23, ..., a2n],
        ...
        [am1, am2, am3, ..., amn]
    ])
    ```
  3. `ndarray[0]` 指 axis = 0 的第 0 項
  4. `ndarray[0][:]` 指 axis = 0 對應 axis = 1 的全部
  > `ndarray[axis = 0][axis = 1]`