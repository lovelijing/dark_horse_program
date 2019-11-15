import pygame

# 初始化pygame后才能使用pygame的其它功能。
pygame.init()
print("游戏代码。。。")

# 创建英雄矩形，并打印矩形大小。（注：Rect方法可以放在init方法之前）
hero_rect = pygame.Rect(100,500,120,126)
print(hero_rect.size)

# 创建并显示游戏窗口。
screen = pygame.display.set_mode((480,700))

# 绘制游戏背景图片。
# 1、用pygame.image.load方法加载图片文件到内存。
# 2、用屏幕对象的blit方法在内存窗口中绘制背景图像。
# 3、用pygame.display.update()方法可以一次性将blit方法绘制的最终结果显示在窗口中。
bg = pygame.image.load(".\\images\\background.png")
screen.blit(bg,(0,0))
# pygame.display.update()

# 绘制英雄的飞机。（方法同显示背景图片相同）
hero = pygame.image.load(".\\images\\me1.png")
screen.blit(hero,(200,500))
pygame.display.update()


# 开始游戏循环。
while True:
    pass

# 关闭pygame。
pygame.quit()