# Log
- [Python之日志处理（logging模块）](https://www.cnblogs.com/yyds/p/6901864.html)
- logging
    - logging模块提供模块级别的函数记录日志
    - 包括四大组件
## 1、日志相关概念
- 日志
    - 日志的级别（level）
        - 不同的用户关注不同的程序信息
        - debug
        - info
        - warning
        - error
        - critical
        - alert
        - emergency
- IO操作（不要频繁操作）
- log的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2、logging模块
- 日志级别
    - 级别可以自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方式
    - 直接使用logging（封装了其他组件）
    - logging四大组件直接定制
## 2.1 logging模块级别的日志
- 使用以下几个函数
    - logging.debug(msg, *args, **kwargs) 	    创建一条严重级别为DEBUG的日志记录
    - logging.info(msg, *args, **kwargs) 	    创建一条严重级别为INFO的日志记录
    - logging.warning(msg, *args, **kwargs) 	创建一条严重级别为WARNING的日志记录
    - logging.error(msg, *args, **kwargs) 	    创建一条严重级别为ERROR的日志记录
    - logging.critical(msg, *args, **kwargs) 	创建一条严重级别为CRITICAL的日志记录
    - logging.log(level, *args, **kwargs) 	    创建一条严重级别为level的日志记录
    - logging.basicConfig(**kwargs) 	        对root logger进行一次性配置
        - 只在第一次调用的时候起作用
        - 不配置logger则使用默认值
            - 输出：sys.stderr
            - 级别：WARNING
            - 格式：level：log_name:content
- 见 01 代码片段1



























