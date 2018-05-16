import random
import pygame
from Plane_main import * 

# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,512,250)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定一个子弹的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵的基类'''

    def __init__(self,image_name,speed=1):

        # 调用父类
        super().__init__()

        # 加载图像
        self.image = pygame.image.load(image_name)

        # 设置尺寸
        self.rect = self.image.get_rect()

        # 记录速度
        self.speed = speed

    def update(self):
        # 横向移动
        self.rect.x += self.speed


class Backgroup(GameSprite):
    '''背景精灵'''
    def update(self):
        # 调用父类
        super().update()

        # 判断是否移出屏幕，如果移出屏幕，将图片移到右方
        if self.rect.x >= SCREEN_RECT.width:
            self.rect.x = -SCREEN_RECT.width


class Enemy(GameSprite):
    '''敌机精灵'''
    def __init__(self):
        super().__init__('/home/guobin/图片/enemy1.png')

        self.speed = random.randint(1,3)
        
        self.rect.left = 0
        
        max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = random.randint(0,max_y)
    def update(self):
        super().update()
        
        if self.rect.x >= SCREEN_RECT.width:
            self.kill()
   

class Hero(GameSprite):
    def __init__(self):

        super().__init__('/home/guobin/图片/life.png',0)

        # 英雄的初始位置
        self.rect.centery = SCREEN_RECT.centery
        self.rect.right = SCREEN_RECT.right - 12

        # 创建一个子弹精灵
        self.bullets = pygame.sprite.Group()

    def update(self):

        self.rect.y += self.speed
        # 判断飞机与屏幕边界
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        # 1、创建子弹
        bullet = Bullet()
        # 2、设置子弹的位置
        bullet.rect.right = self.rect.x - 20
        bullet.rect.centery = self.rect.centery
        # 3、将子弹添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    '''子弹精灵'''
    
    def __init__(self):
        super().__init__('/home/guobin/图片/bullet2.png',-2)

    def __del__(self):
        pass

    def update(self):

        self.rect.x += self.speed
        
        # 判断子弹是否超出屏幕，如果是，让子弹从精灵组删除
        if self.rect.right < 0:
            self.kill()
