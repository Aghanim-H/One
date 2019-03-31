# 代码片段1
print("----代码片段1----")
# 使用shelve创建文件并使用
import shelve
# 打开文件，shv相当于一个字典
shv = shelve.open(r"shv.db")
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()
# 通过以上案例发现，shelve自动创建的不仅仅是一个shv.db文件，还包括其他格式文件

# shelve读取案例
shv = shelve.open(r"shv.db")
try:
    print(shv['one'])
    print(shv['three'])
except Exception as e:
    print("烦死了")
finally:
    shv.close()

# 代码片段2
print("----代码片段2----")
# shelve之只读打开
import shelve
shv = shelve.open(r'shv.db',flag='r')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

import shelve
shv = shelve.open(r'shv.db')
try:
    shv['one'] = {'eins':1,'zwei':2,'drei':3}
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()
# shelve忘记写会，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1['eins'] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

# shelve忘记写会，需要使用强制写回2  writeback
shv = shelve.open(r'shv.db',writeback=True)
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1['eins'] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

# shelve使用with管理上下文环境
with shelve.open(r'shv.db',writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    k1['eins'] = 1000
with shelve.open(r'shv.db') as shv:
    print(shv['one'])