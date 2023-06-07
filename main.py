import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox

def open_image():
    global curX,curY    #记录当前位置，使放大缩小后位置不变
    curX = 0
    curY = 0
    file_path = filedialog.askopenfilename()
    if file_path:
        global img, img_cv, img_tk
        img_cv = cv2.imread(file_path)
        img = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk, tags="image")


def zoom_in():
    global img, img_cv, img_tk
    global curX, curY
    img_cv = cv2.resize(img_cv, None, fx=1.05, fy=1.05, interpolation=cv2.INTER_AREA)
    img = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    img_tk = ImageTk.PhotoImage(img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk, tags="image")
    canvas.move("image", curX, curY)    #移动到当前位置，使放大缩小后位置不变


def zoom_out():
    global img, img_cv, img_tk
    global curX, curY
    img_cv = cv2.resize(img_cv, None, fx=0.95, fy=0.95, interpolation=cv2.INTER_AREA)
    img = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    img_tk = ImageTk.PhotoImage(img)
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk, tags="image")
    canvas.move("image", curX, curY)


def binarize_image(threshold):
    global img, img_cv,img_tk
    if img_cv is None:
        messagebox.showerror("Error", "No image loaded.")
        return
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    _, binarized = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    img_cv = binarized
    img = img_cv
    img_tk = ImageTk.PhotoImage(Image.fromarray(binarized))
    canvas.delete("image")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk,tags="image")
    #canvas.config(width=img.width(), height=img.height())
    canvas.move("image", curX, curY)


def on_canvas_click(event):
    canvas.start_drag_x = event.x
    canvas.start_drag_y = event.y


def on_canvas_drag(event):
    global curX, curY
    delta_x = event.x - canvas.start_drag_x
    delta_y = event.y - canvas.start_drag_y
    curX += delta_x
    curY += delta_y
    canvas.move("image", delta_x, delta_y)
    canvas.start_drag_x = event.x
    canvas.start_drag_y = event.y


def processWheel(event):
    if event.delta > 0:
        zoom_in()  # 滚轮往上滚动，放大
    else:
        zoom_out()  # 滚轮往下滚动，缩小


img = None
img_cv = None

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

canvas.bind("<ButtonPress-1>", on_canvas_click)
canvas.bind("<B1-Motion>", on_canvas_drag)
canvas.bind("<MouseWheel>", processWheel)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="打开", command=open_image)  # Open

zoom_menu = tk.Menu(menu)
menu.add_cascade(label="缩放", menu=zoom_menu)
zoom_menu.add_command(label="放大", command=zoom_in)
zoom_menu.add_command(label="缩小", command=zoom_out)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="编辑",menu = edit_menu)
edit_menu.add_command(label="二值化",command=lambda: binarize_image(122))

root.mainloop()
