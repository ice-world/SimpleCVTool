# import tkinter as tk
# from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np


import values as Va
from windows import *
import binarize_image
from files import *
import draw


def zoom_in():
    Va.img_cv = cv2.resize(
        Va.img_cv, None, fx=1.05, fy=1.05, interpolation=cv2.INTER_AREA
    )
    Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)  # 移动到当前位置，使放大缩小后位置不变


def zoom_out():
    Va.img_cv = cv2.resize(
        Va.img_cv, None, fx=0.95, fy=0.95, interpolation=cv2.INTER_AREA
    )
    Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)


def on_canvas_click(event):
    if Va.drawing is True:
        Va.drawing_x = event.x - Va.curX
        Va.drawing_y = event.y - Va.curY
    else:
        canvas.start_drag_x = event.x
        canvas.start_drag_y = event.y
    update_status_bar(event.x, event.y)


def on_canvas_release(event):
    if Va.drawing is True:
        Va.drawing = False
        if Va.drawing_type == "rectangle":
            draw.draw_opencv_rectangle(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                Va.img_cv,
            )
        elif Va.drawing_type == "circle":
            draw.draw_opencv_circle(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                Va.img_cv,
            )
        elif Va.drawing_type == "line":
            draw.draw_opencv_line(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                Va.img_cv,
            )
        elif Va.drawing_type == "point":
            draw.draw_opencv_point(
                event.x - Va.curX,
                event.y - Va.curY,
                Va.img_cv,
            )


def on_canvas_drag(event):
    if Va.drawing is True:
        if Va.drawing_type == "rectangle":
            temp_img_cv = Va.img_cv.copy()
            draw.draw_opencv_rectangle(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                temp_img_cv,
            )
        elif Va.drawing_type == "circle":
            temp_img_cv = Va.img_cv.copy()
            draw.draw_opencv_circle(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                temp_img_cv,
            )
        elif Va.drawing_type == "line":
            temp_img_cv = Va.img_cv.copy()
            draw.draw_opencv_line(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                temp_img_cv,
            )
        elif Va.drawing_type == "point":
            draw.draw_opencv_point(
                event.x - Va.curX,
                event.y - Va.curY,
                Va.img_cv,
            )
    else:
        delta_x = event.x - canvas.start_drag_x
        delta_y = event.y - canvas.start_drag_y
        Va.curX += delta_x
        Va.curY += delta_y
        canvas.move("image", delta_x, delta_y)
        canvas.start_drag_x = event.x
        canvas.start_drag_y = event.y
        update_status_bar(event.x, event.y)


def on_canvas_move(event):
    update_status_bar(event.x, event.y)


def processWheel(event):
    if event.delta > 0:
        zoom_in()  # 滚轮往上滚动，放大
    else:
        zoom_out()  # 滚轮往下滚动，缩小


def update_status_bar(x, y):
    if Va.img_cv is not None:
        height, width, _ = Va.img_cv.shape
        if Va.curX <= x < width + Va.curX and Va.curY <= y < height + Va.curY:
            color = Va.img_cv[y - Va.curY, x - Va.curX]
            status_bar.config(
                text=f"位置：({x - Va.curX}, {y - Va.curY}) 颜色：(BGR) {color}"
            )
        else:
            status_bar.config(text="鼠标在画布外")
    else:
        status_bar.config(text="没有打开图片")


if __name__ == "__main__":
    Va.InitValues()

    canvas.bind("<ButtonPress-1>", on_canvas_click)
    canvas.bind("<B1-Motion>", on_canvas_drag)
    canvas.bind("<MouseWheel>", processWheel)
    canvas.bind("<Motion>", on_canvas_move)
    canvas.bind("<ButtonRelease>", on_canvas_release)

    root.title(f"{Va.SOFTWARE_NAME} - {Va.SOFTWARE_AUTHOR}")

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="文件", menu=file_menu)
    file_menu.add_command(label="新建", command=new_image)  # New
    file_menu.add_command(label="打开", command=open_image)  # Open
    file_menu.add_command(label="保存", command=save_image)  # Save

    zoom_menu = tk.Menu(menu)
    menu.add_cascade(label="缩放", menu=zoom_menu)
    zoom_menu.add_command(label="放大", command=zoom_in)
    zoom_menu.add_command(label="缩小", command=zoom_out)

    edit_menu = tk.Menu(menu)
    menu.add_cascade(label="编辑", menu=edit_menu)
    edit_menu.add_command(label="二值化", command=binarize_image.show_input_window)

    draw_menu = tk.Menu(menu)
    menu.add_cascade(label="绘图", menu=draw_menu)

    shape_menu = tk.Menu(draw_menu)
    draw_menu.add_cascade(label="图形", menu=shape_menu)
    shape_menu.add_command(label="矩形", command=draw.draw_rectangle)
    shape_menu.add_command(label="圆", command=draw.draw_circle)
    shape_menu.add_command(label="线", command=draw.draw_line)
    # shape_menu.add_command(label="多边形", command=lambda: set_shape("polygon"))
    shape_menu.add_command(label="曲线", command=draw.draw_point)

    color_menu = tk.Menu(draw_menu)
    draw_menu.add_cascade(label="颜色", menu=color_menu)
    color_menu.add_command(label="红", command=lambda: draw.set_drawing_color("red"))
    color_menu.add_command(label="绿", command=lambda: draw.set_drawing_color("green"))
    color_menu.add_command(label="蓝", command=lambda: draw.set_drawing_color("blue"))

    width_menu = tk.Menu(draw_menu)
    draw_menu.add_cascade(label="线宽", menu=width_menu)
    width_menu.add_command(label="1", command=lambda: draw.set_drawing_width(1))
    width_menu.add_command(label="2", command=lambda: draw.set_drawing_width(2))
    width_menu.add_command(label="3", command=lambda: draw.set_drawing_width(3))

    root.mainloop()
