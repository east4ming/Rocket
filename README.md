# Rocket
A Game. There is a rocket on the center of the screen. Player control the rocket to move up/down/left/right. And make sure the rocket can't move to the outside of the screen.

## 游戏设计

- 一个Screen(有背景)
- 一个Rocket
- Rocket可以上下左右移动
- Rocket不能移动出Screen

### 游戏运行主函数

> 导入模块:
> - pygame
> - sys

1. 初始化: `pygame.init()`
2. 游戏窗口大小设置
3. 游戏标题设置
4. 游戏主循环(while循环, 捕获事件)
    1. 捕获事件列表, 使用for循环遍历该列表
    2. 查找是否有`pygame.QUIT`事件, 如果有, 执行`sys.exit()`
    3. 如果没有退出, 执行以下逻辑
        1. 使用选定背景色填充Screen
        2. 重绘屏幕

## 火箭

火箭的类

### `__init__()` 

1. `screen` 形参(后续根据它确定位置, screen来自`pygame.display.set_mode()`)
2. 初始化以下内容:
    1. `image` 来自`pygame.image.load()`
    2. `screen`
    3. 火箭外接矩形: `rect`
    4. `screen`外接矩形: `screen_rect`
    5. 位置: `self.rect.center=self.screen_rect.center`

### 绘制函数

`blitme()` - 2个参数: `image`和`rect`(对象和位置)

### 游戏主文件

- 初始化rocket对象
- 在循环中重绘rocket

## 重构

### 第一次重构

配置放到单独文件中`settings.py`
1. screen参数:
    - width
    - height
    - bg_color
2. ...

## 火箭移动

