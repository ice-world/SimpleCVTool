import values as Va
from windows import *
import cv2


def binarize_image(threshold):
    if Va.img_cv is None:
        messagebox.showerror("Error", "No image loaded.")
        return
    if len(Va.img_cv.shape) == 2:
        messagebox.showerror("Error", "已经是灰度图")
        return
    gray = cv2.cvtColor(Va.img_cv, cv2.COLOR_BGR2GRAY)
    _, binarized = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    Va.img_cv = binarized
    Va.img = Va.img_cv
    Va.img_tk = ImageTk.PhotoImage(Image.fromarray(binarized))
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=Va.img_tk, tags="image")
    # canvas.config(width=img.width(), height=img.height())
    canvas.move("image", Va.curX, Va.curY)
