# 递归函数就是调用函数本身
# 求和函数
def sum1 (a,b):
    c = a+b
    d = a-b
    print(c,d)
    if c>0 and d>0:
        # sum1(c,d)
        print(c,d)
    else: 
        sum1(a,b)
        print(a,b)
sum1(10,5)


