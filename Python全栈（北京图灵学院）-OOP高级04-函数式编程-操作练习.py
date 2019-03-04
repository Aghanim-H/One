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
stm(89)
print(stm)
stm2 = lambda x,y,z: x + y * 10 + z * 100
stm2(4,5,6)
print(stm2)
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




































