import cv2
import numpy as np
import values as Va
from windows import *
from tkinter import filedialog, simpledialog



def show_morphology_input_window(operation):
    if Va.in_operation == True:
        return
    Va.in_operation = True
    input_win = tk.Toplevel()
    input_win.title(f"{operation} 输入参数")

    kernel_label = tk.Label(input_win, text="核大小:")
    kernel_label.grid(row=0, column=0)
    kernel_entry = tk.Entry(input_win)
    kernel_entry.grid(row=0, column=1)

    iterations_label = tk.Label(input_win, text="迭代次数:")
    iterations_label.grid(row=1, column=0)
    iterations_entry = tk.Entry(input_win)
    iterations_entry.grid(row=1, column=1)

    def on_submit():
        kernel_size = int(kernel_entry.get())
        iterations = int(iterations_entry.get())
        perform_morphology_operation(operation, kernel_size, iterations)
        input_win.destroy()

    submit_button = tk.Button(input_win, text="确定", command=on_submit)
    submit_button.grid(row=2, column=0, columnspan=2)

    Va.in_operation = False

def perform_morphology_operation(operation, kernel_size, iterations):
    if Va.img_cv is None:
        return

    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    if operation == "opening":
        result = cv2.morphologyEx(Va.img_cv, cv2.MORPH_OPEN, kernel, iterations=iterations)
    elif operation == "closing":
        result = cv2.morphologyEx(Va.img_cv, cv2.MORPH_CLOSE, kernel, iterations=iterations)
    elif operation == "dilation":
        result = cv2.dilate(Va.img_cv, kernel, iterations=iterations)
    elif operation == "erosion":
        result = cv2.erode(Va.img_cv, kernel, iterations=iterations)

    Va.img_cv = result
    update_image()
