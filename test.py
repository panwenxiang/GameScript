import copy
import os
import time

import cv2
import win32con, win32api
import defAll
from datetime import datetime

a = [2, 10, 15]
b = [4, 6, 10]
c = {
    '1': a.copy(),
    '2': b.copy()
}
d = copy.deepcopy(c)
t_list = [102]

hd = defAll.get_handle('2233.avi')
print('句柄', hd)
screenshot = defAll.get_screenshot(hd)
need_url = 'img/fire-need/'
for item in os.listdir(need_url):
    template_img = cv2.imread(need_url + item)
    match_furnace2 = defAll.match_template(screenshot, template_img)
    print('匹配结果：', match_furnace2, '    ', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

# cv2.rectangle(screenshot, (70, 320), (480, 390), (0, 255, 0), 2)
# cv2.imshow('1', screenshot)
# cv2.waitKey()
# defAll.test_lcation(hd, 277, 684)
# defAll.click_match_img_url(handle, 'img/template/3level/9.png')

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
