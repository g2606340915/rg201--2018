'''定义一个类'''
# class (类名)
#     方法列表


class Dog:
    
    # 方法
    def walk(self):
        print('走')
    def drink(self):
        print('喝水')
    def tian(self):
        print('舔')

# 创建一个叫哈哈的对象
haha = Dog()
haha.name = '哈哈'
print('那只叫“%s”的狗狗'%haha.name)
haha.walk()
haha.drink()
haha.tian()







