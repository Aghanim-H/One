# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用，理论上都应该先导入，string是特例
- calendar，time，datetime的区别参考中文意思

## calendar
- 跟日历相关的模块
- isleap:判断某一年是否闰年
- leapdays:获取指定年份之间的闰年的个数
- month():获取某个月的日历字符串
    - 格式：calendar.month(年，月)
    - 返回值：月日历的字符串
- monthrange():获取一个月的周几开始计和天数
    - 格式：calendar.monthrange(年，月)
    - 返回值：元组（周几开始，总天数）
    - 注意：周默认0-6表示周一到周天
- monthcalendar():返回一个月每天的矩阵列表
    - 格式：calendar.monthcalendar(年，月)
    - 返回值：二级列表
    - 注意：矩阵中没有天数用0表示
- prcal：print calendar缩写，直接打印某年的日历
- prmonth()直接打印整个月的日历
    - 格式：calendar.prmonth(年，月)
    - 返回值：无
- weekday（）获取周几
    - 格式：calendar.weekday(年，月，日)
    - 返回值：周几对应的数字
- 见 操作练习 代码片段1

## time模块
### 时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能够支持到2038年
### UTC时间
    - UTC又称为世界协调时间，以英国的格林尼治天文所在地区的时间作为参考时间，也叫做世界标准时间。
    - 中国时间是UTC+8 东八区
### 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起节省蜡烛！每天变成25个小时，本质没变还是24小时。
### 时间元组
    - 一个包含时间内容的普通元组
    ```
    索引     内容     属性         值

    0       年       tm_year     2015
    1       月       tm_mon      1～12
    2       日       tm_mday     1～31
    3       时       tm_hour     0～23
    4       分       tm_min      0～59
    5       秒       tm_sec      0～61  60表示闰秒  61保留值
    6       周几     tm_wday     0～6
    7       第几天    tm_yday     1～366
    8       夏令时    tm_isdst    0，1，-1（表示夏令时）
    ```
- 见 操作练习 代码片段2
    
## strftime：将时间元组转化为自定义的字符串格式    
```
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
```
- 把时间表示成，2018 3.26 21：05
- 见 操作练习 代码片段3
    
## datetime模块
- datetime提供日期和时间的运算和表示
- 见 操作练习 代码片段4

## datetime.datetime 模块
- 提供比较好用的时间而已
- 类定义
    ```
    class datetime.datetime(year, month, day[, hour
          [, minute
          [, second
          [, microsecond
          [, tzinfo]]]]])
    # The year, month and day arguments are required.
    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= n
    0 <= hour < 24
    0 <= minute < 60
    0 <= second < 60
    0 <= microsecond < 10**
    ```
- 类方法
    ```
    datetime.datetime 模块
    提供比较好用的时间而已
    类定义
    
     class datetime.datetime(year, month, day[, hour
              [, minute
              [, second
              [, microsecond
              [, tzinfo]]]]])
    # The year, month and day arguments are required.
    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= n
    0 <= hour < 24
    0 <= minute < 60
    0 <= second < 60
    0 <= microsecond < 10**
    类方法
    `
    datetime.today(): 返回当前本地datetime.随着 tzinfo None. datetime.fromtimestamp(time.time()). datetime.now([tz]): 返回当前本地日期和时间, 如果可选参数tz为None或没有详细说明,这个方法会像today(). datetime.utcnow(): 返回当前的UTC日期和时间, 如果tzinfo None ,那么与now()类似. datetime.fromtimestamp(timestamp[, tz]): 根据时间戳返回本地的日期和时间.tz指定时区. datetime.utcfromtimestamp(timestamp): 根据时间戳返回 UTC datetime. datetime.fromordinal(ordinal): 根据Gregorian ordinal 返回datetime. datetime.combine(date, time): 根据date和time返回一个新的datetime. datetime.strptime(date_string, format): 根据date_string和format返回一个datetime.
    
    实例方法
    
    datetime.date(): 返回相同年月日的date对象. datetime.time(): 返回相同时分秒微秒的time对象. datetime.replace(kw): kw in [year, month, day, hour, minute, second, microsecond, tzinfo], 与date类似. 类属性
    
    datetime.min: datetime(MINYEAR, 1, 1). datetime.max: datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999).
    
    实例属性(read-only)
    
    datetime.year: 1 至 9999 datetime.month: 1 至 12 datetime.day: 1 至 n datetime.hour: In range(24). 0 至 23 datetime.minute: In range(60). datetime.second: In range(60). datetime.microsecond: In range(1000000). `
    ```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    