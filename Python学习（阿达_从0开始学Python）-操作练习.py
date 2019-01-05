print("Hello World!")
# 从0开始学python-2.2python里的数字
a=3
print(a)
a=5
print(a)
a=3+2
print(a)
a=a+2
print(a)
# 从0开始学python-2.3 字符串与布尔
a="hello world"
print(a)
a="你好！世界"
print(a)
a="Python is beautiful language"
print(a)
a="Python是美丽的语言"
print(a)
# 取长度
a="www.google.com"
print(a)
b=len(a)
print(b)
# 取长度
a="I love Python"
b=len(a)
print(b)
# 取子字符串
a="我们一定要好好学习，天天向上"
b=a[0]
c=a[2]
d=a[5:9]
print(b,c,d)
# 字符串拼接
a="我们一定要好好学习，天天向上,"
b="才能做到有一天金榜题名。"
c=a+b
print(c)
# 字符串替换
a="我们一定要好好学习，天天向尚"
b=a.replace("尚","上")	
print(a,b)
# 布尔值
a=True
b=False
print(a,b)
# 从0开始学python-3.1 列表容器
a=[1,3,5,7,9]
hero=["阿珂","韩信","李白"]
book_list=["海贼王","叮当猫","老夫子"]
# 获取列表长度
A=len(book_list)
print(A)
# 往列表里添加元素
book_list.append("西游记")
print(book_list)	
# 获取列表里的元素
B=book_list[1]
print(B)
# 更改列表里某个位置元素的值
book_list[0]="七龙珠"
print(book_list)	
# 获取多个元素
C=book_list[1:3]
print(C)
# 删除列表里的元素
book_list.remove("叮当猫")
print(book_list)	
# 判断列表里是否包含某个元素（注意in前后空格）
D="海贼王" in book_list
print(D)
# 列表排序，默认是从小到大
E=[3,14,798,54,888,99,4000,567483,1,4,0]
E.sort()
print(E)
# 从0开始学python-3.2 字典与数据总结 字典（Map）：key:value键值对，大括号{}
a={"小明":"10岁","阿达":"12岁","Tom":"15岁"}
b={'小漠漠': '13750823822', '自由飞翔': '13528281235', 'jackson': '15027728853'}
# 查看有多少个好友
len(a)
print(len(a))
# 获取某个好友的个人信息
F=b["jackson"]
print(F)
print(b["jackson"])
# 判断某个人是否在通讯录里
print("jackson" in b)
# 更改某个好友的个人信息
b["jackson"]='13322331212'
print(b)
# 删除某个好友(注意使用的是小括号，列表用remove，字典用pop)
b.pop("jackson")
print(b)
# 从0开始学python-4.1条件语句
# 我们把 == 叫做判断运算符，判断运算符还有：!=;>=;<=
# 注意句式：一定记到加冒号以及缩进，不缩进则代表该行不属于条件语句的语句体
# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……
weather="下雨"
if weather=="下雨":
	print("记得带伞")
	print("记得带伞~~")
print("玩儿去咯")

flag = False
name = 'luren'
if name == 'python':     # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print("welcome boss")  # 并输出欢迎信息
else:
    print(name)             # 条件不成立时输出变量名称

num = 5     
if num == 3:            # 判断num的值
    print("boss")        
elif num == 2:
    print("user")
elif num == 1:
    print("worker")
elif num < 0:           # 值小于零时输出
    print("error")
else:
    print("roadman")     # 条件均不成立时输出

num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print("hello")
num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print("hello")
else:
    print("undefine")
num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    # 判断值是否在0~5或者10~15之间
    print("hello")
else:
    print("undefine")





