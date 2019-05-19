# iter函数
from collections import Iterable
from collections import Iterator
s = "i love wangxiaojing"

print(isinstance(s,Iterable))
print(isinstance(s,Iterator))

s_iter = iter(s)

print(isinstance(s_iter,Iterable))
print(isinstance(s_iter,Iterator))