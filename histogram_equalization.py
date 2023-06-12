import values as Va
from windows import *
import cv2
from tkinter import filedialog, Scale


def show_local_histogram_equalization_window():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    local_window = tk.Toplevel(root)
    local_window.title("局部直方图均衡化")
    local_window.geometry("200x100")

    block_size_label = tk.Label(local_window, text="块大小:")
    block_size_label.pack()
    block_size_entry = tk.Entry(local_window)
    block_size_entry.pack()

    apply_button = tk.Button(local_window, text="应用", command=lambda: local_histogram_equalization(int(block_size_entry.get())))
    apply_button.pack()

    Va.in_operation = False

def show_clahe_window():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    clahe_window = tk.Toplevel(root)
    clahe_window.title("限制对比度自适应直方图均衡化")
    clahe_window.geometry("200x150")

    clip_limit_label = tk.Label(clahe_window, text="剪切限制:")
    clip_limit_label.pack()
    clip_limit_entry = tk.Entry(clahe_window)
    clip_limit_entry.pack()

    block_size_label = tk.Label(clahe_window, text="块大小:")
    block_size_label.pack()
    block_size_entry = tk.Entry(clahe_window)
    block_size_entry.pack()

    apply_button = tk.Button(clahe_window, text="应用", command=lambda: contrast_limited_adaptive_histogram_equalization(float(clip_limit_entry.get()), int(block_size_entry.get())))
    apply_button.pack()

    Va.in_operation = False

def global_histogram_equalization():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    if Va.img_cv is None:
        return

    if len(Va.img_cv.shape) == 3:
        img_yuv = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        Va.img_cv = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    else:
        Va.img_cv = cv2.equalizeHist(Va.img_cv)

    update_image()
    Va.in_operation = False

def local_histogram_equalization(block_size):
    if Va.img_cv is None:
        return

    if len(Va.img_cv.shape) == 3:
        img_yuv = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(block_size, block_size))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        Va.img_cv = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    else:
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(block_size, block_size))
        Va.img_cv = clahe.apply(Va.img_cv)

    update_image()

def contrast_limited_adaptive_histogram_equalization(clip_limit, block_size):
    if Va.img_cv is None:
        return

    if len(Va.img_cv.shape) == 3:
        img_yuv = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(block_size, block_size))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        Va.img_cv = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    else:
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(block_size, block_size))
        Va.img_cv = clahe.apply(Va.img_cv)

    update_image()