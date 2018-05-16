'''
	烤鸡
cook_degree: 烤的时间
cook_degree_chicken: 生熟程度
Fride: 烤
saucelist: 酱料列表

'''


class kao_ji():
	def __init__(self):
		self.cook_degree = 0
		self.cook_degree_chicken = '生得'
		self.saucelist = []
	
	def Fride(self,times):
		self.cook_degree += times
		if self.cook_degree > 8:
			self.cook_degree_chicken = '烤糊了'

		elif self.cook_degree > 5:
			self.cook_degree_chicken = '烤熟了'
			self.saucelist.append('苹果酱料')

		elif self.cook_degree > 3:
			self.cook_degree_chicken = '半生不熟'

		else:
			self.saucelist.append('橄榄油')
			self.cook_degree_chicken = '生鸡'


kj = kao_ji()
kj.Fride(3)
print(kj.cook_degree_chicken)
kj.Fride(3)   # 这里是在前面的3分钟基础上又加上了3分钟
print(kj.cook_degree_chicken)
print(kj.saucelist)
