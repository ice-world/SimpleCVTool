import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

global root
global canvas

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

status_bar_drawing = tk.Label(root, text="准备", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar_drawing.pack(side=tk.BOTTOM, fill=tk.X)

status_bar = tk.Label(root, text="准备", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)