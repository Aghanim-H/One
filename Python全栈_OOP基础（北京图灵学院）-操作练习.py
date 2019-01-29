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

# 代码片段6
# 继承的语法
# 在python中，任何类都有一个共同的父类叫object
class Person():
    name = "NoName"
    age = 0
    def sleep(self):
        print("Sleeping …… ……")
# 父类写在括号内
class Teacher(Person):
    def make_test(self):
        pass

t = Teacher()
print(t.name)
print(Teacher.name)

class person():
    name = "NoName"
    age = 0
    __score = 0  # 考试成绩是秘密，只要自己知道
    _petname = "sec"  # 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping …… ……")
# 父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    def make_test(self):
        print("attention")

t = Teacher()
print(t.name)
# 受保护不能外部访问，为啥这里可以
# print(t._petname)
# 私有访问问题，公开访问私有变量，报错
# print(t.__score)

t.sleep()
print(t.teacher_id)
t.make_test()

# 子类和父类定义了同一个名称变量，则优先使用子类本身的变量
class person():
    name = "NoName"
    age = 0
    __score = 0
    _petname = "sec"
    def sleep(self):
        print("Sleeping …… ……")
class Teacher(Person):
    teacher_id = "9527"
    name = "Dana"
    def make_test(self):
        print("attention")
t = Teacher()
print(t.name)

# 子类扩充父类功能的案例
# 人有工作的函数，老师也有工作的函数，但老师的工作需要讲课
class Person():
    name = "NoName"
    age = 0
    __score = 0
    _petname = "sec"
    def sleep(self):
        print("Sleeping …… ……")
    def work(self):
        print("make some money")
class Teacher(Person):
    teacher_id = "9527"
    name = "Dana"
    def make_test(self):
        print("attention")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        # Person.work(self)  # 方法一，注意需传入一个参数，这里传入的为self
        super().work()  # 方法二，super代表得到父类
        self.make_test()
t = Teacher()
t.work()

# 构造函数的概念
# __init__就是构造函数，每次实例化的时候，第一个被自动调用，因为主要工作是进行初始化，所以得名
class Dog():
    def __init__(self):
        print("I am init in dog")
# 实例化的时候，括号内的参数需要跟构造函数参数匹配
kaka = Dog()

# 继承中的构造函数1
class Animal():
    pass
class PaxinAni(Animal):
    pass
class Dog(PaxinAni):
    def __init__(self):
        print("I am init in dog")
# 实例化的时候，自动调用了Dog的构造函数
kaka = Dog()

# 继承中的构造函数2
class Animal():
    def __init__(self):
        print("Animal")
class PaxinAni(Animal):
    def __init__(self):
        print("Paxing Dongwu")
class Dog(PaxinAni):
    def __init__(self):
        print("I am init in dog")
# 实例化的时候，自动调用了Dog的构造函数,因为找到了构造函数，则不再查找父类的构造函数
kaka = Dog()
# 猫没有写构造函数
class Cat(PaxinAni):
    pass
# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数,在PaxingAni中查到了构造函数，则停止向上查找
c = Cat()

# 继承中的构造函数3
class Animal():
    def __init__(self):
        print("Animal")
class PaxinAni(Animal):
    def __init__(self,name):
        print("Paxing Dongwu {0}".format(name))
class Dog(PaxinAni):
    def __init__(self):
        print("I am init in dog")
d = Dog()  # 实例化Dog时，查找到Dog的构造函数，参数匹配，不报错
# class Cat(PaxinAni):
#     pass
# c = Cat()  # 此时，由于Cat没有构造函数，则向上查找。因为PaxinAni的构造函数需要两个参数，实例化的时候只给了一个，报错

# 继承中的构造函数4
class Animal():
    def __init__(self):
        print("Animal")
class PaxinAni(Animal):
    pass
class Dog(PaxinAni):
    pass
d = Dog()
class Cat(PaxinAni):
    pass
c = Cat()

# super是一个类
print(type(super))
help(super)

















