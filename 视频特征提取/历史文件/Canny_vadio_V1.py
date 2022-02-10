'''
@auther:Jelly
用途：实现将一段视频内容进行Canny边缘检测提取边缘特征

'''

import cv2
import numpy as np
import os
import subprocess


#os.chdir()  # 用于改变当前工作目录到指定的路径
v_path = '测试序列.mp4'
image_save = './输出图片'

cap = cv2.VideoCapture(v_path)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 视频文件中的帧数。

# 进行灰度化和边缘检测
for i in range(int(frame_count)):
    _,img = cap.read()
    detected_edges = cv2.GaussianBlur(img,(3,3),0) # 高斯滤波
    detected_edges = cv2.Canny(detected_edges,50,180) # 边缘检测
    cv2.imwrite('./输出图片/image{}.jpg'.format(i),detected_edges) # 保存处理后的图片

# 合并帧成视频
images_path = image_save + '/image%d.jpg'
# 帧率
fps = str(24)
str_cmd = 'ffmpeg -i ' + images_path +' -r ' + fps + ' output.mp4'
p = subprocess.Popen(str_cmd, shell=True, stdout=None, stderr=None)
stdout, stderror = p.communicate()