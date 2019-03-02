'''
# 内置数据结构（或者叫变量类型）
    ·list：列表
        ·一组有顺序的数据的组合
        ·创建列表
            ·空列表
            ·见 代码片段1
        ·列表常用操作
            ·访问操作
                ·使用下标操作（索引）
                ·列表下标的位置是从0开始
                ·见 代码片段2
            ·分片操作
                ·分片操作是生成一个新的list
                    ·内置函数id，负责显示一个变量或者数据的唯一确定编号
                    ·见 代码片段4
                    ·通过id可以直接判断出分片是从新生成了一份数据还是使用的同一份数据？答案：是重新生成了一份数据
                    ·见 代码片段5
                ·对列表进行任意一段的截取：列表名称[:]
                ·下标值可以为空，如果不写，左边下标默认值为0，右边下标值为最大数加一，即表示截取至最后一个数据
                ·分片可以控制步长/步进，默认步长/步进为1
                ·下标可以超出范围，超出后不再考虑多余下标对应的内容
                ·下标值及步进/步长可以为负数，规定：列表最后一个值对应下标为-1。
                ·正下标：从左至右数0，1，2，3，……；负下标：从右至左数-1，-2，-3，-4，……
                ·正常情况下，分片左边的值一定要小于右边的值;如果分片一定左边值比右边大，则步进/步长参数需要使用负数
                ·见代码片段3
            ·del：删除命令
                ·如果使用del后，id的值和删除前不一样，则说明删除生成了一个新的list
                ·del一个变量后不能继续使用此变量
                ·见 代码片段6
            ·列表相加
                ·使用加号链接两个列表
                ·见 代码片段7
            ·使用乘号操作列表
                ·相当于把n个列表接在一起
                ·见 代码片段8
            ·成员资格运算
                ·就是判断一个元素是否在list里边
                ·见 代码片段9
            ·列表的遍历
                ·for
                ·while
                ·见 代码片段10
            ·双层列表循环
                ·见 代码片段11
            ·列表内涵：list content
                ·通过简单方法创作列表
                ·见 代码片段12
        ·关于列表的常用函数
            ·len：求列表长度
            ·list：将其他格式的数据转换成list
            ·append：插入一个内容，在末尾添加
            ·insert：指定位置插入，insert（index，data）：插入位置是index前面
            ·del：删除，指定位置
            ·pop：从对位拿出一个元素，即把最后一个元素拿出来
            ·remove：在列表中删除指定的值的元素，如果被删除的值没在list中，则报错，即，删除list指定值得操作应该使用try……excepty语句，或者先行进行判断
            ·clear：清空
            ·reverse：翻转,原地翻转，id一样
            ·extrnd：扩展列表，两个列表，把一个直接拼接到后一个上,id值不变
            ·count：查找列表中指定值或元素的个数
            ·copy：拷贝，浅拷贝
                ·深拷贝与浅拷贝的区别
                ·见 代码片段14
            ·见 代码片段13
    ·set：集合
        ·集合是高中数学中的一个概念
        ·一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素
        ·集合的特征
            ·集合内数据无序，即无法使用索引和分片
            ·集合内部数据元素具有唯一性，可以用来排除重复数据
            ·集合内的数据，str，int，float，tuple，冰冻集合等，即内部只能放置可哈希数据
            ·冰冻集合就是不可以进行任何修改的集合，frozen set是一种特殊的集合
                ·见 代码片段20
            ·集合遍历操作
            ·集合的内涵
        ·见 代码片段18
        ·关于集合的函数
            ·len，max，min：跟其他基本函数一致
            ·见 代码片段19
    ·dict
        ·字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现
            ·字典的创建
            ·见 代码片段21
            ·字典的特征
                ·字典是序列类型，但是是无序序列，所以没有索引和分片
                ·字典中的数据每个都有键值对组成，即kv对
                    ·key：必须是可哈希的值，比如int，string，float，tuple，但是，list，set，dict不行
                    ·value：任何值
                ·字典常见操作
                ·见 代码片段22
                ·字典相关函数
                    ·通用函数：len，max，min，dict
                    ·str（字典）：返回字典的字符串格式
                    ·clear：清空字典
                    ·items：返回字典的键值对组成的元组格式
                    ·key：返回字典的键组成的一个结构
                    ·values：同理，返回字典的值组成的一个结构，是一个可迭代的结构
                    ·get：根据指定键返回相应的值，get的好处是可以设置默认值
                    ·formkeys：使用指定的序列作为键，使用一个值作为字典的所有的键的值
                    ·见 代码片段23
        ·元组可以看成是一个不可更改的list
            ·元组创建
            ·见 代码片段15
            ·元组的特征特性
                ·是序列表，有序
                ·元组数据值可以访问，不能修改，不能修改，不能修改
                ·元组数据可以是任意类型
                ·总之，list所有特性，除了可修改之外，元组都具有
                ·也就意味着，list具有的一些操作，比如索引，分片，序列相加，相乘，成员资格操作等，一模一样
                ·见 代码片段16
            ·元组的函数
                ·基本跟list通用
                ·len：获取元组的长度
                ·max：最大值，如果列表或元组中有多个最大最小值，则实际打印出哪个？
                ·min：最小值
                ·以上函数，对list基本适用
                ·tuple：转化或创建元组
                ·count：计算指定数据出现的次数
                ·index：求指定元素在元组中的索引位置，如果要查找的值有多个相同，则返回第一个
                ·两个变量交换值
                ·见 代码片段17
'''

# 代码片段1
l1 = []
print(type(l1))  # type是内置函数，负责打印出变量的类型
print(l1)

l2 = [100]
print(type(l2))
print(l2)

l3 = [2,3,4,5,56,454,65,55444,6664,3,4,5,6,4444,5]
print(type(l3))
print(l3)

l4 = list()  # 使用list（）
print(type(l4))
print(l4)

# 代码片段2
l = [3,2,1,888,6,7,99]
print(l[3])
print(l[0])

# 代码片段3
print(l[1:3])  # 截取下标为1至下标为2（3-1）的值片段
print(l[:4])
print(l[2:])
print(l[1:6:2])  # 步进设置为2
print(l[2:20])
print(l[-4:-2])
print(l[-2:-4:-1])  # 此案例为一个list直接正反颠倒提供了一种思路

# 代码片段4
a = 100
b = 200
print(id(a))
print(id(b))
c = a
a = 101
print(id(a))
print(id(c))  # 如果a跟c指向同一个数据，则更改a的值同样也会更改c的值，但是显示结果并非如此，为什么？

# 代码片段5
# 如果两个id值一样，则表面分片产生的列表是使用的同一地址同一份数据，否则，则表明分片是重新生成了一份数据，即一个新的列表，然后把数值拷贝到新列表中
l = [33,0,44,2,55,3,66,4,77,5]
ll = l[:]
lll = ll
print(id(l))
print(id(ll))
print(id(lll))
# 通过id知道，ll和lll是同一份数据，验证如下：
l[1] = 1111
print(l)
print(ll)
ll[1] = 2222
print(ll)
print(lll)

# 代码片段6
a = [1,2,3,4,5,6]
del a[2]
print(a)
a = [1,2,3,4,5,6]
print(id(a))
del a[2]
print(id(a))
print(a)

# del a
# print(a)

# 代码片段7
a = [1,2,3,4,5]
b = [5,6,7,8,9]
d = ["a","b","c"]
c = a + b + d
print(c)

# 代码片段8
a = [1,2,3,4,5]
b = a*3
print(b)

# 代码片段9
c = b in a
print(c)
b = 4
print(b in a)
# not in
a = [1,2,3,4,5]
b = 9
print(b not in a)

# 代码片段10
a = [1,2,3,4,5]
for i in a:
    print(i)
# java,c++ 程序员写的python代码可能是这样的
'''
for i in range(0,len(a)):
    print(a[i])
    i += 1
'''
b = ["I love 王晓静"]
for i in b:
    print(i)
# range：in后面的变量要求是可以迭代的内容
for i in range(1,10):
    print(i)
print(type(range(1,10)))
# while循环访问list，一般不用while遍历list
a = [1,2,3,4,5,6]
length = len(a)
indx = 0  # indx表示的是list的下标
while indx < length:
    print(a[indx])
    indx += 1

# 代码片段11
a = [["one",1],["two",2],["three",3]]  # a为嵌套列表或者叫双层列表
for k,v in a:
    print(k,"------",v)

# 双层列表循环变异
# 这个例子说明，k，v，w的个数应该跟解包出来的变量个数一致
a = [["one",1,"eins"],["two",2,"skdfk"],["three",3,"ffffff"]]
for k,v,w in a:
    print(k,"<---->",v,"<---->",w)

# 代码片段12
a = ["a","b","c"]
b = [i for i in a]  # for创建；用list a创建一个list b；含义是：对于所有a中的元素，逐个放入新列表b中
print(b)

a = [1,2,3,4,5]
b = [i*10 for i in a]  # 对a中所有元素乘以10，生成一个新list
print(b)

# 还可以过滤原来list中的内容并放入新列表
a = [x for x in range(1,35)]  # 生成一个从1到34的一个列表
b = [m for m in a if m%2 == 0]  # 把a中所有偶数生成一个新的列表b
print(b)

# 列表生成式可以嵌套
a = [i for i in range(1,4)]
print(a)
b = [i for i in range(100,400) if i%100 == 0]
print(b)
c = [m+n for m in a for n in b]
print(c)
# 上面一段代码等价于此段代码
for m in a:
    for n in b:
        print(m+n,end=" ")
print()

# 嵌套的列表生成式也可以用条件表达式
d = [m+n for m in a for n in b if m+n < 250]
print(d)

# 代码片段13
a = [x for x in range(1,100)]
print(len(a))  # 求列表长度
print(max(a))  # 求列表中的最大值
print(min(a))  # 求列表中的最小值

b = ["man","film","python"]
print(max(b))

s = "I love wangxiaojing"
print(list(s))  # list：转换为list

print(list(range(12,19)))

a = [ i for i in range(1,5)]
print(a)
a.append(100)
print(a)
a.insert(3,666)
print(a)

last_ele = a.pop()
print(last_ele)
print(a)

print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))  # 输出两个id值一样，说明，remove操作是在原list直接操作

print(a)
print(id(a))
a.clear()
print(a)
print(id(a))  # 如果不必id值不变，清空列表可以使用a = []

a = [1,2,3,4,5]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))

a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))

a.append(8)
a.insert(4,8)
print(a)
a_len = a.count(8)
print(a_len)

# 列表类型变量赋值示例，list类型，简单赋值操作，是传地址。为了解决上述问题，list赋值需要采用copy函数。
a = [1,2,3,4,5,666]
print(a)
b = a
b[3] = 777
print(a)
print(b)

b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 30)
b[3] = 888
print(a)
print(b)

# 代码片段14
# 出现下列问题的原因是，copy函数是个浅拷贝函数，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1,2,3,[10,20,30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)

# 代码片段15
# 创建空元组
t = ()
print(type(t))
# 创建一个只有一个值的元组
t = (1,)  # 没有逗号为int
print(type(t))
print(t)
t = 1,
print(type(t))
print(t)
# 创建多个值的元组
t = (1,2,3,4,5)
print(type(t))
print(t)
t = 1,2,3,4,5
print(type(t))
print(t)
# 使用其他结构创建
l = [1,2,3,4,5]
t = tuple(l)
print(type(t))
print(t)

# 代码片段16
# 索引操作
t = (1,2,3,4,5,6)
print(t[4])
# print(t[12])  # 超标错误,切片可以超标
t1 = t[1::3]
print(id(t))
print(id(t1))
t2 = t[2:100]  # 切片可以超标
print(t2)
# 序列相加
t1 = (1,2,3)
t2 = (5,6,7)
# 传址操作
print(t1)
print(id(t1))
t1 = t1 + t2
print(t1)
print(id(t1))
# 以上操作类似于
t1 = (1,2,3)
t1 = (2,3,4)
# tuple的不可修改，指的是内容的不可修改
# t1[1] = 100  # 修改tuple内容会导致报错
# 元组相乘
t = (1,2,3,9)
t = t * 3
print(t)
# 成员相乘
t = (1,2,3)
if 2 in t:
    print("yes")
else:
    print("no")
# 元组遍历，一般采用for
# 1、单层元组遍历
t = (1,2,3,"wangxiaojing","i","love")
for i in t:
    print(i,end=" ")
print()
# 2、双层元组遍历
t = ((1,2,3),(2,3,4),("i","love","wangxiaojing"))
for i in t:  # 第一种
    print(i)
for k,m,n in t:  # 第二种
    print(k,"----",m,"----",n)

# 代码片段17
t = (1,2,3,4,5)
len(t)
print(max(t))
print(min(t))

l = [1,2,3,4,5]
t = tuple(l)
print(t)
t = tuple()
print(t)

t = (2,1,2,3,45,1,1,2,)
print(t.count(2))
print(t.index(45))
print(t.index(1))

# 两个变量交换值
a = 1
b = 3
print(a)
print(b)
print("-" * 10)
# java程序员会这么写
c = a
a = b
b = c
print(a)
print(b)
print("*" * 10)
# python写法
a,b = b,a
print(a)
print(b)

# 代码片段18
# 集合的定义
s = set()
print(type(s))
print(s)

s = {1,2,3,4,5,6,7}  # 此时，大括号内一定要有值，否则定义出的是一个dict

d = {}
print(type(d))
print(d)

# 集合序列操作
# 成员检测，in，not in
s = {4,5,"i","love","wangxiaojing"}
print(s)
if "love" in s:
    print("爱呀")
if "haha" not in s:
    print("爱个锤子")
# 集合遍历操作
s = {4,5,"i","love","wangxiaojing"}
for i in s:
    print(i,end=" ")
# 带有元组的集合遍历
s = {(1,2,3),("i","love","wangxiaojing"),(4,5,6)}
for k,m,n in s:
    print(k,"----",m,"----",n)
for k in s:
    print(k)
# 集合的内涵
# 普通集合内涵
# 以下集合在初始化后自动过滤掉重复元素
s = {23,223,545,3,1,2,3,4,3,2,3,1,2,4,3}
print(s)

ss = {i for i in s}
print(ss)

# 带条件的集合内涵
sss = {i for i in s if i%2 == 0}
print(sss)

# 多循环的集合内涵
s1 = {1,2,3,4}
s2 = {"i","love","wangxiaojing"}
s = {m*n for m in s2 for n in s1}
print(s)

s = {m*n for m in s2 for n in s1 if n == 2}
print(s)

# 代码片段19
s = {43,23,56,223,4,2,1222,4,323,1}
print(len(s))
print(max(s))
print(min(s))
# set：生成一个集合
l = [1,2,3,4,3,23,1,2,3,4]
s = set(l)
print(s)
# add：向集合内添加元素
s = {1}
s.add(334)
print(s)
# clear。结果表明clear函数是原地清空数据
s = {1,2,3,4,5}
print(id(s))
s.clear()
print(id(s))
# copy：拷贝
# remove：移除指定的值，直接改变原有值，如果要删除的值不存在，报错
# discard：移除集合中指定的值，跟remove一样，但是如果要删除的话，不报错
s = {23,3,4,5,1,2,3}
s.remove(4)
print(s)
s.discard(1)
print(s)
print("*" * 20)
s.discard(1100)
print(s)
# s.remove(1100)  #报错，为啥remove不存在的值会报keyerror？因为哈希
# print(s)  # 报错
# pop：随机移除一个元素
s = {1,2,3,4,5,6,7}
d = s.pop()
print(d)
print(s)
# intersection：交集
# difference：差集
# union：并集
# issubset：检查一个集合是否为另一个子集
# issuperset：检查一个集合是否为另一个超集
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
s_1 = s1.intersection(s2)
print(s_1)
s_2 = s1.difference(s2)
print(s_2)
s_3 = s1.issubset(s2)
print(s_3)
# 集合的数学操作
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
s_4 = s1 - s2
print(s_4)

# 代码片段20
# frozen set:冰冻集合
s = frozenset()
print(type(s))
print(s)

# 代码片段21
# 创建空字典
d = {}
print(d)

d = dict()
print(d)

# 创建有值得字典，每组数据用冒号隔开，每一对键值对用逗号隔开
d = {"one":1,"two":2,"three":3}
print(d)
# 用dict创建有内容字典1
d = dict({"one":1,"two":2,"three":3})
print(d)
# 用dict创建有内容字典2
# 利用关键字参数
d = dict(one=1,two=2,three=3)
print(d)

d = dict([("one",1),("two",2),("three",3)])
print(d)

# 代码片段22
# 访问数据
d = {"one":1,"two":2,"three":3}
# 注意访问格式
# 中括号内是键值
print(d["one"])
d["one"] = "dmdmfm"
print(d)

# 删除某个操作，使用del操作
del d["one"]
print(d)

# 成员检测，in，not in。成员检测检测的是key内容
d = {"one":1,"two":2,"three":3}
if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d:
    print("kv")

# 遍历在python 2 和python 3 中区别比较大，代码不适用
# 按key来使用for循环，直接按key值访问
d = {"one":1,"two":2,"three":3}
for k in d:
    print(k,d[k])
# 上述代码可以改写如下：
for k in d.keys():
    print(k,d[k])
# 只访问字典的值
for v in d.values():
    print(v)
# 还可以这样写，注意此种为特殊用法
for k,v in d.items():
    print(k,"----",v)

# 字典生成式
d = {"one":1,"two":2,"three":3}
# 常规字典生成式
dd = {k:v for k,v in d.items()}
print(dd)
# 加限制条件的字典生成式
dd = {k:v for k,v in d.items() if v%2 == 0}
print(dd)

# 代码片段23
d = {"one":1,"two":2,"three":3}
print(str(d))

i = d.items()
print(type(i))
print(i)

k = d.keys()
print(type(k))
print(k)

v = d.values()  # 注意是values而不是value！
print(type(v))
print(v)

# get默认值是None，可以设置
d = {"one":1,"two":2,"three":3}
print(d.get("on33"))
print(d.get("one",100))
print(d.get("on333",100))
# print(d["on33"])  # 报错

# formkeys
# 注意formkeys的两个参数的类型
# 注意fromkeys的调用主体
l = ["eins","zwei","dree"]
d = dict.fromkeys(l,"hahahahhahaaaa")
print(d)








# 传值和传地址的区别
# 对于简单的数值，采用传值操作，即在函数内对参数的操作不影响外面的变量
# 对于复杂变量，采用传地址操作，此时函数内的参数和外部变量是同一份内容，任何地方对此内容的更改都影响另外的变量或参数的使用
def a(n):
    n[2] = 300
    print(n)
    return None

def b(n):
    n +=100
    print(n)
    return None

an = [1,2,3,4,5,6]
bn = 9
print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)






