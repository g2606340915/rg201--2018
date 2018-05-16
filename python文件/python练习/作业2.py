def addOne(a):
    print('修改前是：',a)
    a += 1
    print('修改后是：',a)
    return a 

a = 3
print('函数内部操作后的a：',addOne(a))
print('函数外部的变量a为：',a)
