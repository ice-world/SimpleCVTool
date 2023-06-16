import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import values as Va
import cv2

global root     #窗口变量
global canvas   #画布变量

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600) #设置画布大小
canvas.pack()

status_bar_drawing = tk.Label(root, text="准备", bd=1, relief=tk.SUNKEN, anchor=tk.W)   #画图状态栏设置
status_bar_drawing.pack(side=tk.BOTTOM, fill=tk.X)  #在窗口底部创建画图状态栏

status_bar = tk.Label(root, text="准备", bd=1, relief=tk.SUNKEN, anchor=tk.W)   #状态栏设置
status_bar.pack(side=tk.BOTTOM, fill=tk.X)  #在窗口底部创建状态栏

def update_image(): #Value.img_cv得到更新后，通过调用该函数更新画布上的图象
    if len(Va.img_cv.shape) == 2:   #根据图象类型进行转化
        Va.img = Image.fromarray(cv2.cvtColor(cv2.cvtColor(Va.img_cv, cv2.COLOR_GRAY2BGR), cv2.COLOR_BGR2RGB))
        print("update image gray")
    else:
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        print("update image")
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(Va.curX, Va.curY, anchor=tk.NW, image=Va.img_tk, tags="image")
    