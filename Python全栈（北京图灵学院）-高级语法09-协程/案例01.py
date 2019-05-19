# 可迭代
l = [i for i in range(10)]

# l是可迭代的，但不是迭代器
for idx in l:
    print(idx)

# range是个迭代器
for i in range(5):
    print(i)