import values as Va
import cv2
from windows import *
import numpy as np


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
