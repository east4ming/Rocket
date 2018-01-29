"""The Rocket main function.

- 一个Screen(有背景)
- 一个Rocket
- Rocket可以上下左右移动
- Rocket不能移动出Screen
"""

import pygame
import sys

from rocket import Rocket

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Rocket')
    # 初始化火箭对象
    rocket = Rocket(screen)


    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill((230, 230, 230))
            # 绘制火箭
            rocket.blitme()
            pygame.display.flip()


run_game()