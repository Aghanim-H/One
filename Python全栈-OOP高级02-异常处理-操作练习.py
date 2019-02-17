# 代码片段1
# l = [1,2,3,4,5]
# print(l[10])
# print(l.liudana)
# 常常犯的除零错误
# num = int(input("Please input your mun:"))
# print(100/num)

# 代码片段2
# 简单异常案例
try:
    num = int(input("Plz imput your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
except:
    print("你特娘的输入的啥玩意儿")
    # exit是退出程序的意思
    exit()

# 简单异常案例2
# 给出提示信息
try:
    num = int(input("Plz imput your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
# 捕获异常后，把异常实例化，出错信息就会在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
# 如果是多种error的情况
# 需要把越具体的错误，越往前放
# 在异常类继承关系中，越是子类的异常，越要往前放，越是父类的异常，越要往后放
# 在处理异常的时候，一旦拦截到某一个异常，则不再继续往下查看，直接进行下一个
# 代码，即有finally则执行finally语句块，否则就执行下一个大的语句
except ZeroDivisionError as e:
    print("你特娘的输入的啥玩意儿")
    print(e)
    # exit是退出程序的意思
    exit()
except NameError as e:
    print("名字错了")
    print(e)
except AttributeError as e:
    print("好像属性有问题")
    print(e)
    exit()
# 所有异常都是继承自Exception，如果写上下面这句话，任何异常都会拦截住
# 而且，下面这句话一定是最后一个exception
except Exception as e:
    print("我也不知道就出错了")
    print(e)
# exception下面不应该在跟其他的异常处理了
except ValueError as e:
    print("No>>>>>>>>>>>>")
print("hahahhaha!!!!")
# 作业：为什么我们可以直接打印出实例e，此时实例e应该实现了哪个函数

# 代码片段3
# raise案例
try:
    print("我爱王晓静")
    print(3.1415926)
    # 手动引发一个异常，注意语法：raise ErrorClassName
    raise ValueError
    print("还没完呀")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行的")

# raise案例2
# 自定义异常，需要注意，自定义异常必须是系统异常类的子类
class DanaError(ValueError):
    pass
try:
    print("我爱王晓静")
    print(3.1415926)
    # 手动引发一个异常，注意语法：raise ErrorClassName
    raise DanaError
    print("还没完呀")
except NameError as e:
    print("NameError")
except DanaError as e:
    print("DanaError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行的")

# else语句案例
try:
    num = int(input("Plz input your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("反正我都会被执行")

























































