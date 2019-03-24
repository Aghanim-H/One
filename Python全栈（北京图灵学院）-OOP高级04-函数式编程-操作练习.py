# 代码片段1
print("----代码片段1----")
# "小"的函数举例
def printA():
    print("AAAAAAAA")
printA()

# 代码片段2
print("----代码片段2----")
# lambda表达式的用法
# 1、以lambda开头
# 2、紧跟一定的参数（如果有的话）
# 3、参数后用冒号和表达式主题隔开
# 4、只是一个表达式，所以，没有return
# 计算一个数字的100倍数
stm = lambda x: 100 * x
# 使用上跟函数调用一模一样
print(stm(89))
stm2 = lambda x,y,z: x + y * 10 + z * 100
print(stm2(4,5,6))
# 怎么回事？打印出一个内存地址？
# 怎么无法输出结果 运行不起？？？

# 代码片段3
print("----代码片段3----")
# 变量可以赋值
a = 100
b = a
# 函数名称就是一个变量
def funA():
    print("In funA")
funB = funA
funB()

# 代码片段4
print("----代码片段4----")
# 高阶函数举例
# funA是普通函数，返回一个传入数字的100倍数字
def funA(n):
    return n * 100
# 再写一个函数，把传入参数乘以300倍，利用高阶函数
def funB(n):
    # 最终是想返回300n
    return funA(n) * 3
print(funB(9))

# 写一个高阶函数
def funC(n,f):
    # 假定函数是把n扩大100倍
    return f(n) * 3
print(funC(9,funA))
# 比较funC和funB，显然funC的写法要优于funB
# 例如：
def funD(n):
    return n * 10
# 需求变更，需要把n放大三十倍，此时funB则无法实现
print(funC(7,funD))

# 代码片段5
print("----代码片段5----")
# map举例
# 有一个列表，想对列表里的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)

# 利用map实现
def mulTen(n):
    return n * 10
l3 = map(mulTen,l1)
# map类型是一个可迭代的结构，所有可以使用for循环遍历
for i in l3:
    print(i)
# 以下列表生成式得到的结果为空，为什么？
l4 = [i for i in l3]
print(l4)

# 代码片段6
print("----代码片段6----")
from functools import reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd,[1,2,3,4,5,6])
print(rst)

# 代码片段7
print("----代码片段7----")
# 对于一个列表，对其进行过滤，偶数组成一个新列表
# filter案例
# 需要定义过滤函数
# 过滤函数要求有输入，返回布尔值
def isEven(a):
    return a % 2 == 0
l = [3,4,56,3,2,3,4556,67,4,4,3,23455,43]
rst = filter(isEven,l)
# 返回的filter内容是一个可迭代对象
print(type(rst))
print(rst)
print([i for i in rst])

# 代码片段8
print("----代码片段8----")
# 排序的案例
a = [234,22312,123,45,43,2,3,66723,34]
al = sorted(a,reverse = True)
print(al)
# 排序案例2
a = [-43,23,45,6,-23,2,-4345]
# 按绝对值进行排序
# abs是求绝对值的意思
# 即按照绝对值的倒序排列
al = sorted(a,key=abs,reverse=True)
print(al)

# sorted案例
astr = ['dana','Danaa','wangxiaojing','jingjing','haha']
str1 = sorted(astr)
print(str1)
str2 = sorted(astr,key=str.lower)
print(str2)

# 代码片段9
print("----代码片段9----")
# 定义一个普通函数
def myF(a):
    print('In myF')
    return None
a = myF(8)
print(a)
# 函数作为返回值返回，被返回的函数在函数体内定义
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3
# 使用上面定义
# 调用myF2，返回一个函数myF3，赋值给f3
f3 = myF2()
print(type(f3))
print(f3)
f3()

# 复杂一点的返回函数的例子
# args：参数列表
# 1、myF4定义函数，返回内部定义的函数myF5
# 2、myF5使用了外部变量，这个变量是myF4的参数
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5
f5 = myF4(1,2,3,4,5,6,7,8,9,0)
# f5的调用方式
f5()

f6 = myF4(10,20,30,40,50)
# f5的调用方式
f6()

# 代码片段10
print("----代码片段10----")
# 闭包常见坑
def count():
    # 定义列表，列表里面存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

# 代码片段11
print("----代码片段11----")
# 修改代码片段10的函数
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())

# 代码片段12
print("----代码片段12----")
def hello():
    print("Hello world")
hello()
f = hello
f()
# f和hello是一个函数
print(id(f))
print(id(hello))
print(f.__name__)
print(f.__name__)
# 现在有新的需求：
# 对hello功能进行扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# 这个功能就使用装饰器实现
# 任务：对hello函数进行功能扩展，每次执行hello前打印当前时间
import time
# 高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper
# 上面定义了装饰器，使用的时候需要用到@，此符号是python的语法糖
@printTime
def hello():
    print("Hello world")
hello()
# 装饰器的好处是，一但定义，则可以装饰任意函数
# 一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上
@printTime
def hello2():
    print("今天很高兴，被老板揪着讲课了")
    print("还可以有很多的选择")
hello2()

# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数
def hello3():
    print("我是手动执行的")
hello3()

hello3 = printTime(hello3)
hello3()
f = printTime(hello3)
f()
# 作业：解释上面代码的执行结果

# 代码片段13
print("----代码片段13----")
# 把字符串转化成十进制数字
int("12345")
help(int)
# 求八进制的字符串12345，表示成十进制的数字是多少
int("12345",base=8)
# 新建一个函数，此函数是默认输入的字符串是16进制数字
# 把此字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)
int16("12345")

import functools
# 实现上面int16的功能
int16 = functools.partial(int,base=16)
int16("12345")

# 代码片段14
print("----代码片段14----")
# zip案例
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(z)

for i in z:
    print(i)

l1 = ["wangwang","mingyue","yyt"]
l2 = [89,23,78]
z = zip(l1,l2)
for i in z:
    print(i)
# 考虑下面结果，为什么为空
l3 = [i for i in z]
print(l3)

# 代码片段15
# enumerate案例1
print("----代码片段15----")
l1 = [11,22,33,44,55]
em = enumerate(l1)
l2 = [i for i in em]
print(l2)

em = enumerate(l1,start=100)
l2 = [i for i in em]
print(l2)

# 代码片段16
print("----代码片段16----")
import collections
help(collections.namedtuple)
Point = collections.namedtuple("Point",['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(100,150,50)
print(c)
print(type(c))
# 想检测一下namedtuple到底属于谁的子类
print(isinstance(c,tuple))

# 代码片段17
# deque
print("----代码片段17----")
from collections import deque
q = deque(['a','b','c'])
print(q)
q.append('d')
print(q)

q.appendleft('x')
print(q)

# 代码片段18
print('----代码片段18----')
d1 = {"one":1,"two":2,"three":3}
print(d1['one'])
# print(d1['four'])  # 直接调用four没有，报错
from collections import defaultdict
# lambda表达式，直接返回字符串
func = lambda:"刘大拿"
d2 = defaultdict(func)
help(defaultdict)
d2["one"] = 1
d2["two"] = 2
print(d2['one'])
print(d2['four'])

# 代码片段19
print("----代码片段19----")
from collections import Counter
# 为什么下面结果不把abcdefg....作为键值，而是以其中每一个字母作为键值
# 需要括号内容为可迭代
c = Counter("abcdefgabcdeabcdabcaba")
print(c)
s = ["liudana","love","love","love","love","wangxiaona"]
c = Counter(s)
print(c)


















