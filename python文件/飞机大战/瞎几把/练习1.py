'''
number = 1
while number <= 5:
    print(number)
    number += 1
'''
'''
a = '\n告诉我一些命令，我将会返回给你'
a += '\n如果你不想继续，可以输入‘quit’来退出:'
print('*'*30)
b = ''
while b != 'quit':
    b = input(a)
    print(b)
'''

class Dog():
    
    def __init__(self,name,age):
        '''这里是属性name和age'''
        self.name = name
        self.age = age
    def sit(self):
        '''这里是方法'''
        print(self.name.title() + '正坐在雪地里')
    
    def roll(self):  # roll的意思是打滚
        print(self.name.title() + '小狗在打滚')






