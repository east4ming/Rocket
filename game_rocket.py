"""The Rocket main function.

- 一个Screen(有背景)
- 一个Rocket
- Rocket可以上下左右移动
- Rocket不能移动出Screen
"""

import pygame

from rocket import Rocket
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    rkt_settings = Settings()
    screen = pygame.display.set_mode((rkt_settings.screen_width, rkt_settings.screen_height))
    pygame.display.set_caption('CASEY ROCKET')
    # 初始化火箭对象
    rocket = Rocket(screen)

    # 游戏主循环
    while True:
        gf.check_events(screen, rkt_settings, rocket)
        # 响应箭头, 移动火箭
        rocket.move_rocket(rkt_settings)
        # 如果`screen.fill(rkt_settings.bg_color)`这一句放在`check_events()`的for循环里, 就会出现火箭残影
        # 重绘函数
        gf.blime(rocket)


run_game()
