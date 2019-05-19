'''
协程代码案例1
'''

def simple_coroutine():
    print('-> start')
    x = yield
    print('-> recived',x)

# 主线程
sc =simple_coroutine()
print(1111)
# 可以使用sc.send(None),效果一样
next(sc)  # 预激

print(2222)
sc.send('zhexiao')

