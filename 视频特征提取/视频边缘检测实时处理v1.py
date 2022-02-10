import cv2
import time

import numpy as np

######################     视频载入       #############################
cap = cv2.VideoCapture("测试序列.mp4")
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video_width = int(cap.get(3))
video_height = int(cap.get(4))
video_fps = int(cap.get(5))
out = cv2.VideoWriter('output1.mp4', fourcc, video_fps, (video_width, video_height))   # 视频写入时，其视频的帧宽度与高度与原视频一致

#####################       模型载入      #############################
def img_Canny(img,lowThreshold):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_C = cv2.GaussianBlur(img, (3, 3), 0)  # 高斯滤波
    img_C = cv2.Canny(img_C, lowThreshold, lowThreshold*3,apertureSize = 3)  # 边缘检测
    img_C = cv2.cvtColor(img_C,cv2.COLOR_GRAY2BGR)
    print('lowThreshold', lowThreshold)
    return img_C


def update_lowThreshold(x):
    global lowThreshold,frame_C,frame
    lowThreshold = cv2.getTrackbarPos('low Threshold','image')
    frame_C=img_Canny(frame, lowThreshold)
    cv2.imshow("image", frame_C)
    print('a')

#####################      视频处理       #############################
num = 0    # 帧数目
lowThreshold = 0
min_lowThreshold = 0
max_lowThreshold = 200

# 创建可调节画布
cv2.namedWindow('image',0)
cv2.resizeWindow("image",video_width,video_height)
# 创建滑动条
cv2.createTrackbar('low Threshold', 'image',min_lowThreshold, max_lowThreshold, update_lowThreshold)
cv2.setTrackbarPos('Alpha', 'image', 30)

while cap.isOpened():  # 视频文件已经打开
    # get a frame
    rval, frame = cap.read()

    # save a frame
    if rval == True:
        # Start time
        start = time.time()
        # End time
        end = time.time()

        # Time elapsed
        seconds = end - start + 0.0001
        print("Time taken : {0} seconds".format(seconds))
        # Calculate frames per second
        fps = 1 / seconds
        print("Estimated frames per second : {0}".format(fps))

        frame_C = frame
        frame_C = img_Canny(frame_C, lowThreshold)
        print(frame_C.shape)
        out.write(frame_C)# 写如入视频帧
        num = num + 1
        print(num)

    else:
        break
    # show a frame
    cv2.imshow("image", frame_C)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
    '''
    ord('q')：返回q对应的Unicode码对应的值，q对应的Unicode数值为113。
    cv2.waitKey(1)：返回与按下键值对应的32位整数。
    0xFF：0xFF是一个位掩码，它将左边的24位设置为0。因为ord()在0和255之间返回一个值，因为您的键盘只有一个有限的字符集。
    因此，一旦应用了掩码，就可以检查它是否是相应的键。
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):   # 键入Q直接关闭
        break

#####################      释放资源       #############################
cap.release()
out.release()
cv2.destroyAllWindows()

