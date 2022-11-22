import os
import cv2
import win32gui, win32con, win32api
from PyQt5.QtWidgets import QApplication
import sys
import numpy as np

import qimage2ndarray


def get_window(name):
    handle = win32gui.FindWindow(0, name) | win32gui.FindWindow(name, None)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回句柄handle
        return handle


handle = get_window('企业微信')
print('获取的句柄:', handle, hex(eval(str(handle))))

if handle:
    # 窗口放到最上层
    # win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 1200, 800, win32con.SWP_SHOWWINDOW)

    # Qt5截图
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(handle).toImage()

    # Qimage转ndarray(我日泥马的格式转化搞了我半天才找到方法)
    imgz = qimage2ndarray.rgb_view(img)

    imgz = cv2.cvtColor(imgz, cv2.COLOR_BGR2RGB)  # BGR转RGB
    imgz = cv2.cvtColor(imgz, cv2.COLOR_BGR2GRAY)  # BGR转灰度
    cv2.imshow('2222', imgz)



    #
    # imgW=cv2.imread(img)
    # cv2.imshow('截图', imgW)
    # img.save("C:/Users/66/Desktop/screenshot2.jpg")
    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    # 获取坐标
    (x1, y1, x2, y2) = win32gui.GetWindowRect(handle)
    print('坐标:', x1, y1, x2, y2)

    cv2.waitKey()
