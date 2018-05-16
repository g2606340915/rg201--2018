# 定义一个父类
class A:
    def printA(self):
        print('---A---')

# 定义一个父类
class B:
    def printB(self):
        print('---B---')

# 定义一个子类，继承A，B
class C(A,B):
    def printC(self):
        print('---C---')
    

obj_C = C()
obj_C.printA()
obj_C.printB()
