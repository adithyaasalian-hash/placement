import numpy as np
a=np.array([10,20,30,40])
print(a)
print(type(a))
print(np.array(a))
print(a.shape)
print(np.array(a).dtype)
a=[10,20,30,40]
print(a)
import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
print(a)
print(type(a))
print(np.array(a))
print(a.shape)
print(np.array(a).dtype)
import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[4,5,6],[6,7,8]])
print(a1+a2)
print('------------------------')
print(a1*a2)
print('------------------------')

print(a1-a2)
print('------------------------')

print(a1/a2)
print('------------------------')

print(np.min(a1))
print('------------------------')
print(np.max(a1))
print('------------------------')

print(np.mean(a1))
print('------------------------')


print(a1>5)
print('------------------------')

print(a1<5)
print('------------------------')

print(a2>5)
print('------------------------')

print(a2<5)
print('------------------------')
print(a2&a1)
print('------------------------')

print(a2|a1)
print('------------------------')
print(np.sum(a1,axis=0))
print('------------------------')
print(np.sum(a1,axis=1))
print('------------------------')
print(np.sum(a1))
print('------------------------')
print(np.sum(a1,axis=1))

import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[4,5],[2,3],[7,8]])
print(np.array(a1@a2))
print(np.matmul(a1,a2))