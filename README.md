# Rocket
A Game. There is a rocket on the center of the screen. Player control the rocket to move up/down/left/right. And make sure the rocket can't move to the outside of the screen.

> 亮瞎你钛合金狗眼的Casey Rocket飞行
> 背景颜色随机
> 增加 time.sleep(0.3) 来让颜色变得慢一点
> 增大rocket speed来让它移动快一点

## 游戏设计

- 一个Screen(有背景)
- 一个Rocket
- Rocket可以上下左右移动
- Rocket不能移动出Screen

## 游戏运行主函数

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

### 火箭移动

`rocket.py`增加`move_rocket()`函数.

1. 设置移动标志, 默认为False, 为True时移动
2. 检测KEYUP/KEYDOWN事件
    1. 如果KEYDOWN, 移动标志改为True
    2. 如果KEYUP, 移动标志改为False
3. 火箭移动: 移动标志为True且火箭不在边界上, 则以火箭速度进行移动

## 重构

### 第一次重构

配置放到单独文件中`settings.py`
1. screen参数:
    - width
    - height
    - bg_color
2. 火箭速度

### 第二次重构

游戏运行主函数单独拆分为文件`game_functions.py`, 包含:

- `keyup_event()`
- `keydown_event()`
- `check_event()`
- `blitme()`

#### `keyup_event()`

如果KEYDOWN, 移动标志改为True

#### `keydown_event()`

如果KEYUP, 移动标志改为False

#### `check_event()`

检查以下事件并响应:

1. 退出事件 -> 退出进程
2. `KEYDOWN`事件 -> 移动标志为True
3. `KEYUP`事件 -> 移动标志为False

#### `blitme()`

重绘以下内容:

1. screen背景色填充
2. 火箭重绘
3. 最后绘制的元素总是显示在上
