import os
import time

import cv2
import win32con, win32api
import defAll
from datetime import datetime

# print(1111, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# time.sleep(0.5)
# print(2222, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# img = cv2.imread('img/imgTest/1.png')
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# cv2.imwrite('C:/Users/j/Desktop/test/test1.png', img)
# cv2.imwrite('C:/Users/j/Desktop/test/test2.png', img)
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

# hd = defAll.get_handle('夜神模拟器')
# screenshot = defAll.get_screenshot(hd)
# cv2.rectangle(screenshot, (130, 310), (410, 400), (0, 255, 0), 2)
# screenshot = screenshot[310:400, 130:410]
#
# cv2.imshow('1', screenshot)

# test_list = []
# print(11, test_list)
# test_list.append(23)
# test_list.append(8)
# print(22, test_list)

a = [2, 5, 2]
print(a)
del(a[0])
raise NameError("count设置错误")
print(a)


# handle = defAll.get_handle('4截取视频.avi')
handle = ''
template_img_url = 'img/imgNeed/'

# handle = int('000A07E4', 16)
if handle:
    for i in range(6):
        bottom_img = defAll.get_screenshot(handle)
        is_found = False
        for item in os.listdir(template_img_url):
            template_img = cv2.imread(template_img_url + item)
            match = defAll.match_template(bottom_img, template_img)
            if match['max_val'] > 80:
                print(item, '******匹配成功：', match)
                is_found = True
                break
            else:
                print(item, '匹配低于80%：', match)
            # defAll.click_match_img_url(handle, 'img/imgTest/'+item)
        print('--------------------------------')
        if is_found:
            break
        time.sleep(0.1)
cv2.waitKey()
# if handle:
#     print('获取的句柄:', handle, hex(eval(str(handle))))
#     img_b = defAll.get_screenshot(handle)
#     imb_t = cv2.imread('img/system/listNext.png')
#     a = defAll.match_template(img_b, imb_t)
#     print(a)
#     # x = 50
#     # y = 50
#     # defAll.test_lcation(handle, x, y)
#     #
#     # long_position = win32api.MAKELONG(x, y)  # 模拟鼠标指针 传送到指定坐标
#     # # time.sleep(2)
#     #
#     # # 模拟鼠标按下
#     # win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
#     # # win32api.SendMessage(hd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position)
#     # win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, long_position)  # 模拟鼠标弹起


# long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起
