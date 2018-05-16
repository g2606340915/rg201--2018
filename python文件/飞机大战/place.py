import pygame

class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵的基类'''

    def __init__(self,image_name,speed = 1):
        # 先调用父类的初始化方法
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸 
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self,*args):
        # 设置在垂直方向的移动
        

