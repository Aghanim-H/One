# 函数案例

def odd():
    print("Step 1")
    print("Step 2")
    print("Step 3")
    return None

odd()

# 生成器的案例
# 在函数odd中，yield负责返回
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3

# odd()是调用生成器
g = odd()
one = next(g)
print(one)

two = next(g)
print(two)

three = next(g)
print(three)

# for循环调用生成器，斐波那契数列

def fib(max):
    n,a,b = 0,0,1  # 注意写法
    while n < max:
        print(b)
        a,b = b,a+b  # 注意写法
        n += 1
    return "Done"

fib(5)

# 生成器写法，斐波那契数列

def fib(max):
    n,a,b = 0,0,1  # 注意写法
    while n < max:
        yield b
        a,b = b,a+b  # 注意写法
        n += 1
    # 需要注意，爆出异常返回的值是return的返回值
    return "Done"

G = fib(5)

for i in range(6):
    rst = next(G)
    print(rst)

ge = fib(10)
'''
生成器的典型用法是在for中使用
比较常见的典型生成器就是range
'''
# 在for循环中使用生成器
for i in ge:
    print(i)