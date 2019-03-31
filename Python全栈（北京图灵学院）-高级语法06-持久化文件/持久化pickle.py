# 代码片段1
print("----代码片段1----")
# 序列化案例
import pickle
age = 19
with open(r"test02.txt",'wb') as f:
    pickle.dump(age,f)

# 反序列化案例
import pickle
with open(r"test02.txt",'rb') as f:
    age = pickle.load(f)
    print(age)

# 序列化案例2
import pickle
a = [19,'liudana','i love wangxiaojing',[185,76]]
with open(r"test03.txt",'wb') as f:
    pickle.dump(a,f)
with open(r"test03.txt",'rb') as f:
    a = pickle.load(f)
    print(a)