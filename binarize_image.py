import values as Va
from windows import *
import cv2
import numpy as np

'''用于debug滤波的函数
def gasuss_noise(image, mean=0, var=0.001):
    """
        添加高斯噪声
        mean : 均值
        var : 方差
    """
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out
'''
def show_input_window():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    input_window = tk.Toplevel(root)
    input_window.title("输入阈值")
    input_window.geometry("200x100")

    threshold_label = tk.Label(input_window, text="请输入阈值(0-255):")
    threshold_label.pack(pady=10)

    threshold_entry = tk.Entry(input_window)
    threshold_entry.pack()

    confirm_button = tk.Button(input_window, text="确定", command=lambda: binarize_image(input_window, threshold_entry))
    confirm_button.pack(pady=10)

    Va.in_operation = False

def binarize_image(input_window, threshold_entry):
    threshold = int(threshold_entry.get())
    input_window.destroy()
    if Va.img_cv is None:
        messagebox.showerror("Error", "当前无图片")
        return
    if len(Va.img_cv.shape) == 2:
        messagebox.showerror("Error", "已经是灰度图")
        return
    gray = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2GRAY)
    _, binarized = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    
    #bi = gasuss_noise(binarized, mean=0, var=0.01)  # 均值为0，方差为0.01
    Va.img_cv = binarized
    Va.img = Image.fromarray(Va.img_cv)
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    # canvas.config(width=img.width(), height=img.height())
    canvas.move("image", Va.curX, Va.curY)
