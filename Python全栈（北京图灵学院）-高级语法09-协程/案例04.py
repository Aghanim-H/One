# 直接使用生成器

L = [x*x for x in range(5)]  # 放在中括号中是列表生成器
G = (x*x for x in range(5))  # 放在小括号中就是生成器

print(type(L))
print(type(G))
