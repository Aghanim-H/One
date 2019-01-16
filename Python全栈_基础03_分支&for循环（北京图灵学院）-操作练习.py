# 程序的三大结构
# 	·顺序
# 	·分支
# 	·循环
# 	分支
# 		·分支的基本语法
# 			if 条件表达式:
# 				语句1
# 				语句2
# 				语句3
# 				…………
# 		·条件表达式就是计算结果必须为布尔值的表达式
#		·表达式后面的冒号不能少
#		·注意if后面出现的语句，如果属于if语句块，则必须同一个缩进等级
# 		·条件表达式结果为True则执行if后面的缩进的语句块
# 		·见 代码片段1
# 			·双向分支
# 				if……else……语句
# 					if 条件表达式:
# 						语句1
# 						语句2
# 						……
# 					else:
# 						语句1
# 						语句2
# 						……
# 				·双向分支有两个分支，当程序执行到if……else……语句的时候，一定会执行if或者else中的一个，也仅执行一个
# 				·缩进问题：if和else一个层级，其余语句一个层级
# 			·见 代码片段2
# 		多路分支
# 			·很多分支的情况，简称多路分支
# 			·elif可以有很多个
# 			·else可选
# 			·多路分支只会选一个执行
# 				语法：
# 				if 条件表达式:
# 					语句1
# 					……
# 				elif 添加表达式:
# 					语句1
# 					……
# 				elif 条件表达式:
# 				……
# 				else:
# 					语句1
# 					……
# 			·见 代码片段3
# 		if语句其他：
# 			·if语句可以嵌套使用，单不推荐
# 			·python里面没有switch-case语句
# 	循环语句
# 		·重复执行某些固定动作或者处理某些基本固定的事物
# 		·分类
# 			·for循环
# 			·while循环
# 			for循环：
# 				·for循环中的变量表示，一般用i，k，m，n，或者index，idx，item之类
# 				·在python中，如果循环变量名称不重要，可以用下划线"_"代替
# 				·语法
# 					for 变量 in 序列：
# 						语句1
# 						语句2
# 						……
# 			·见 代码片段4
# 			range介绍
# 				·生成一个数字序列
# 				·具体范围可以设定
# 				·注意，一般在python中，如果有表示数字范围的两个数，一般是包含左边数字不包含右边数字
# 				·randint是特例，它左右都包含
# 				·range函数在python2中和python3中有严重的区别
# 				·见 代码片段5
# 			for-else语句：
# 				·当for循环结束的时候，会执行else语句
# 				·else语句是可选语句
# 				·见 代码片段6
# 			循环之break，continue，pass
# 				·break：无条件结束整个循环，简称循环猝死
# 				·continue：无条件结束本次循环，从新进入下一轮循环
# 				·pass：表示略过，通常用于占位，没有跳过功能
# 				·见 代码片段7


# 代码片段1
age = 17  #if语句练习，如果age小于18岁，则打印信息“去叫家长”
if age < 18:
	print("去叫家长吧，孩子")
	print("我们不带你玩")
	print("滚球吧")

age = 19  
if age < 18:
	print("去叫家长吧，孩子")
	print("我们不带你玩")
	print("滚球吧")
print("开始上车咯，老司机们")

# 代码片段2
print("今天学习for循环")
gender = "男"
if gender == "女":
	print("来，叔叔给你糖吃")	
print("开始讲for循环了")

gender = input("请输入性别：")  #input的作用是：1、在屏幕上输出括号内的字符串。2、接受用户输入的内容并返回到程序。3、input返回的内容一定是字符串类型。
print("你输入的性别是： {0}".format(gender))
if gender == "nan":
	print("来，我们纪念一下今天吧，代码敲十遍")
else:
	print("发糖了发糖了")
	print("你是女生，特殊照顾咯")
print("开始上课了")

# 必须得吧SublimeREPL给我搞定了  再继续
# 他妈隔壁  找了无数文章  还是没找到解决办法  泪崩中
# 20190113，只有更换Pycharm使用了，没有办法，Sublime网站部分网页上不去
# 20190115，pycharm基本用法及Markdown基本用法学会了，继续正常学习写代码……
print("hello world")
# 考试成绩判断，90以上，输出A；80-90，B；70-80，C；60-70，D；60以下，输出：起开，我没你这撇学生。
score = input("请输入学生成绩：")  # 注意input函数返回值得类型(是字符串)
score = int(score)  # 需要把str转换成int
if score > 90:
	print("A")
if score >= 80:
	print("B")
if score >= 70:
	print("C")
if score >= 60:
	print("D")
if score < 60:
	print("起开，我没你这撇学生")

score = input("请输入学生成绩：")
score = int(score)
if score >= 90:
	print("A")
if score >= 80 and score < 90:
	print("B")
if score >= 70 and score < 80:
	print("C")
if score >= 60 and score < 70:
	print("D")
if score < 60:
	print("起开，我没你这撇学生")

# 代码片段3
score = input("请输入学生成绩：")
score = int(score)
if score >= 90:
	print("A")
elif score >= 80:
	print("B")
elif score >= 70:
	print("C")
elif score >= 60:
	print("D")
else:
	print("起开，我没你这撇学生")

# 代码片段4
for name in ["zhangsan","lisi","wangwu","zhaoliu"]:
	print(name)
for name in ["zhangsan","lisi","wangwu","jingjing"]:
	print(name)
	if name == "jingjing":
		print("我的最爱 {0}出现了".format(name))
	else:
		print("同学我们不约，不约，同学请自重")

# 代码片段5
for i in range(1,10):
	print(i)

# 代码片段6
# for-else语句，打印列表中的同学，如果没有在列表中或者列表结束了，我们需要打印提示语句，表示不再爱了
for name in ["zhangsan","lisi","wangwu","jingjing"]:
	print(name)
	if name == "jingjing":
		print("我的最爱 {0}出现了".format(name))
	else:
		print("同学我们不约，不约，同学请自重")
else:
	print("别的都不是我的学生，不会再爱了")

# 代码片段7
# 在数字1-10中，寻找数字7，一旦找到，打印出来，其余什么都不做
for i in range(1,11):
	if i == 7:
		print("我找到7了")
		break
	else:
		print(i)
# 1-10中找到所有偶数后打印
for i in range(1,11):
	if i%2 == 1:
		continue
	else:
		print(" {0} 是偶数".format(i))
# 版本2
for i in range(1,11):
	if i%2 == 0:
		print(" {0} 是偶数".format(i))
# 版本3
for i in range(1,11):
	if i%2 == 1:
		continue
	print(" {0} 是偶数".format(i))

# pass例子
for i in range(1,11):
	pass
	print("wo zai zhe li")



