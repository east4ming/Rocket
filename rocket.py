"""rocket class.

火箭的类.
- 初始化一个火箭.
- 加载绘制一个图片.
- 放置火箭在**屏幕**中央
"""

import pygame
from settings import Settings


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
        # 火箭移动标志
        self.move_up_flag = False
        self.move_down_flag = False
        self.move_left_flag = False
        self.move_right_flag = False
        # 火箭速度
        self.rocket_spd = 1

    def blitme(self):
        """绘制火箭."""
        self.screen.blit(self.image, self.rect)

    def move_rocket(self):
        if self.move_up_flag and self.rect.top > 0:
            self.rect.centery -= self.rocket_spd
        elif self.move_down_flag and self.rect.bottom < Settings().screen_height:
            self.rect.centery += self.rocket_spd
        elif self.move_left_flag and self.rect.left > 0:
            self.rect.centerx -= self.rocket_spd
        elif self.move_right_flag and self.rect.right < Settings().screen_width:
            self.rect.centerx += self.rocket_spd
