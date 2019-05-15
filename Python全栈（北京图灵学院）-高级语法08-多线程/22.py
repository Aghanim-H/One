import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        # 处理锁
        item = input_q.get()
        print("pull",item,"out of q")  # 此处替换为有用的工作
        input_q.task_done()  # 发出信号通知任务完成
    print("Out of consumer:",ctime())  # 此句未执行，因为

def producer(sequence,output_q):
    print("Into producer:",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("Out of procuder:",ctime())

# 建立进程
if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer,args = (q,))
    cons_p.daemon = True
    cons_p.start()

    # 生产多个锁，sequence代表要发给消费者的锁序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
    # 等待所有锁被处理
    q.join()