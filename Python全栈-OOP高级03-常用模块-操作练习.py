# 代码片段1
# 使用前需要先导入
import calendar
# calendar：获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2019)
print(type(cal))

cal  = calendar.calendar(2019,l = 0,c = 5)
print(cal)

# isleap判断某一年是否闰年
calendar.isleap(2000)

# leapdays获取指定年份间的闰年个数
calendar.leapdays(2001,2018)

help(calendar.leapdays)

# month()获取某一个月日历的字符串
m3 = calendar.month(2019,2)
print(m3)

# monthrange()获取一个月周几开始记，以及这个月的总天数
help(calendar.monthrange)
w,t = calendar.monthrange(2019,3)
print(w)
print(t)

# monthcalendar()获取一个月每天的矩阵列表
m = calendar.monthcalendar(2019,3)
print(type(m))
print(m)

# prcal:print calendar直接打印某年日历
calendar.prcal(2019)
help(calendar.prcal)

# prmonth（）直接打印整个月的日历
calendar.prmonth(2019,3)

# weekday()获取周几
calendar.weekday(2019,3,27)

# 代码片段2
# 需要单独导入
import time
# 时间模块的属性
# timezone：当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔，东八区的是-28800
# altzone：获取当前时区与UTC时间相差的秒数，在有夏令时的情况下
# daylight：检测当前是否是夏令时时间状态，0 表示 是
print(time.timezone)
print(time.altzone)
print(time.daylight)
# 得到时间戳
time.time()
# localtime：得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素的内容
t = time.localtime()
print(type(t))
print(t)
print(t.tm_hour)

# asctime（）返回元组的正常字符串化之后的时间格式
# 格式：time.asctime(时间元组)
# 返回值：字符串 Tue Jun 6 11：11：00 2017
t = time.localtime()
tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime：获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)

# mktime()使用时间元组获取对应的时间戳
# 格式：time.mktime(时间元组)
# 返回值：浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(type(t))
print(ts)

# clock：获取CPU时间，3.0-3.3版本直接使用，3.6版本调用有问题

# sleep：使程序进入睡眠，n秒之后继续
for i in range(10):
    print(i)
    time.sleep(1)

# 代码片段3
# strftime：将时间元组转化为自定义的字符串格式
# 把时间表示成，2018年3月26日 21：05
t = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%M",t)
print(ft)

# 代码片段4
import datetime
# datetime常见属性
# datetime.date：一个理想化的日期，提供year，month，day属性
dt = datetime.date(2018,3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.time：提供一个理想化的时间，提供hour，minute，sec，microsec等内容

# datetime.datetime：提供日期跟时间的组合
from datetime import datetime
# 常用类方法：
# today：
# now：
# utcnow：
# fromtimestamp：从时间戳中返回本地时间
dt = datetime(2018,2,15)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta：提供一个时间差，时间长度
# 表示一个时间间隔
from datetime import datetime,timedelta
t1 = datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours = 1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

# timeit：时间测量工具
# 测量程序运行时间间隔试验
def p():
    time.sleep(3.6)
t1 = time.time()
p()
print(time.time() - t1)

# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
import timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
# 利用timeit调用代码，执行十万次，查看运行时间
t1 = timeit.timeit(stmt = "[i for i in range(1000)]",number = 100000)
# 测量代码c执行十万次运行结果
t2 = timeit.timeit(stmt = c,number = 100000)
print(t1)
print(t2)

help(timeit.timeit)

# timeit可以执行一个函数，来测量一个函数的执行时间
def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))
# 执行函数，重复10次
t = timeit.timeit(stmt = doIt,number = 10)
print(t)

s = '''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
'''
# 执行doIt（num）
# setup负责把环境变量准备好
# 实际相当于给timeit创造了一个小环境
# 在创造小环境中，代码执行的顺序大致是
'''
def doIt(num):
    …………
num = 3
doIt(num)
'''
t = timeit.timeit("doIt(num)",setup = s+"num = 3",number = 10)
print(t)

# 代码片段5
from datetime import datetime as dt
print(dt.now())




