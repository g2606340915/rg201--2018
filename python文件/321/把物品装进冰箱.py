class Play_zs:
    # 1、写一个构造函数 init
    def __init__(self,newName,animal):
        self.animal = animal
        self.name = newName
    
    # 2、张三需要去买大象 
    def buyAnimal(self):
        print('%s'%self.name,"准备了一只%s"%self.animal)

    # 3、打开冰箱
    def open_bingxiang(self):
        print('打开冰箱')
    
    # 装进冰箱
    def put_in(self):
        print('把%s装进冰箱里面'%self.animal)

    # 关闭冰箱
    def close_bingxiang(self):
        print('关闭冰箱')

game = Play_zs('张三','老虎')
game.buyAnimal()
game.open_bingxiang()
game.put_in()
game.close_bingxiang()

print('*'*30)

cao = Play_zs('李四','狮子')
cao.buyAnimal()
cao.open_bingxiang()
cao.put_in()
cao.close_bingxiang()

print('*'*30)

abc = Play_zs('王五','大象')
abc.buyAnimal()
abc.open_bingxiang()
abc.put_in()
abc.close_bingxiang()

