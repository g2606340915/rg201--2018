class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print('%s\n%s'%(self.name,self.type))
        # print('%s'%self.type)
        
    def open_restaurant(self):
        zhong = '正在营业'
        print(zhong.center(25))

print('*'*30)

can_guan = Restaurant('呀麦碟餐馆--吃到你喊呀麦碟\n','本店菜品有：蔬菜类，水果类，肉食类')
can_guan.open_restaurant()

print('*'*30)
can_guan.describe_restaurant()


