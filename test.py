import copy
import os
import time

import cv2
import win32con, win32api
import defAll
from datetime import datetime

def ff(aa):
    del(aa[0])

a = [2, 10, 15]
b = [4, 6, 10]
c = {
    '1': a.copy(),
    '2': b.copy()
}
d = copy.deepcopy(c)
t_list = [102]
# a=2
# s=False
#
# if a != s:
#     print(22)

# level_address = {
#     '1': 'img/template/1level',
#     '2': 'img/template/2level',
#     '3': 'img/template/3level',
#     '4': 'img/template/4level',
#     '5': 'img/template/5level',
# }
# w = {}
# e = {
#     '1':[2]
# }
# test_level = [3, 4]
# test_list = {}
# for i in test_level:
#     test_list[str(i)] = []
#
# for i in test_level:
#     test_list[str(i)].append(68)
hd = defAll.get_handle('大号')
level = '6'
address = defAll.level_address[level]
# address = 'img/imgTest/'
for url in os.listdir(address):
    template = cv2.imread(address + url)
    screenshot = defAll.get_screenshot(hd)
    screenshot = screenshot[480:800, 0:596]
    match = defAll.match_template(screenshot, template)
    print(url, match)
    # if match['max_val'] > 90:
    #     cv2.rectangle(screenshot, (match['center_x'], match['center_y']), (match['center_x'], match['center_y']), (0, 255, 0), 5)
    #     cv2.imshow('awd', screenshot)
    #     cv2.waitKey()




sq_list_first = [1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 16, 18, 19, 21, 24, 25, 27, 31, 32, 34, 36, 37, 38, 39, 42, 43, 47, 52, 57, 59, 60, 61, 64, 67, 69, 71, 72, 76, 78, 80, 81, 82, 89, 91, 94, 95, 96, 98, 99, 100]

# print(len(sq_list_first))
# print(51*10+1117)
# 51
# 1627
# hdl = defAll.get_handle('大号')
# defAll.click_imitate(hdl, 490, 684, 0.5)
# print(test_list)


# hd = defAll.get_handle('2233.avi')
# print('句柄', hd)
# screenshot = defAll.get_screenshot(hd)
# need_url = 'img/fire-need/'
# for item in os.listdir(need_url):
#     template_img = cv2.imread(need_url + item)
#     match_furnace2 = defAll.match_template(screenshot, template_img)
#     print('匹配结果：', match_furnace2, '    ', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

# hd = defAll.get_handle('大号')
# screenshot = defAll.get_screenshot(hd)
# defAll.test_lcation(hd, 300, 400)
# defAll.click_imitate(hd, 490, 684)
# defAll.click_match_img_url(hd, 'img/system/back.png')
#
# defAll.click_imitate(hd, 480, 950, 1)  # 点击右下角魔法书
# defAll.click_imitate(hd, 360, 800, 0.1)  # 点击特殊

# cv2.rectangle(screenshot, (70, 320), (480, 390), (0, 255, 0), 2)

#
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
