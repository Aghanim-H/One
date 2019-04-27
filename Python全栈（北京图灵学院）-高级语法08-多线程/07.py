import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun,args=())
# 设置守护线程的方法：必须在start之前设置，否则无效
t1.setDaemon(True)  # 这样写也行：t1.daemon = True
t1.start()

time.sleep(1)
print("Main thread end")

# 为什么老师视频只打印三句话 我这段代码还是打印四句话，难道跟老师说的什么大环境有关系？