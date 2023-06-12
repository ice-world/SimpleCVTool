import cv2
import numpy as np
import values as Va
from windows import *
from tkinter import filedialog, simpledialog

def show_canny_input_window():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    def apply_canny():
        lower_threshold = int(lower_threshold_entry.get())
        upper_threshold = int(upper_threshold_entry.get())
        canny_edge_detection(lower_threshold, upper_threshold)
        input_window.destroy()

    input_window = tk.Toplevel()
    input_window.title("Canny 参数输入")

    lower_threshold_label = tk.Label(input_window, text="下阈值：")
    lower_threshold_label.grid(row=0, column=0)
    lower_threshold_entry = tk.Entry(input_window)
    lower_threshold_entry.grid(row=0, column=1)

    upper_threshold_label = tk.Label(input_window, text="上阈值：")
    upper_threshold_label.grid(row=1, column=0)
    upper_threshold_entry = tk.Entry(input_window)
    upper_threshold_entry.grid(row=1, column=1)

    apply_button = tk.Button(input_window, text="确定", command=apply_canny)
    apply_button.grid(row=2, columnspan=2)

    Va.in_operation = False

def canny_edge_detection(lower_threshold, upper_threshold):
    if Va.img_cv is not None:
        gray = None
        if len(Va.img_cv.shape) == 3:
            gray = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = Va.img
        edges = cv2.Canny(gray, lower_threshold, upper_threshold)
        Va.img_cv = edges
        update_image()

def find_external_contours():
    if Va.in_operation == True:
        return
    Va.in_operation = True
    if Va.img_cv is not None:
        gray = None
        if len(Va.img_cv.shape) == 3:
            gray = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = Va.img
        threshold = simpledialog.askfloat("边缘检测", "请输入阈值:", initialvalue=127)
        _, thresh = cv2.threshold(gray,threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(Va.img_cv, contours, -1, (0, 255, 0), 2)
        update_image()
    Va.in_operation = False

def fill_contours():
    if Va.in_operation == True:
        return
    Va.in_operation = True
    if Va.img_cv is not None:
        gray = None
        if len(Va.img_cv.shape) == 3:
            gray = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2GRAY)
        else:
            gray = Va.img
        threshold = simpledialog.askfloat("填充轮廓", "请输入阈值:", initialvalue=127)
        _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(Va.img_cv, contours, -1, (0, 255, 0), cv2.FILLED)
        update_image()
    Va.in_operation = False
