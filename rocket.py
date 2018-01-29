"""rocket class.

火箭的类.
- 初始化一个火箭.
- 加载绘制一个图片.
- 放置火箭在**屏幕**中央
"""

import pygame


class Rocket():
    def __init__(self, screen):
        # 获取窗口信息
        self.screen = screen
        # 加载火箭图片
        self.image = pygame.image.load('images/rocket.png')
        # 获取火箭外接矩形及屏幕窗口外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 放置火箭到窗口中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """绘制火箭."""
        self.screen.blit(self.image, self.rect)