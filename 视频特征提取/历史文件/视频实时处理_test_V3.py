import cv2
import time

import numpy as np

######################     视频载入       #############################
cap = cv2.VideoCapture("测试序列.mp4")
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
out = cv2.VideoWriter('output11.mp4', fourcc, 20, (1440, 1080))

#####################       模型载入      #############################

#####################      视频处理       #############################
num = 0
while cap.isOpened():
    # get a frame
    rval, frame = cap.read()

    # save a frame
    if rval == True:
        # Start time
        start = time.time()
        #        rclasses, rscores, rbboxes=process_image(frame) #换成自己调用的函数

        #clean_image_tensor = process_image(data_hazy)  # 换成自己调用的函数

        # End time
        end = time.time()

        # Time elapsed
        seconds = end - start + 0.0001
        print("Time taken : {0} seconds".format(seconds))
        # Calculate frames per second
        fps = 1 / seconds
        print("Estimated frames per second : {0}".format(fps))
        # bboxes_draw_on_img(frame,rclasses,rscores,rbboxes)
        # print(rclasses)
        # out.write(clean_image_tensor)
        out.write(frame)
        num = num + 1
        print(num)
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    else:
        break
    # show a frame
    cv2.namedWindow('capture',0)
    cv2.resizeWindow("capture",700,500)
    cv2.imshow("capture", frame)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
    '''
    ord('q')：返回q对应的Unicode码对应的值，q对应的Unicode数值为113。
    cv2.waitKey(1)：返回与按下键值对应的32位整数。
    0xFF：0xFF是一个位掩码，它将左边的24位设置为0。因为ord()在0和255之间返回一个值，因为您的键盘只有一个有限的字符集。
    因此，一旦应用了掩码，就可以检查它是否是相应的键。
    '''
    if cv2.waitKey(0) & 0xFF == ord('q'):   # 键入Q直接关闭
        break

cap.release()
out.release()
cv2.destroyAllWindows()
