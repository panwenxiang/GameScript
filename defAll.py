import cv2
import win32gui
from PyQt5.QtWidgets import QApplication
import sys
import qimage2ndarray


# 查找窗口方法
def get_window(name):
    # 通过名字或类名获取窗口句柄
    handle = win32gui.FindWindow(0, name) | win32gui.FindWindow(name, None)
    if handle == 0:
        return None
    else:
        # 返回句柄handle
        return handle


# handle-句柄
# 获取截图并转灰
def get_screenshot(handle):
    if handle:
        # 窗口放到最上层
        # win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 1200, 800, win32con.SWP_SHOWWINDOW)

        # Qt5截图
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(handle).toImage()

        # Qimage转ndarray(我日泥马的格式转化方法搞了我半天)
        imgz = qimage2ndarray.rgb_view(img)

        imgz = cv2.cvtColor(imgz, cv2.COLOR_BGR2RGB)  # BGR转RGB
        imgz = cv2.cvtColor(imgz, cv2.COLOR_BGR2GRAY)  # BGR转灰度
        return imgz

    # 窗口放到最上层
    # win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 1200, 800, win32con.SWP_SHOWWINDOW)
    # 获取坐标
    # (x1, y1, x2, y2) = win32gui.GetWindowRect(handle)
