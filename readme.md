# SimpleCVTool
---
一个简易的图形界面图像处理工具

使用python的tkinter框架开发，基于OpenCV实现底层的图像处理功能

计算机图像处理期末大作业

---


## 需要实现的功能

目前还未实现全部功能

### 图像处理

1. 二值化 (已完成)
2. 几何变换 
    1. 旋转 (已完成)
    2. 放大 (已完成)
    3. 缩小 (已完成)
    4. 裁剪 (已完成)
3. 滤波
    1. 均值 
    2. 高斯  
    3. 中值 
4. 直方图均衡化 
    1. 局部 
    2. 全局 
    3. 限制对比度自适应 
5. 形态学操作 
    1. 开 
    2. 闭 
    3. 膨胀 
    4. 腐蚀 
6. 水印 
7. 边缘检测
    1. Canny 算法
    2. 外轮廓检测
    3. 填充轮廓

### GUI要求
1. 有菜单、工具栏、状态栏 (已完成)

2. 在软件界面上显示图像，软件标题栏要显示软件名称、作者信息和所打开的文件名 (已完成)

3. 图像处理时所需的参数能够用对话框来输入或者通过主界面上的控件来输入参数或者用鼠标交互操作来完成 (已完成)

4. 每次处理之后，要能在界面上显示当前处理结果；下次处理是对前面处理结果继续处理，而不是仍然对原图进行处理 (已完成)


### 交互功能
1. 鼠标在图片上时，在状态栏实时显示鼠标在图像中的位置，及该位置的颜色 (已完成)

2. 用鼠标滚轮进行图片的放大缩小 (已完成)

3. 当图片放大后，大于界面显示区域时，能够用鼠标进行平移操作 (已完成)

### 文件操作功能
1. 能用对话框选择图像文件（要用文件扩展名过滤）(已完成)

2. 能保存当前处理结果图，并用对话框选择图片保存路径和文件名。(已完成)

3. 能新建图像。(已完成)

### 画图功能

1. 能用鼠标在图像上画图形：矩形、圆、任意多边形、任意曲线 (已完成)

2. 能在图像上写字，位置由鼠标指定 (已完成)