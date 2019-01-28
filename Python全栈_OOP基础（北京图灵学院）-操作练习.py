'''
定义一个学生类，用来形容学生
'''
# 代码片段1
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过，此处pass必须有
    pass
# 定义一个对象
mingyue = Student()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    coure = "Python"
    # 需要注意：1、def doHomework的缩进层级；2、系统默认有一个self参数。
    def doHomework(self):
        print("I 在做作业")
        # 推荐在函数末尾使用return
        return None
# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()

# 代码片段2
class Student():
    name = "dana"
    age = 18
Student.__dict__
# 实例化
yueyue = Student()
yueyue.__dict__
print(yueyue.name)

# 代码片段3
class A():
    name = "dana"
    age = 18
    # 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
# 此案例说明，类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量
# 此时，A称为类实例
print(A.name)
print(A.age)
print("*" * 20)
# id可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.name))
print(id(A.age))
print("*" * 20)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print(A.name)
print(A.age)
print("*" * 20)
print(id(A.name))
print(id(A.age))
print("*" * 20)
a = A()
print(A.__dict__)
print(a.__dict__)
a.name = "yaona"
a.age = 16
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

# 代码片段4
class Student():
    name = "dana"
    age = 18
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
yueyue = Student()
yueyue.say()

class Student():
    name = "dana"
    age = 18
    def sayAgain(s):
        s.name = "bbbb"
        s.age = 20
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))
yueyue = Student()
yueyue.sayAgain()

class Teacher():
    name = "dana"
    age = 19
    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
        # 调用类的成员变量需要用 __class__
        print("My Age Is {0}".format(__class__.age))
    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print("Hello,nice to see you again")
t = Teacher()
t.say()
# 调用绑定类函数使用类名
# t.sayAgain()  # 此代码会报错
Teacher.sayAgain()

# 关于self的案例
class A():
    name = "liuying"
    age = 18
    def __init__(self):
        self.name = "aaaa"
        self.age = 200
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = "bbbb"
    age = 90
a = A()
a.say()  # 此时，系统会默认把a作为第一个参数传入函数
A.say(a)  # 此时self被a替换
# A.say()  # 会报错
A.say(A)  # 同样可以把A作为参数传入
A.say(B)  # 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
# 以上代码，利用了鸭子模型

# 代码片段5
# 私有变量案例
class Person():
    # name是共有的成员
    name = "liuying"
    # __age就是私有成员
    __age = 18
p = Person()
print(p.name)  # name是公有变量
# print(p.__age)  # __age是私有变量，注意报错信息
# name mangling技术
print(Person.__dict__)
p._Person__age = 19
print(p._Person__age)









































