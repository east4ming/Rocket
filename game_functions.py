"""游戏运行相关函数.

- 游戏初始化
-
"""


import pygame
import sys
import random
import time

def keyup_event(event, rocket):
    if event.key == pygame.K_UP:
        rocket.move_up_flag = True
    elif event.key == pygame.K_DOWN:
        rocket.move_down_flag = True
    elif event.key == pygame.K_LEFT:
        rocket.move_left_flag = True
    elif event.key == pygame.K_RIGHT:
        rocket.move_right_flag = True


def keydown_event(event, rocket):
    if event.key == pygame.K_UP:
        rocket.move_up_flag = False
    elif event.key == pygame.K_DOWN:
        rocket.move_down_flag = False
    elif event.key == pygame.K_LEFT:
        rocket.move_left_flag = False
    elif event.key == pygame.K_RIGHT:
        rocket.move_right_flag = False


def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keyup_event(event, rocket)
        elif event.type == pygame.KEYUP:
            keydown_event(event, rocket)


def blitme(screen, rocket):
    """重绘所有对象."""
    time.sleep(0.3)
    screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    rocket.blitme()
    pygame.display.flip()
