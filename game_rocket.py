"""The Rocket main function.

- 一个Screen(有背景)
- 一个Rocket
- Rocket可以上下左右移动
- Rocket不能移动出Screen
"""

import pygame
import sys

from rocket import Rocket
from settings import Settings

def run_game():
    pygame.init()
    rkt_settings = Settings()
    screen = pygame.display.set_mode((rkt_settings.screen_width, rkt_settings.screen_height))
    pygame.display.set_caption('Rocket')
    # 初始化火箭对象
    rocket = Rocket(screen)


    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 代码太长, 待优化
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rocket.move_up_flag = True
                elif event.key == pygame.K_DOWN:
                    rocket.move_down_flag = True
                elif event.key == pygame.K_LEFT:
                    rocket.move_left_flag = True
                elif event.key == pygame.K_RIGHT:
                    rocket.move_right_flag = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.move_up_flag = False
                elif event.key == pygame.K_DOWN:
                    rocket.move_down_flag = False
                elif event.key == pygame.K_LEFT:
                    rocket.move_left_flag = False
                elif event.key == pygame.K_RIGHT:
                    rocket.move_right_flag = False
            screen.fill(rkt_settings.bg_color)
        # 响应箭头, 移动火箭
        rocket.move_rocket()
        # 绘制火箭
        rocket.blitme()
        pygame.display.flip()


run_game()