import os
import cv2
import win32gui, win32con, win32api


def get_window(name):
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回句柄handle
        return handle


handle = get_window('企业微信')
print('获取的句柄:', handle)
if handle:
    # 窗口放到最上层
    win32gui.SetForegroundWindow(handle)
    win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 1200, 800, win32con.SWP_SHOWWINDOW)

    # 获取坐标
    (x1, y1, x2, y2) = win32gui.GetWindowRect(handle)
    print('坐标:', x1, y1, x2, y2)
