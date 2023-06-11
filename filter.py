import tkinter as tk
from tkinter import simpledialog
from windows import *
import values as Va
import cv2

def mean_filter():
    if Va.in_operation == True:
        return
    Va.in_operation = True
    ksize = simpledialog.askinteger("均值滤波", "请输入滤波核大小(奇数):", initialvalue=3, minvalue=1)
    if ksize is not None and ksize % 2 == 1:
        Va.img_cv = cv2.blur(Va.img_cv, (ksize, ksize))
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.delete("image")
        canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
        canvas.move("image", Va.curX, Va.curY) 

    Va.in_operation = False


def gaussian_filter():
    if Va.in_operation == True:
        return
    Va.in_operation = True
    ksize = simpledialog.askinteger("高斯滤波", "请输入滤波核大小(奇数):", initialvalue=3, minvalue=1)
    sigma = simpledialog.askfloat("高斯滤波", "请输入标准差:", initialvalue=0)
    if ksize is not None and ksize % 2 == 1:
        Va.img_cv = cv2.GaussianBlur(Va.img_cv, (ksize, ksize), sigma)
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.delete("image")
        canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
        canvas.move("image", Va.curX, Va.curY) 

    Va.in_operation = False


def median_filter():
    if Va.in_operation == True:
        return
    Va.in_operation = True
    ksize = simpledialog.askinteger("中值滤波", "请输入滤波核大小(奇数):", initialvalue=3, minvalue=1)
    if ksize is not None and ksize % 2 == 1:
        Va.img_cv = cv2.medianBlur(Va.img_cv, ksize)
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.delete("image")
        canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
        canvas.move("image", Va.curX, Va.curY)  
    Va.in_operation = False

