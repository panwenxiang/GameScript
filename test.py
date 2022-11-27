import time

import cv2
import win32con, win32api
import defAll

a = {'name': 'zhangsan', 'sex': '男'}
handle = defAll.get_handle('夜神模拟器')
# handle = ''
print('拿到的handle:', handle, a['name'])

if handle:
    print('获取的句柄:', handle, hex(eval(str(handle))))
    img_b = defAll.get_screenshot(handle)
    imb_t = cv2.imread('img/system/next.png')
    a = defAll.match_template(img_b, imb_t)
    print(a)
    # x = 50
    # y = 50
    # defAll.test_lcation(handle, x, y)
    #
    # long_position = win32api.MAKELONG(x, y)  # 模拟鼠标指针 传送到指定坐标
    # # time.sleep(2)
    #
    # # 模拟鼠标按下
    # win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    # # win32api.SendMessage(hd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position)
    # win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, long_position)  # 模拟鼠标弹起

# long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起
