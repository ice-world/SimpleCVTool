global img, img_cv, img_tk
global curX, curY

global SOFTWARE_NAME, SOFTWARE_AUTHOR

global drawing
global drawing_type
global drawing_x, drawing_y
global color, drawing_width
global drawing_text


def InitValues():
    global img, img_cv, img_tk
    global curX, curY  # 记录当前位置，使放大缩小后位置不变
    global SOFTWARE_NAME, SOFTWARE_AUTHOR

    global drawing
    global drawing_type
    global drawing_x, drawing_y
    global color, drawing_width
    global drawing_text

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
