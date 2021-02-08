#1
import numpy as np
a = np.arange(15)
print("a = np.arange(15):", a)
a=a.reshape(3, 5)
print("a.reshape(3, 5):",a,sep="\n")

#2
print("a.shape=",a.shape)
print("a.ndim=",a.ndim)
print("a.dtype.name=",a.dtype.name)
print("a.itemsize=",a.itemsize)
print("a.size=",a.size)
print("type(a)=",type(a))

#3
b = np.array([6, 7, 8])
print(b)
print("type(b)=",type(b))

#18
import numpy as np
array = np.array([[1,2,3],[2,3,4]])
print(array)

#19
import numpy as np
a = np.array([2,3,4])
print("a=", a)
print("a.dtype:",a.dtype)
b = np.array([1.2, 3.5, 5.1])
print("b=", b)
print("b.dtype:", b.dtype)

