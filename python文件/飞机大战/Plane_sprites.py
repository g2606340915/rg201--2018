import random
import pygame

# 屏幕尺寸
SCREEN_RECT = pygame.Rect(0,0,480,700)


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵'''
    def __init__(self,image_name,speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self,*args):
        self.rect.top += self.speed

    @staticmethod
    def image_names(prefix,count):
        names = []
        for i in range(1,count + 1):
            names.append('/home/guobin/图片'+ prefix + str(i) + '.png')

        return names


class Background(GameSprite):
    '''背景精灵'''
    def __init__(self,is_alt = False):
        super().__init__('/home/guobin/图片/background.png')
        if is_alt:
            self.rect.bottom = 0

    def update(self,*args):
        super().update(args)

        if self.rect.top >= SCREEN_RECT.height:
            self.rect.bottom = 0


class PlaneSprite(GameSprite):
    '''飞机精灵，包括敌人和英雄'''
    def __init__(self,image_names,destroy_names,life,speed):
        image_name = image_name[0]
        super().__init__(image_name,speed)

        # 生命值
        self.life = life

        # 正常图像列表
        self.__life_images = []
        for file_name in image_names:
            image = pygame.image.load(file_name)
            self.__life_images.append(image)

        # 被摧毁图像列表
        self.__destroy_images = []
        for file_name in destroy_names:
            image = pygame.image.load(file_name)
            self.__destroy_images.append(image)

        # 默认播放生存图片
        self.images = self.__life-images
        # 显示图像索引
        self.show_image_index = 0
        # 是否循环播放
        self.is_loop_show = True
        # 是否可以被解除
        self.can_destroied = False

    def update(self,*args):
        self.update_images()

        super().update(args)

    def update_images(self):
        '''更新图像'''
        pre_index = int(self.show_image_index)
        self.show_image_index += 0.05
        count = len(self.images)

    # 判断是否循环播放
        if self.is_loop_show:
            
















































