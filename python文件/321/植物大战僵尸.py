# 定义一个向日葵的类
class xrk:
    def __init__(self,newname):
        self.name = newname
        self.price = '50'
        self.xue = '200'
    def yang_guang(self):
        print(self.name,'放阳光')

# 创建对象
yellow_xrk = xrk('向日葵')
yellow_xrk.yang_guang()
yellow_xrk.color = '黄色'
print('内存地址1：',id(yellow_xrk))
print('%s的颜色是%s\t价格是%s\t血量有%s'%(yellow_xrk.name,yellow_xrk.color,yellow_xrk.price,yellow_xrk.xue))

print('')
print('*'*30)
print('')

# 定义一个豌豆的类
class wd:
    def __init__(self,newname):
        self.name = newname
        self.price = '100'
        self.action = '摇头'
        self.xue = '250'
    def behave(self):
        print(self.name,'发射炮弹+摇头')

# 创建对象
green_wd = wd('豌豆')
green_wd.behave()
green_wd.color = '绿色'
print('内存地址2：',id(green_wd))
print('%s的颜色是%s\t价格是%s\t血量有%s'%(green_wd.name,green_wd.color,green_wd.price,green_wd.xue))

print('')
print('*'*30)
print('')

# 定义一个坚果的类
class jg:
    def __init__(self,newname):
        self.name = newname
        self.price = '50'
        self.action = '阻挡'
        self.xue = '600'
    def behave(self):
        print(self.name,'阻挡僵尸前进')

# 创建对象
grown_jg = jg('坚果')
grown_jg.behave()
grown_jg.color = '棕色'
print('内存地址3：',id(grown_jg))
print('%s的颜色是%s\t价格是%s\t血量有%s'%(grown_jg.name,grown_jg.color,grown_jg.price,grown_jg.xue))

print('')
print('*'*30)
print('')

# 定义一个僵尸的类
class js:
    def __init__(self,newname):
        self.name = newname
        self.purpose = '\僵尸是你的敌人，你需要使用众多植物来消灭它们/'
        self.action1 = '有的僵尸会走、会跑、会跳。'
        self.action2 = '如果僵尸们到了你的植物面前，它会一口一口的吃掉植物'
        self.xue = '300'
    def behave(self):
        print(self.name,'一步一步的走进你的房子，并吃掉你的脑子')
# 创建对象
blank_js = js('僵尸')
blank_js.behave()
blank_js.color = '黑色'
print('内存地址4：',id(blank_js))
print('%s的颜色是%s,%s,血量有%s'%(blank_js.name,blank_js.color,blank_js.purpose,blank_js.xue))





