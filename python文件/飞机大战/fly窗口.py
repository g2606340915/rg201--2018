import pygame
# 开始
pygame.init()

# display (窗口) 类
# set_mode() 方法 初始化我们的显示窗口
# update() 方法 刷新我们的屏幕
screen = pygame.display.set_mode((480,700))
# image.load
# 步骤1 加载图片数据
bg = pygame.image.load('/home/guobin/图片/background.png')
# 步骤2 绘制图片数据
screen.blit(bg,(0,0))
# 步骤3 更新显示
pygame.display.update()

# 英雄战机
# 步骤1 加载英雄图片数据
hero_fly = pygame.image.load('/home/guobin/图片/life.png')
# 步骤2 绘制到屏幕上
screen.blit(hero_fly,(100,500))
# 步骤3 更新屏幕显示
hero_rect = pygame.Rect(200,600,102,126)

screen.blit(hero_fly,hero_rect)
pygame.display.update()
# 设置英雄初始位置
# hero_rect = pygame.Rect(200,600,102,126)

# screen.blit(hero_fly,hero_rect)
'''
# 敌人
hero_fly = pygame.image.load('/home/guobin/图片/enemy2.png')
screen.blit(hero_fly,(400,100))
pygame.display.update()


# 敌人
hero_fly = pygame.image.load('/home/guobin/图片/enemy2.png')
screen.blit(hero_fly,(200,150))
pygame.display.update()

# 敌人
hero_fly = pygame.image.load('/home/guobin/图片/enemy2.png')
screen.blit(hero_fly,(100,120))
pygame.display.update()

# 炮弹
hero_fly = pygame.image.load('/home/guobin/图片/bullet2.png')
screen.blit(hero_fly,(100,300))
pygame.display.update()

# 炮弹
hero_fly = pygame.image.load('/home/guobin/图片/bullet2.png')
screen.blit(hero_fly,(120,400))
pygame.display.update()
'''

# 游戏时钟
clock = pygame.time.Clock()

i = 0

while True:
    # 设置帧率
    clock.tick(60)
    # 铺货事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        print('退出游戏')
        pygame.quit()
        exit()
    ''''
    # 设置y轴的值
    
    if hero_rect.y == 0:
        hero_rect.y = 600
    else:
        hero_rect.y = hero_rect.y - 1
    hero_rect.x = hero_rect.x + 1
    # 重新设置一下坐标
    screen.blit(bg,(0,0))

    # 绘制英雄的坐标
    screen.blit(hero_fly,hero_rect)

    # 更新屏幕
    pygame.display.update()
    # print(hero_rect.x,hero_rect.y)
    '''
    i += 1

    pass


# 结束
pygame.quit()
