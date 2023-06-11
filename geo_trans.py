# geometry_transformation

import values as Va
from windows import *
import cv2
from tkinter import filedialog, Scale


def zoom_in():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    Va.img_cv = cv2.resize(
        Va.img_cv, None, fx=1.05, fy=1.05, interpolation=cv2.INTER_AREA
    )
    Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)  # 移动到当前位置，使放大缩小后位置不变

    Va.in_operation = False


def zoom_out():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    Va.img_cv = cv2.resize(
        Va.img_cv, None, fx=0.95, fy=0.95, interpolation=cv2.INTER_AREA
    )
    Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
    Va.img_tk = ImageTk.PhotoImage(Va.img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    canvas.move("image", Va.curX, Va.curY)

    Va.in_operation = False


def show_rotation_window():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    rotation_window = tk.Toplevel(root)
    rotation_window.title("旋转角度")
    rotation_scale = Scale(
        rotation_window,
        from_=0,
        to=360,
        length=600,
        orient=tk.HORIZONTAL,
        command=rotate_image_show,
    )
    rotation_scale.pack()
    confirm_button = tk.Button(
        rotation_window,
        text="确定",
        command=lambda: rotate_image_confirm(rotation_window, rotation_scale.get()),
    )
    confirm_button.pack(pady=10)


def rotate_image_show(angle):
    if Va.img_cv is not None:
        Va.rotation_angle = int(angle)
        height = 0
        width = 0
        if len(Va.img_cv.shape) == 3:
            height, width, _ = Va.img_cv.shape
        else:
            height, width = Va.img_cv.shape
        center = (width // 2, height // 2)
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, Va.rotation_angle, 1)
        img_cv = cv2.warpAffine(Va.img_cv, rotation_matrix, (width, height))
        Va.img = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.delete("image")
        canvas.create_image(
            Va.curX, Va.curY, image=Va.img_tk, anchor=tk.NW, tags="image"
        )


def rotate_image_confirm(rotation_window, angle):
    rotation_window.destroy()
    Va.in_operation = False
    if Va.img_cv is not None:
        Va.rotation_angle = int(angle)
        height = 0
        width = 0
        if len(Va.img_cv.shape) == 3:
            height, width, _ = Va.img_cv.shape
        else:
            height, width = Va.img_cv.shape
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, Va.rotation_angle, 1)
        Va.img_cv = cv2.warpAffine(Va.img_cv, rotation_matrix, (width, height))
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.delete("image")
        canvas.create_image(
            Va.curX, Va.curY, image=Va.img_tk, anchor=tk.NW, tags="image"
        )


def cut_img_draw():
    if Va.in_operation == True:
        return
    Va.in_operation = True

    Va.drawing_type = "cut"
    Va.drawing = True


def cut_img(x1, y1, x2, y2):
    if Va.img_cv is not None:
        Va.curX = 0
        Va.curY = 0
        height = 0
        width = 0
        if len(Va.img_cv.shape) == 3:
            height, width, _ = Va.img_cv.shape
        else:
            height, width = Va.img_cv.shape
        y1 = max(0, y1)
        y2 = min(y2, height - 1)
        x1 = max(0, x1)
        x2 = min(x2, width - 1)
        cropped_img = Va.img_cv[y1:y2, x1:x2]

        Va.img_cv = cropped_img.copy()
        Va.img = Image.fromarray(cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2RGB))
        Va.img_tk = ImageTk.PhotoImage(Va.img)
        canvas.delete("image")
        canvas.create_image(0, 0, image=Va.img_tk, tags="image",anchor="nw")
        canvas.move("image", Va.curX, Va.curY)
        Va.in_operation = False
