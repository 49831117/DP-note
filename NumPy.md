# NumPy

----

- **觀察資料**
    1. `.ndim` 陣列維度個數（有多少個 dimension？）
    2. `.shape` 陣列每個維度的大小（行數、列數等）
    3. `.dtype.name` 描述陣列中元素類型的物件
    4. `.itemsize` 陣列中每個元素的位元組大小
    5. `.size` 陣列元素的總數
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




- **常用函數**

  `all`、`any`、`apply_along_axis`、`argmax`最大值的索引值、`argmin`最小值的索引值、`argsort`、`average`、
  `bincount`
  `ceil`、`clip`、`conj`、`corrcoeof`、`cov`、`cross`、`cumprod`、`cumsum`、
  `diff`差值、`dot`、
  `floor`、
  `inner`、`lexsort`、
  `max`、`maximum`、`mean`、`median`、`min`、`minimum`、`nonzero`、
  `outer`、
  `prod`、
  `re`、`round`、
  `sort`、`std`、`sum`、
  `trace`、
  `var`、`vdot`、`vectorize`、
  `where`

  -  中位數優於平均數：可以避開雜訊


- **NumPy 的運算**
  
  `+` array 相加 
  `-` array 相減
  `*` 各元素相乘
  `**` 各元素次方
  `np.dot(a, b)` ≡ `a.dot(b)` ≡ `a @ b` 矩陣內積
  `np.sum(b)` 所有元素的和
  `np.min(b)` 所有元素的最小值
  `np.max(b)` 所有元素的最大值
  `np.sum(b, axis = 1)` 各 axis = 1 的和（各 row 列的和）
  `np.sum(b, axis = 0)` 各 axis = 0 的和（各 column 行的和）



### Question 1. 複本?
```python
c = a.view()
print(c is a) # False
print(c.base is a) # True
print(c.flags.owndata) # False

c.shape = 2, 6
print(a.shape) # (3, 4)

c[0, 4] = 1234
print(a) # a's data changed.
```


