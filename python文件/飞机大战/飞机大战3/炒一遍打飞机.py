# 使用pygame  我们要先导入这个包
import pygame
from Plane_sprites import * 


class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):   
        print('游戏初始化')
        
        # 1、创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN.RECT.size)
        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()














