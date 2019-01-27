'''
定义一个学生类，用来形容学生
'''
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

class Student():
    name = "dana"
    age = 18
Student.__dict__
# 实例化
yueyue = Student()
yueyue.__dict__
print(yueyue.name)

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






















