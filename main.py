# !/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import numpy as np

file = r".\\pic\\123.jpg"
# step1:读取照片
img = cv2.imread(file)

# step1.2:缩放图片()
img = cv2.resize(img, None, fx=1.5, fy=1.5)
rows, cols, channels = img.shape
# 展示图片
cv2.imshow("original...", img)

# step2.1 图片转换为灰度图并显示
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# :图片的二值化处理
# 红底变蓝底
# 将在两个阈值内的像素值设置为白色（255），
# 而不在阈值区间内的像素值设置为黑色（0）
#
lower_red = np.array([0, 125, 125])
upper_red = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

# step2.3:腐蚀膨胀 若是腐蚀膨胀后仍有白色噪点，可以增加iterations的值
erode = cv2.erode(mask, None, iterations=5)
# cv2.imshow('erode', erode)
dilate = cv2.dilate(erode, None, iterations=7)

# step3遍历每个像素点，进行颜色的替换
'''
#若是想要将红底变成蓝底img[i,j]=(255,0,0)，
#若是想将蓝底变为红底则img[i,j]=(0,0,255),
#若是想变白底img[i,j]=(255,255,255)
'''
for i in range(rows):
    for j in range(cols):
        if dilate[i, j] == 255:  # 像素点255表示白色,180为灰度
            img[i, j] = (0, 0, 255)  # 此处替换颜色，为BGR通道，不是RGB通道

# step4 显示图像
new_file = r".\\pic\\123_red.png"
cv2.imwrite(new_file, img)
res = cv2.imread(new_file)
cv2.imshow('result...', res)
# 窗口等待的命令，0表示无限等待
cv2.waitKey(0)
