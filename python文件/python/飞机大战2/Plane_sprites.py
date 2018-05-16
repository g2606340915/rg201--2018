import random
import pygame
from Plane_feiji import *

# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定一个子弹的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1




class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵的基类'''

    def __init__(self,image_name,speed=1):
        
        # 调用父类的方法
        super().__init__()

        # 加载图像的属性 pygame.image.load() 加载图像
        self.image = pygame.image.load(image_name)
        
        # 设置尺寸 slef.image.get_rect() 返回图片的宽和高
        self.rect = self.image.get_rect()
        
        # 记录速度
        self.speed = speed
    

    def update(self):

        # 默认在垂直方向上移动
        self.rect.y += self.speed
        
        
class Backgroup(GameSprite):
    '''背景精灵组'''     
    def update(self):
        # 1、调用父类的方法
        super().update()

        # 2、判断是否移动出屏幕，如果移出屏幕，将图片移到上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height
        
class Enemy(GameSprite):
    '''敌机精灵类'''       

    def __init__(self):
        
        # 1、调用父类的方法，创建敌机的精灵，并且指定敌机的图像
        super().__init__('/home/guobin/图片/enemy1.png')

        self.bullets = pygame.sprite.Group()     # .0.0.0.0.0.0.0
        # 2、设置敌机的随机初始速度
        self.speed = random.randint(1,3)
    
        # 3、设置敌机的随机初始位置        
        self.rect.bottom = 0
        
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        
        # 1、调用父类的方法，让敌机在垂直方向上移动
        super().update()

        # 2、判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    def fire(self):
        a_bullet = Abullet()
        a_bullet.rect.top = self.rect.y + 20
        a_bullet.rect.centerx = self.rect.centerx
        self.bullets.add(a_bullet)

    def __del__(self):
        pass
		  
        
class Hero(GameSprite):   # 这是父类
    '''英雄的精灵'''  
    
    def __init__(self):   

        super().__init__('/home/guobin/图片/life.png',0)  

        # 给英雄设置一个初始位置
        self.rect.centerx = SCREEN_RECT.centerx     # 这里设置飞机的中心等于屏幕x轴的中心
        self.rect.bottom = SCREEN_RECT.bottom - 120   # 飞机距离底部120个距离

        # 创建一个子弹精灵
        self.bullets = pygame.sprite.Group()
        
    def update(self):
        
        # super().update()
        # 飞机水平移动   
        self.rect.x += self.speed
        
        # 判断飞机屏幕边界
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right 

    def fire(self):
        # print('发射子弹')
        # for i in (1,2,3): 
            # 1、创建子弹
            bullet = Bullet()
            # 2、设置子弹的位置
            bullet.rect.bottom = self.rect.y - 20     # *i
            bullet.rect.centerx = self.rect.centerx
            # 3、将子弹添加到精灵组
            self.bullets.add(bullet)


# 创建英雄2类
class Hero_two(GameSprite):
    def __init__(self):
        super().__init__('/home/guobin/图片/bomb.png')
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 60

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire_two(self):
        bullet_two = Bullet_two()
        bullet_two.rect.bottom = self.rect.y - 20
        bullet_two.rect.centerx = self.rect.centerx
        self.bullets.add(bullet_two)



class Bullet(GameSprite):
    '''子弹精灵'''


    def __init__(self):

        # 1、调用父类的方法
        super().__init__('/home/guobin/图片/bullet2.png',-2)

    def __del__(self):   # 子弹删除了
        pass

    def update(self):
        
        # super().update()
        self.rect.y += self.speed
        
        # 判断子弹是否超出屏幕，如果是，我们要让子弹从精灵组删除
        if self.rect.bottom < 0:
            self.kill()

class Bullet_two(GameSprite):
    '''子弹精灵'''


    def __init__(self):

        # 1、调用父类的方法
        super().__init__('/home/guobin/图片/bullet2.png',-2)
    def __del__(self):
        pass

    def update(self):
        
        # super().update()
        self.rect.y += self.speed

        # 判断子弹是否超出屏幕，如果是，我们要让子弹从精灵组删除
        if self.rect.bottom < 0:
            self.kill()
    

class Abullet(GameSprite):
    '''敌机子弹精灵'''
    def __init__(self):
        super().__init__('/home/guobin/图片/bullet1.png',15)

    def __del__(self):
        # print('zidan')
        pass
 
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 700:
            self.kill()

















