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
    ·dict
    ·tuple：元组
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






