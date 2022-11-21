import os
import cv2
import win32gui
import win32con
import numpy as np


hwnd = win32gui.GetForegroundWindow()
# 将当前窗口缩放至指定位置及大小
# win32gui.MoveWindow(hwnd, 0, 0, 1440, 900, True)
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def match_windows(win_title):
    """
    查找指定窗口
    :param win_title: 窗口名称
    :return: 句柄列表
    """

    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            win_text = win32gui.GetWindowText(hwnd)
            # 模糊匹配
            if win_text.find(win_title) > -1:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)  # 列出所有顶级窗口，并传递它们的指针给callback函数
    return hwnds


def win_active(win_title):
    """
    激活指定窗口
    :param win_title: 窗口名称
    :return:
    """
    assert win_title, "win_title不能为空！"
    hwnds = match_windows(win_title)
    if hwnds:
        win32gui.ShowWindow(hwnds[0], win32con.SW_SHOWNORMAL)  # SW_SHOWNORMAL 默认大小，SW_SHOWMAXIMIZED 最大化显示
        win32gui.SetForegroundWindow(hwnds[0])
        win32gui.SetActiveWindow(hwnds[0])



# os.system('notepad')
# scale = [0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2]
# for sl in scale:
#     print(sl)

# imgBottom[:150, :50, :] = img
# cv2.imshow(imgBottom)

# train_dir = os.path.join("E:/CelebA/Img/64normal")
# img1 = cv2.imread("C:/Users/j/Desktop/img/template/1.png")
# img2 = cv2.imread("img/template/1.png")
# imgList = os.listdir("img/template")
# for file in os.listdir("img/template"):
#     filePath = "img/template/"+file
#     print(666, filePath)
#     img = cv2.imread("img/template/"+file)
#     cv2.imshow(file, img)

# cv2.imshow('名字', img1)
# print(111, imgList)
# path = "C:\Users\j\Desktop\img\template"
# for file in os.listdir("img/template"):
#     img = cv2.imread("img/template" + file)
#     print(666, img)
    # cv2.imshow(img)
# arr = np.array([1, 2, 3, 4])
# print(np.where(arr > 3, 1, 2))
#
#
# # a = np.arange(10)
# # print(888888,a)
# # print(np.where(a > 5))

cv2.waitKey()