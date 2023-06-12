# import tkinter as tk
# from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np


import values as Va
from windows import *
import binarize_image
import files
import draw
import geo_trans
import filter
import histogram_equalization
import edge_detection

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
        elif Va.drawing_type == "text":
            draw.draw_opencv_text(event.x - Va.curX, event.y - Va.curY, Va.img_cv)
        elif Va.drawing_type == "cut":
            geo_trans.cut_img(Va.drawing_x, Va.drawing_y, event.x - Va.curX, event.y - Va.curY)
            


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
        elif Va.drawing_type == "cut":
            temp_img_cv = Va.img_cv.copy()
            draw.draw_opencv_rectangle(
                Va.drawing_x,
                Va.drawing_y,
                event.x - Va.curX,
                event.y - Va.curY,
                temp_img_cv,
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
        geo_trans.zoom_in()  # 滚轮往上滚动，放大
    else:
        geo_trans.zoom_out()  # 滚轮往下滚动，缩小


def update_status_bar(x, y):
    if Va.img_cv is not None:
        if len(Va.img_cv.shape) == 3:
            height, width, _ = Va.img_cv.shape
            if Va.curX <= x < width + Va.curX and Va.curY <= y < height + Va.curY:
                color = Va.img_cv[y - Va.curY, x - Va.curX]
                status_bar.config(
                    text=f"位置：({x - Va.curX}, {y - Va.curY}) 颜色：(BGR) {color}"
                )
            else:
                status_bar.config(text="鼠标在画布外")
        else:
            height, width = Va.img_cv.shape
            if Va.curX <= x < width + Va.curX and Va.curY <= y < height + Va.curY:
                color = Va.img_cv[y - Va.curY, x - Va.curX]
                status_bar.config(
                    text=f"位置：({x - Va.curX}, {y - Va.curY}) 颜色：(灰度) {color}"
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
    file_menu.add_command(label="新建", command=files.new_image)  # New
    file_menu.add_command(label="打开", command=files.open_image)  # Open
    file_menu.add_command(label="保存", command=files.save_image)  # Save

    geometric_menu = tk.Menu(menu)
    menu.add_cascade(label="几何变换", menu=geometric_menu)
    geometric_menu.add_command(label="放大", command=geo_trans.zoom_in)
    geometric_menu.add_command(label="缩小", command=geo_trans.zoom_out)
    geometric_menu.add_command(label="旋转", command=geo_trans.show_rotation_window)
    geometric_menu.add_command(label="裁剪", command=geo_trans.cut_img_draw)
    edit_menu = tk.Menu(menu)
    menu.add_cascade(label="二值化", menu=edit_menu)
    edit_menu.add_command(label="二值化", command=binarize_image.show_input_window)

    draw_menu = tk.Menu(menu)
    menu.add_cascade(label="绘图", menu=draw_menu)

    shape_menu = tk.Menu(draw_menu)
    draw_menu.add_cascade(label="图形", menu=shape_menu)
    shape_menu.add_command(label="文字", command=draw.draw_text)
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
    
    filter_menu = tk.Menu(menu)
    menu.add_cascade(label="滤波", menu=filter_menu)
    filter_menu.add_command(label="均值滤波", command=filter.mean_filter)
    filter_menu.add_command(label="高斯滤波", command=filter.gaussian_filter)
    filter_menu.add_command(label="中值滤波", command=filter.median_filter)

    histogram_menu = tk.Menu(menu)
    menu.add_cascade(label="直方图均衡化", menu=histogram_menu)
    histogram_menu.add_command(label="全局直方图均衡化", command=histogram_equalization.global_histogram_equalization)
    histogram_menu.add_command(label="局部直方图均衡化", command=histogram_equalization.show_local_histogram_equalization_window)
    histogram_menu.add_command(label="限制对比度自适应直方图均衡化", command=histogram_equalization.show_clahe_window)

    edge_detection_menu = tk.Menu(menu)
    menu.add_cascade(label="边缘检测", menu=edge_detection_menu)
    edge_detection_menu.add_command(label="Canny 算法", command=edge_detection.show_canny_input_window)
    edge_detection_menu.add_command(label="外轮廓检测", command=edge_detection.find_external_contours)
    edge_detection_menu.add_command(label="填充轮廓", command=edge_detection.fill_contours)

    watermarks_menu = tk.Menu(menu)
    menu.add_cascade(label="水印", menu=watermarks_menu)
    watermarks_menu.add_command(label="水印", command=draw.draw_text)
    root.mainloop()
