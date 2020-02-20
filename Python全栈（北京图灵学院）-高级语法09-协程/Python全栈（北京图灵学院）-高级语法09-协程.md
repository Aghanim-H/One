# 协程
- 参考资料
    - [Python 3.5 协程究竟是个啥](http://python.jobbole.com/86481/)
    - [Python黑魔法 --- 异步IO（ asyncio） 协程](http://python.jobbole.com/87310/)
    - [python协程2：yield from 从入门到精通](https://segmentfault.com/a/1190000009781688)
    
# 迭代器
- 可迭代（Iterable）：直接作用于for循环的变量
    - 见 案例01
- 迭代器（Iterator）：不但可以作用于for循环，还可以被next调用
    - list是典型的可迭代对象，但不是迭代器
    - 通过isinstance判断
        - 见 案例02
    - iterable和iterator可以转换
        - 通过iter函数
            - 见 案例03
            
# 生成器
- generator：一边循环一边计算下一个元素的机制/算法
    - 需要满足三个条件
        - 每次调用都生产出for循环需要的下一个元素或者
        - 如果达到最后一个后，爆出StopIteration异常
        - 可以被next函数调用
    - 如何生成一个生成器
        - 直接使用
            - 见 案例04
        - 如果函数中包含yield，则这个函数就叫生成器
        - next调用函数，遇到yield返回
            - 见 案例05
            
# 协程
- 历史历程
    - 3.4引入协程，用yield实现
    - 3.5引入协程语法
    - 实现的协程比较好的包有asyncio，tornado，gevent
- 定义：
    协程是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序。
    - 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
- 协程的实现：
    - yield返回
    - send调用
        - 见 案例06
- 协程的四个状态
    - inspect.getgeneratorstate(￿￿￿￿￿三个小圆点省略号怎么打？)函数确定，该函数会返回下述字符串中的一个
    - GEN_CREATED：等待开始执行
    - GEN_RUNNING：解释器正在执行
    - GEN_SUSPENED：在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next预激（prime）
    - 见 案例07
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给next函数或send方法的调用方（即触发协程的对象）
    - 止协程的一种方式：发送某个哨符值，让协程退出。内置的None 和 Ellipsis 等常量经常用作哨符值==。
- yield from
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止会发出StopIteration异常，异常对象的value属性保存返回值
    - yield from 从内部捕获StopIteration异常
    - 见 案例08
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yield from表达式出暂停，调用方可以直接把数据发给子生成器
        - 子生成器在把产出的值发给调用方
        - 子生成器在最后，解释器会抛出StopIteration，并且把返回值附加到异常对象上
        - 见 案例09
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    