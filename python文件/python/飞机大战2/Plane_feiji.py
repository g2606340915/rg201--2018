# 使用pygame 我们要先导入这个包
import pygame
from Plane_sprites import *


class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):  # init是类的初始化，放属性的地方
        print('游戏初始化中')
        
        # 1、创建游戏窗口 pygame.display.set_mode 创建游戏窗口，需要传宽和高，返回给我们一个窗口
        # .size 取宽和高 .x取x轴的值 .y取y轴的值
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2、创建游戏时钟 pygame.time.Clock 会给我们返回一个时钟对象    用来更新的
        self.clock = pygame.time.Clock()
        # 3、调用私有方法，里面的创建精灵和精灵组
        self.enemy_group = pygame.sprite.Group()
        self.enemy = Enemy()
        self.enemy_group.add(self.enemy)

        self.__create_sprites()

        self.enemy.kill()

        # 4、设置定时器事件，每秒创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)     # 这里是1000毫秒 也就是1秒 
        '''
        # 5、每隔0.5秒发射一个豆豆
        pygame.time.set_timer(HERO_FIRE_EVENT,500)        # 这里是500毫秒 也就是0.5秒
        '''
    
    def start_game(self):
        print('开始游戏')
        
        while True:
            # 1、设置帧率
            self.clock.tick(60)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新精灵组
            self.__update_sprites()
            # 5、更新屏幕显示
            pygame.display.update()

    def __create_sprites(self): # 前面两个下划线，表示调用私有方法
        '''创建精灵和精灵组'''
        # pygame.sprite.Group() 可以创建一个精灵组
        # 1、背景精灵组
        bg1 = Backgroup('/home/guobin/图片/background.png')
        bg2 = Backgroup('/home/guobin/图片/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 2、敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 3、英雄精灵组
        self.hero = Hero()   # 这是实例化一个对象，然后扔到精灵组里
        self.hero_two = Hero_two()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero_two)
        
        # if self.enemy.speed == 2:   # 0.0.0.0.0
            # self.enemy.fire()    # .0.0.0.0.0
            

    def __event_handler(self):
        '''事件监听的方法'''
        # pygame.event.get() 获取监听事件的列表
        # 获取完列表以后，我写了一个for循环，循环这个列表

        # 这里监听一下按键
        key_pressed = pygame.key.get_pressed()   # ...
        for event in pygame.event.get():
            # print(event)
            # 当列表里面有pygame.QUIT这个值的时候，说明用户点了关闭按钮
            if event.type == pygame.QUIT:
                # 调用静态私有方法
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy = Enemy()   # ...
                self.enemy_group.add(self.enemy)   # ...
                self.enemy.fire()   # 这里是调用了敌机子弹
            # if self.enemy.speed == 2:
                # self.enemy.fire()
            '''
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            '''
            # elif event.tyge == pygame.KEYDOWN and event.key == pygame.K_RIGHT:   # pygame.KEYDOWN 是检测哪一个键被按下
                # print('动了')
            
            # 另外一个方案。返回所有按键的元组，如果某个按键按下，对应的值
            # key_pressed = pygame.key.get_pressed()

            if key_pressed[257]:   # 英雄1按下1键发子弹
                self.hero.fire()
            elif key_pressed[106]:   # 英雄2按下j键发子弹
                self.hero_two.fire_two()

            elif key_pressed[pygame.K_RIGHT]:
                # print('向右移动')
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                # print('向左移动')
                self.hero.speed = -2

            elif key_pressed[100]:
                # print('英雄2向右移动'):
                self.hero_two.speed = 2
            elif key_pressed[97]:
                # print('英雄2向左移动')
                self.hero_two.speed = -2
            else:
                self.hero.speed = 0
                self.hero_two.speed = 0

    def __check_collide(self):
        '''碰撞检测的方法'''
        # 1、子弹摧毁飞机 pygame里面有sprites这个模块，sprites模块里有groupcollide的方法，因为groupcollide首字母没有大写，所以不是类
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        pygame.sprite.groupcollide(self.hero_two.bullets,self.enemy_group,True,True)
        
        # 2、英雄撞到飞机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True) 
        enemies2 = pygame.sprite.spritecollide(self.hero_two,self.enemy_group,True) 
        enemies3 = pygame.sprite.spritecollide(self.hero,self.enemy.bullets,True) 

        enemies4 = pygame.sprite.spritecollide(self.hero_two,self.enemy.bullets,True) 
 

       # 3、判断列表是否有内容
        if len(enemies) > 0:
            
            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()
        if len(enemies2) > 0:
            
            # 让英雄牺牲
            self.hero_two.kill()

            # 结束游戏
            PlaneGame.__game_over()
        
        if len(enemies3) > 0:
            
            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()
        if len(enemies4) > 0:
            
            # 让英雄牺牲
            self.hero_two.kill()

            # 结束游戏
            PlaneGame.__game_over()
    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero_two.bullets,self.enemy.bullets]:
            # 更新精灵组里面所有精灵的位置
            group.update()
            # 绘制到屏幕上
            group.draw(self.screen)
        
    
    @staticmethod
    def __game_over():
        '''游戏结束'''
        print('游戏结束')
        pygame.quit()
        exit()
        pass




# 一般情况下，比如有一个场景：测试
if __name__ == '__main__':
    # 1、创建游戏对象
    game = PlaneGame()

    # 2、调用开始游戏的方法
    game.start_game()














