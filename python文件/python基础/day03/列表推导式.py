# 普通的一个随机数
b = []
for x in range(0,11):
    print(x)
    b.append(x)    
print('b=',b)
print('*'*30)

# 列表推导式1
a = [x for x in range(0,11)]
print(a)

c = [x for x in range(2,20)]
print(c)

# 列表推导式2
w = [(x,y) for x in range(1,3) for y in range(2,4)]
print(w)

z = [(x,y,z) for x in range(1,3) for y in range(2,4) for z in range(5,9)]
print(z)

# 以下d和e其实是一种输出，只不过方法不一样
d = []
for x in range(1,11):
    # 奇数
    if x%2 != 0:
        d.append(x)
print('d=',d)

e = [x for x in range(1,11) if x%2 != 0]
print('e=',e)

# set用法
m = [1,2,3.4,5,6,6,7,7]
L = set(m)
print(L)
print('*'*30)

n = [22,22,22]
n = set(n)
print(n)

