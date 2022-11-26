import time

import cv2
import win32con,win32api
import defAll

# handle = defAll.get_handle('夜神模拟器-小号')
handle = ''
print('拿到的handle:', handle)

if handle:
    print('获取的句柄:', handle, hex(eval(str(handle))))
    # defAll.set_window(handle, win32con.SWP_SHOWWINDOW)
    img_z = defAll.get_screenshot(handle)


    # cv2.imshow('2222', img_z)

    cv2.waitKey()

hd = int('005C03A2', 16)
print('16进制转换10进制句柄：', hd)
x = 50
y = 50
defAll.test_lcation(hd, x, y)

long_position = win32api.MAKELONG(x, y)  # 模拟鼠标指针 传送到指定坐标
# time.sleep(2)

# 模拟鼠标按下
win32api.SendMessage(hd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
# win32api.SendMessage(hd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position)
win32api.SendMessage(hd, win32con.WM_LBUTTONUP, 0, long_position)  # 模拟鼠标弹起


# long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起
