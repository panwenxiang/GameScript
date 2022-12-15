import time

import cv2
import defAll
import copy

# 请确保设置和游戏在桌面

# 输入窗口名
handle = defAll.get_handle('大号')
wait_time1 = 0.1
wait_time3 = 0.3
wait_time5 = 0.5

if handle:
    defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
    defAll.click_match_img_url(handle, 'img/system/system-set.png', wait_time3, 1)  # 点设置
    defAll.click_match_img_url(handle, 'img/system/system-wifi.png', wait_time3)  # 点wifi
    defAll.click_match_img_url(handle, 'img/system/system-wifi-click-close.png', wait_time3)  # 点关闭wifi
    defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
    defAll.click_match_img_url(handle, 'img/system/system-game.png', wait_time3, 1)  # 点游戏
    defAll.click_match_img_url(handle, 'img/system/down-stair.png', wait_time3, 1)  # 点下楼

    defAll.click_imitate(handle, 480, 950, wait_time5)  # 点击右下角魔法书
    defAll.click_imitate(handle, 500, 450, wait_time1)  # 点击土系
    defAll.click_imitate(handle, 340, 380, wait_time1)  # 点击地震术
    defAll.click_imitate(handle, 340, 380, 3)  # 点击使用地震术
else:
    print('找不到句柄')
    exit()