global img, img_cv, img_tk
global curX, curY

global SOFTWARE_NAME, SOFTWARE_AUTHOR


def InitValues():
    global img, img_cv, img_tk
    global curX, curY  # 记录当前位置，使放大缩小后位置不变
    global SOFTWARE_NAME,SOFTWARE_AUTHOR
    img = None
    img_cv = None
    img_tk = None
    curX = 0
    curY = 0

    SOFTWARE_NAME = "SimpleCVTool"
    SOFTWARE_AUTHOR = "Xunchi Zhang"
