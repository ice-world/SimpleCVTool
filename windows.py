import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
global root
global canvas

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
