# 餐馆
class Restaurant():

    def __init__(self):
        self.name = "老王八餐馆"

        self.cuisine_type = "--中餐--"

    def describe_restaurant(self):
        print(self.name,self.cuisine_type)

    def open_restaurant(self):
        print('*'*30)
        print('本餐馆正在营业')

res = Restaurant()
res.describe_restaurant()
res.open_restaurant()

print('*'*30)
re = Restaurant()
re.describe_restaurant()

print('*'*30)
r = Restaurant()
r.describe_restaurant()







