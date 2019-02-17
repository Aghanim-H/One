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























