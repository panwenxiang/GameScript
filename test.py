import copy
import os
import time

import cv2
import win32con, win32api
import defAll
from datetime import datetime

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
# # address = defAll.level_test_address[level]
# address = 'img/system/'
# for url in os.listdir(address):
#     template = cv2.imread(address + url)
#     screenshot = defAll.get_screenshot(hd)
#     # screenshot = screenshot[480:800, 0:596]
#     match = defAll.match_template(screenshot, template)
#     print(url, match)

# if match['max_val'] > 90:
#     cv2.rectangle(screenshot, (match['center_x'], match['center_y']), (match['center_x'], match['center_y']), (0, 255, 0), 5)
#     cv2.imshow('awd', screenshot)
#     cv2.waitKey()


sq_list_first = [1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 16, 18, 19, 21, 24, 25, 27, 31, 32, 34, 36, 37, 38, 39, 42, 43,
                 47, 52, 57, 59, 60, 61, 64, 67, 69, 71, 72, 76, 78, 80, 81, 82, 89, 91, 94, 95, 96, 98, 99, 100]

# 位置测试截图
hd = defAll.get_handle('大号')
screenshot = defAll.get_screenshot(hd)
defAll.test_lcation(hd, 470, 200)

# defAll.click_imitate(hd, 580, 955)
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

cv2.waitKey()
