"""
#函数
    工程思想、模块化
    ·代码的一种组织形式
    ·一个函数一般完成一项特定的功能
    ·函数使用
        ·函数需要先定义，只是定义的话函数不会执行
        ·使用函数，俗称调用
            ·直接函数名后面跟括号
        ·def关键字，后跟一个空格
        ·函数名，自己定义，起名需要遵循命名规则，约定俗成，大驼峰命名只给类用
        ·后面括号和冒号不能省，括号内可以有参数
        ·函数内所有代码缩进
        ·见 代码片段1
    ·函数的参数和返回值
        ·参数：负责给函数传递一些必要的数据或者信息
            ·形参（形式参数）：在函数定义的时候用到的参数，没有具体值，只是一个占位的符号，称为形参
            ·实参（实际参数）：在调用函数的时候输入的值
            ·参数分类
                ·普通参数
                    ·参见代码片段2。定义的时候直接定义变量名。调用的时候直接把变量或者值放入指定位置。
                        def 函数名（参数1，参数2，……）
                            函数体
                        调用：调用的时候，具体值参考的是位置，按位置赋值
                        函数名（value1，walue2，……）
                ·默认参数
                    ·形参带有默认值。调用的时候，如果没有对相应参数赋值，则使用默认值。
                        def func_name(p1=v1,p2=v2,……):
                            func_bloc
                        调用1
                            func_name()
                        调用2
                            value1 = 100
                            value2 = 200
                            func_name(value1,value2)
                    ·见 代码片段6
                ·关键字参数
                    ·语法
                        def func(p1=v1,p2=v2,……)
                            func_body
                        调用函数：
                        func(p1=value1,p2=value2……)
                    ·比较麻烦，但是也有好处：不容易混淆，一般实参和形参只是按照位置一一对应即可，容易出错，使用关键字参数，可以不考虑参数位置。
                    ·见 代码片段7
                ·收集参数
                    ·把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
                    ·语法：
                        def func(*args):
                            func_body
                            # 按照list使用方式访问args得到传入的参数
                        调用：
                        func(p1,p2,p3,……)
                    ·参数名args不是必须这么写，但是我们推荐直接使用args，约定俗成
                    ·参数名args前面需要有星号
                    ·收集参数可以和其他参数共存
                    ·见 代码片段8
                    ·收集参数之关键字收集参数
                        ·把关键字参数以字典的格式存入收集参数
                        ·语法：
                            def func(**kwargs):
                                func_body
                            调用：
                            func(p1=v1,p2=v2,p3=v3,……)
                        ·kwargs 用此词一般约定俗成
                        ·调用的时候，把多余的关键字参数放入kwargs
                        ·访问kwargs需要按字典格式访问
                        ·见 代码片段9
                    ·收集参数混合调用的顺序问题
                        ·收集参数，关键字参数，普通参数可以混合使用
                        ·使用规则就是，普通参数和关键字参数优先
                        ·定义的时候一般按顺序找普通参数，关键字参数，收集参数tuple，收集参数dict
                        ·见 代码片段10
                    ·收集参数的解包问题
                        ·把参数放入list或者dict中，直接把list/dict中的值放入收集参数中
                        ·语法：
                            ·见 代码片段11
        ·返回值：函数的执行结果
            ·使用return关键字
            ·如果没有return，默认返回一个none
                ·见 代码片段3
            ·函数一旦执行return语句，则无条件返回，即结束函数的执行
                ·见 代码片段4
        ·参数的定义和使用
        ·见 代码片段2
    ·查找函数帮助文档
        ·见 代码片段5
"""

# 代码片段1
def func():
    print("我是一个函数")
    print("我要完成一定功能")
    print("我结束了")
func()

# 代码片段2
# 参数person只是一个符号，代表的是调用的时候的某一个数据
# 调用的时候，会用p的值代替函数中的所有的person
def hello(person):
    print(" {0},你怎么了".format(person))
    print("Sir,你不理我我就走了")
p = "明月"
hello(p)

# 代码片段3
# return语句的基本使用。函数打完招呼后返回一句话
def hello(person):
    print(" {0},你怎么了".format(person))
    print("Sir,你不理我我就走了。")
    return "我已经跟 {0} 打完招呼了， {1} 不理我。".format(person,person)
p = "明月"
rst = hello(p)
print(rst)

# 代码片段4
def hello(person):
    print(" {0},你怎么了".format(person))
    return "哈哈，我提前结束了"
    print("Sir,你不理我我就走了。")
    return "我已经跟 {0} 打完招呼了， {1} 不理我。".format(person,person)
p = "东东"
rst = hello(p)
print(rst)

# 九九乘法表
# print函数默认任务打印完毕后换行
for row in range(1,10):
    for col in range(1,row+1):
        #={2}等号之前留两个空格就对不齐，留其他个数的空格都能对齐？
        print("{1}*{0}={2}".format(row,col,row*col),end="\t")
    print()
# 代码片段5
# help(print)

# 代码片段6
# 报名函数，需要知道学生性别。学习python的学生基本都是男生，所以，报名的时候如果没有特别指定，我们认为是男生
def reg(name,age,gender="male"):
    if gender == "male":
        print("{0} is {1} years old,and he is a good student".format(name,age))
    else:
        print("{0} is {1} years old,and she is a good student".format(name,age))

reg("mingyue",21)
reg("xiaojing",23,"female")

# 代码片段7
# 普通参数及调用法
def stu(name,age,addr):
    print("I am a student")
    print("我叫{0},我今年 {1} 岁了，我住{2}".format(name,age,addr))

n = "jingjing"
a = 18
addr = "大石坝"
stu(a,n,addr)  # 普通参数，只按照位置传递，容易出错
stu(name=n,age=a,addr=addr)  # 普通参数，只按照位置传递，容易出错
# 关键字参数及调用法
def stu_keyword(name="No name",age=0,addr="No addr"):
    print("我是个学生！")
    print("我叫{0},我今年{1}岁了，我家住在{2}".format(name,age,addr))

h = "大东"
b = 15
j = "观音桥"
stu_keyword(age=b,addr=j,name=h)

# 代码片段8
# 函数模拟一个学生进行自我介绍，但具体内容不清楚。把args看成一个列表
def stu(*args):
    print("Hello 大家好，我自我介绍一下，简单说两句：")
    print(type(args))
    for item in args:
        print(item)

stu("liuying",18,"重庆沙坪坝区","wangxiaojing","single")
stu("周大生")
stu()  # 收集参数可以不带任何参数调用，此时收集参数为空tuple
# stu(name="liuying")  # 如果使用关键字参数格式调用，会出现问题

# 代码片段9
# 自我介绍，调用的时候需要使用关键字参数调用
def stu(**kwargs):
    # 在函数体内对于kwargs的使用不用带星号
    print("Hello 大家好，很高兴认识大家，我先自我介绍一下：")
    print(type(kwargs))
    # 对于字典的访问，python2和python3有区别
    for k,v in kwargs.items():
        print(k,"------",v)

stu(name="小红",age=19,addr="重庆江北区",lover="王晓静",work="Teacher")
print("-------------")
print("+"*20)
stu(name="周大大大")
stu()  # 收集参数可以为空

# 代码片段10
def stu(name,age,*args,hobby="没有",**kwargs):
    print("Hi 大家好！！！")
    print("我叫{0},我今年{1}岁了。".format(name,age))
    if hobby == "没有":
        print("我没有爱好，很遗憾！")
    else:
        print("我的爱好是{0}".format(hobby))
    print("*"*20)
    for i in args:
        print(i)
    print("#"*30)
    # 字典用法请注意.items()
    for k,v in kwargs.items():
        print(k,"-----",v)

name = "小小明明"
age = 18
# 不同格式的调用
stu(name,age)
stu(name,age,hobby="游泳")
stu(name,age,"王晓静","刘小毛",hobby="游泳",hobby2="烹饪",hobby3="看书读报")

# 代码片段11
def stu(*args):
    print("hahhahaahhhh")
    n = 0  # n用来表示循环次数，主要用来调试
    for i in args:
        print(type(i))
        print(i)
        n += 1
        print(i)

# stu("小花花","大明明",19,200)
l = ["小胖胖",19,23,"李甜甜"]
stu(l)





