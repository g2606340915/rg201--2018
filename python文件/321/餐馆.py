class Restaurant:
    def __init__(self,newname):

        # 餐馆名字
        self.restaurant_name = newname
        # 菜系
        self.cuisine_type = '蔬菜','肉食','水果'
    def shu_cai(self):
        print(self.restaurant_name,'清淡','多含维生素')
    def rou_shi(self):
        print(self.restaurant_name,'油腻','含有较多的能量')
    def shui_guo(self):
        print(self.restaurant_name,'甜','开胃')

#can_guan=reataurant_name()
can_guan = Restaurant('蔬菜')
can_guan.shu_cai()

print('*'*30)

can_guan = Restaurant('肉食')
can_guan.rou_shi()

print('*'*30)

can_guan = Restaurant('水果')
can_guan.shui_guo()

print('*'*30)



    
