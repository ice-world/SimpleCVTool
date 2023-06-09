import cv2
import numpy as np

from windows import *
import values as Va


def open_image():
    Va.curX = 0
    Va.curY = 0
    file_path = filedialog.askopenfilename(filetypes=[("图片", ".jpg .png")])
    if file_path:
        Va.img = Image.open(file_path)
        Va.img_cv = np.array(Va.img)
        Va.img_cv = cv2.cvtColor(Va.img_cv, cv2.COLOR_RGB2BGR)
        # Va.img_cv = cv2.imread(file_path) 中文文件名无法正确读取
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
        root.title(f"{Va.SOFTWARE_NAME} - {Va.SOFTWARE_AUTHOR} - {file_path}")


def save_image():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".jpg", filetypes=[("JPEG文件", "*.jpg"), ("PNG文件", "*.png")]
    )
    if file_path:  # 如果用户选择了保存路径
        # cv2.imwrite(file_path, Va.img_cv) 中文文件名无法正确保存
        Va.img.save(file_path)


def new_image():
    Va.curX = 0
    Va.curY = 0
    file_path = "new_image"
    Va.img_cv = np.ones((512, 512, 3), np.uint8)
    Va.img_cv *= 255
    Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    root.title(f"{Va.SOFTWARE_NAME} - {Va.SOFTWARE_AUTHOR} - {file_path}")
