# 定义一个汽车类
class Car:
    def __init__(self,newname):
        self.name = newname
        self.price = '50000000'
    def move(self):
        print(self.name,'移动')
    def toot(self):
        print(self.name,'叫')
    def ao(self):
        print(self.name,'滴滴滴...')

# 创建对象
red_car = Car('BWM')
red_car.move()
red_car.color = 'red'
print('内存地址1：',id(red_car),red_car.color)

blue_car = Car('AUDI')
blue_car.toot()
blue_car.color = 'blue'
print('内存地址2：',id(blue_car),blue_car.color)

yellow_car = Car('野马')
yellow_car.ao()
yellow_car.color = 'yellow'
print('内存地址3：',id(yellow_car),yellow_car.color)



