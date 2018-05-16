import pygame

# 定义一个常量
SCREEN_RECT = pygame.Rect(0,0,480,700)

class GameSprite(pygame.sprite.Sprite):
    '''精灵基类'''
    def __init__(self,image_name,speed=1):
        # 1、调用父类方法
        super().__init__()
        
        # 加载图片
        self.image = pygame.image.load(image_name)
  
        # 设置尺寸
        self.rect = self.image.get_rect()

        # 记录速度
        self.speed = speed

    def update(self,):

        # 默认情况下在垂直方向上移动
        self.rect.y += self.speed



class Backgroup(GameSprite):
    '''游戏背景精灵'''

    def update(self):
        
        # 先调用父类的方法
        super().update()

        # 判断是否移出屏幕，如果移动出屏幕，将图片设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -screen_rect.height

        
        



