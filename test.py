import copy
import os
import time

import cv2
import win32con, win32api
import defAll
from datetime import datetime

wait_time1 = 0.1
wait_time3 = 0.3
wait_time5 = 0.5
# a = {'5': [4, 7, 19, 35, 45, 53, 58], '6': [65, 66, 74, 92, 97, 4, 7, 12, 19, 35, 45, 53, 58]}
b = [1, 2, 3]
# if 6 in b or 2 in b:
#     print(888)
# else:
#     print(444)

# hd = defAll.get_handle('大号')
# defAll.close_net(hd)

# 图片对比测试
# hd = defAll.get_handle('大号')
# level = '4'
# address = defAll.level_test_address[level]
# address = 'img/system/'
# # address = 'img/need_click_goods/box/'
# # address = 'img/template/test/5level/'
# for url in os.listdir(address):
#     template = cv2.imread(address + url)
#     screenshot = defAll.get_screenshot(hd)
#     # screenshot = screenshot[480:800, 0:596]
#     match = defAll.match_template(screenshot, template)
#     print(match, '*********图片名：', url)



# if match['max_val'] > 90:
#     cv2.rectangle(screenshot, (match['center_x'], match['center_y']), (match['center_x'], match['center_y']), (0, 255, 0), 5)
#     cv2.imshow('awd', screenshot)
#     cv2.waitKey()


sq_list_first = [1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 16, 18, 19, 21, 24, 25, 27, 31, 32, 34, 36, 37, 38, 39, 42, 43,
                 47, 52, 57, 59, 60, 61, 64, 67, 69, 71, 72, 76, 78, 80, 81, 82, 89, 91, 94, 95, 96, 98, 99, 100]

# 位置测试截图
# handle = defAll.get_handle('大号')
# bottom_img = defAll.get_screenshot(handle)
# # bottom_img = bottom_img[940:1020, 0:400]
# defAll.test_lcation(handle, 220, 600)
# test_list = {
#     '2': [1, 2, 3, 4]
# }
# for i in test_list:
#     test_list[i] = sorted(test_list[i])
# print('星测序完成，字典：', test_list, '共有', len(test_list[i]), '个日光')
#
# defAll.play_sound()
# time.sleep(0.3)
# print('停了')
# exit()
# # cv2.imshow('12', bottom_img)
# defAll.loop_match_img_url(handle, 'img/system/ok.png')

# handle = defAll.get_handle('大号')
#
# defAll.click_match_img_url(handle, 'img/system/magic-book.png', wait_time5, 'no-stop', 0.2)  # 点击右下角魔法书


handle = defAll.get_handle('大号')
defAll.loop_find(handle, 'img/system/startGame.png')
# defAll.click_imitate(handle, 480, 950, wait_time5)  # 点击右下角魔法书
# cv2.waitKey()
