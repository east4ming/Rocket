"""rocket class.

火箭的类.
- 初始化一个火箭.
- 加载绘制一个图片.
- 放置火箭在**屏幕**中央
"""

import pygame
# from settings import Settings


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

    def blitme(self):
        """绘制火箭."""
        self.screen.blit(self.image, self.rect)

    def move_rocket(self, rkt_settings):
        if self.move_up_flag and self.rect.top > 0:
            self.rect.centery -= rkt_settings.rocket_spd
        elif self.move_down_flag and self.rect.bottom < rkt_settings.screen_height:
            self.rect.centery += rkt_settings.rocket_spd
        elif self.move_left_flag and self.rect.left > 0:
            self.rect.centerx -= rkt_settings.rocket_spd
        elif self.move_right_flag and self.rect.right < rkt_settings.screen_width:
            self.rect.centerx += rkt_settings.rocket_spd
