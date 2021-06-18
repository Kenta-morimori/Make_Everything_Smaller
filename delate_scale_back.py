import urllib.request, urllib.error
import os
import sys
import cv2

def delate_back(image_dir):
    if os.path.exists(image_dir):
        # 背景削除
        img = cv2.imread(image_dir)
        print(img.shape)
        b = img[:, :, 0]
        g = img[:, :, 1]
        r = img[:, :, 2]
        # a = img[:, :, 3]

        cv2.imshow("img", img)
        cv2.imshow("b", b)
        cv2.imshow("g", g)
        cv2.imshow("r", r)
        # cv2.imshow("a", a)

        # return after_image
    else:
        print("画像が存在しません．")
        sys.exit()



import platform

use_os = platform.system()
if(use_os == "Windows"):
    dir_connect = "\\"
else:
    dir_connect = "/"
parent_dir = os.getcwd()
scale_image_name = "scale2.jpeg"
scale_dir = parent_dir + dir_connect + "scale_image" + dir_connect + scale_image_name

delate_back(scale_dir)


