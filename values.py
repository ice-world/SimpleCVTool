global img, img_cv, img_tk #分别代表RGB格式图象，opencv的BGR格式图象，用于显示在画布上的图象
global curX, curY   #记录当前相对于左上角的移动位置

global SOFTWARE_NAME, SOFTWARE_AUTHOR   #作者信息

#画图相关变量
global drawing  #是否在进行画图   True/False
global drawing_type #画笔类型
global drawing_x, drawing_y     #画笔起始位置
global color, drawing_width     #画笔状态信息
global drawing_text     #存储绘画的文字

global in_operation #锁，确保同时只能进行一个操作

def InitValues():   #初始化所有变量
    global img, img_cv, img_tk
    global curX, curY  # 记录当前位置，使放大缩小后位置不变
    global SOFTWARE_NAME, SOFTWARE_AUTHOR

    global drawing
    global drawing_type
    global drawing_x, drawing_y
    global color, drawing_width
    global drawing_text

    global in_operation

    color = (255, 0, 0)
    drawing_width = 1
    drawing = False
    drawing_type = "rectangle"
    drawing_x = 0
    drawing_y = 0

    img = None
    img_cv = None
    img_tk = None
    curX = 0
    curY = 0

    SOFTWARE_NAME = "SimpleCVTool"
    SOFTWARE_AUTHOR = "Xunchi Zhang"

    in_operation = False
