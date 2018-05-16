
import pygame
from Plane_sprites import * 


class PlaneGame(object):
    '''飞机大战主游戏类'''

    def __init__(self):    # init方法是初始化这个类
        '''初始化游戏'''
        # 1、游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)    # screen只是相当于一个变量，可以自己命名.后面的大写是调用到了精灵组里面的东西
        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()    # clock也是变量名，后面的是pygame里面的，time是模块，Clock是模块里的类
        # 3、背景 英雄 敌机 这些精灵
        self.__create_sprites()
        

    def start_game(self):
        '''开始游戏'''
        print('开始游戏')

        while True:
            # 1、设置帧率
            self.clock.tick(60)
            # 2、事件监听
            self.__event_hander()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新精灵组和精灵
            self.__update_sprites()
            # 5、屏幕显示
            pygame.display.update()
    def __event_handler(self):
        '''事件监听'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
    
    @staticmethod            
    def __game_over():
        pygame.quit()
        exit()


    def __check_collide(self):
        '''碰撞检测'''
        pass

    def __update_sprites(self):
        '''更新精灵和精灵组'''
        pass

    def __create_sprites(self):
        '''创建精灵用'''
        pass

if __init__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()   # 实例化

    # 开始游戏
    game.start_game()   # 调用开始游戏
