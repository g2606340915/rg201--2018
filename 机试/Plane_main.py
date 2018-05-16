import pygame
from Plane_sprite import *


class PlaneGame(object):
    '''主游戏类'''
    def __init__(self): 
        print('游戏初始化')

        # 1、创建游戏窗口   并固定尺寸
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3、调用私有方法，里面的创建精灵和精灵组
        self.enemy_group = pygame.sprite.Group()
        self.enemy = Enemy()
        self.enemy_group.add(self.enemy)

        self.__create_sprites()
    
        self.enemy.kill()

        # 4、设置定时器事件，每秒创建一个飞机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

        # pygame.time.set_timer(HERO_FIRE_EVENT,500)

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

    def __create_sprites(self):
        '''创建精灵和精灵组'''
        bg1 = Backgroup('/home/guobin/图片/u=3010804840,2593571328&fm=27&gp=0.jpg')
        bg2 = Backgroup('/home/guobin/图片/u=3010804840,2593571328&fm=27&gp=0.jpg')
        bg2.rect.x = -bg2.rect.width
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        '''事件监听'''

        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy = Enemy()
                self.enemy_group.add(self.enemy)
                
            

            if key_pressed[257]:
                self.hero.fire()

            elif key_pressed[119]:
                # 向上移动
                self.hero.speed = -2
                
            elif key_pressed[115]:
                # 向下移动
                self.hero.speed = 2

            else:
                self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁飞机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        
        # 英雄撞到飞机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()
    
            
              











    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
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


if __name__ == '__main__':
    game = PlaneGame()

    game.start_game()
