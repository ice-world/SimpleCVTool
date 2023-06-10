import values as Va
import cv2
from windows import *
import numpy as np
from tkinter import filedialog, simpledialog
from PIL import ImageFont, ImageDraw, Image

def update_status_bar_drawing():
    status_bar_drawing.config(text=f"画笔颜色：(BGR) {Va.color} 粗细：{Va.drawing_width}")


def draw_rectangle():
    Va.drawing = True
    Va.drawing_type = "rectangle"


def draw_circle():
    Va.drawing = True
    Va.drawing_type = "circle"


def draw_line():
    Va.drawing = True
    Va.drawing_type = "line"

def draw_point():
    Va.drawing = True
    Va.drawing_type = "point"


def draw_text():
    Va.drawing_type = "text"
    Va.drawing = True
    text = simpledialog.askstring("输入文本", "请输入要绘制的文本：")
    if text:
        Va.drawing_text = text
def draw_opencv_text(x, y, img_cv):

    font_scale = 1
    font_thickness = 2

    fontpath = "STSONG.TTF"                             #指定字体文件名    
    font = ImageFont.truetype(fontpath,36)         	#载入字体，设置字号
    draw = ImageDraw.Draw(Va.img)                      #创建Draw对象
    draw.text((x, y),Va.drawing_text,font=font,fill=(255,0,0))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    Va.img_cv = np.array(Va.img)   #将绘有文字的图片转换回opencv格式，保证信息同步  
    Va.img_cv = cv2.cvtColor(Va.img_cv, cv2.COLOR_RGB2BGR)      #将RGB的格式转化回BGR，和打开图片同理
    canvas.delete("image")  
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)



def draw_opencv_rectangle(x1, y1, x2, y2, cur_img):
    cv2.rectangle(cur_img, (x1, y1), (x2, y2), Va.color, Va.drawing_width)
    Va.img = Image.fromarray(cv2.cvtColor(cur_img, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)


def draw_opencv_circle(x1, y1, x2, y2, cur_img):
    cv2.circle(
        cur_img,
        (x1, y1),
        int(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)),
        Va.color,
        Va.drawing_width,
    )
    Va.img = Image.fromarray(cv2.cvtColor(cur_img, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)


def draw_opencv_line(x1, y1, x2, y2, cur_img):
    cv2.line(cur_img, (x1, y1), (x2, y2), Va.color, Va.drawing_width)
    Va.img = Image.fromarray(cv2.cvtColor(cur_img, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)


def draw_opencv_point(x1, x2, cur_img):
    cv2.circle(cur_img, (x1, x2), 0, Va.color, Va.drawing_width)
    Va.img = Image.fromarray(cv2.cvtColor(cur_img, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)


def set_drawing_type(draw_type):
    Va.drawing_type = draw_type


def set_drawing_color(draw_color):
    if draw_color == "red":
        Va.color = (0, 0, 255)
    elif draw_color == "green":
        Va.color = (0, 255, 0)
    elif draw_color == "blue":
        Va.color = (255, 0, 0)
    update_status_bar_drawing()


def set_drawing_width(draw_width):
    Va.drawing_width = draw_width
    update_status_bar_drawing()
