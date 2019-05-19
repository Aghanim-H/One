# isinstance案例
# 判断某个变量是否是一个实例
#判断是否可迭代
from collections import Iterable
ll = [1,2,3,4,5]

print(isinstance(ll,Iterable))

from collections import Iterator
print(isinstance(ll,Iterator))
