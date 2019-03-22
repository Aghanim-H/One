# 代码片段1
# "小"的函数举例
def printA():
    print("AAAAAAAA")
printA()

# 代码片段2
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
# 变量可以赋值
a = 100
b = a
# 函数名称就是一个变量
def funA():
    print("In funA")
funB = funA
funB()

# 代码片段4
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
from functools import reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd,[1,2,3,4,5,6])
print(rst)

# 代码片段7
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

# 代码片段9
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

# 代码片段10
# 修改代码片段9的函数
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







