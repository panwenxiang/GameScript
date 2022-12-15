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
wait_time9 = 5

if handle:
    defAll.temporarily_part(handle)  # 暂离，然后回迷宫
    defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
    defAll.click_match_img_url(handle, 'img/system/system-set-net.png', 1, 1)  # 点设置断网软件
    defAll.close_net(handle)  # 判断是否为断网状态，不是则断网
    defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
    defAll.click_match_img_url(handle, 'img/system/system-game.png', 2, 1)  # 点游戏
    defAll.click_match_img_url(handle, 'img/system/down-stair.png', wait_time9, 2)  # 点下楼

    defAll.click_imitate(handle, 480, 950, wait_time5)  # 点击右下角魔法书
    defAll.click_imitate(handle, 500, 450, wait_time1)  # 点击土系
    defAll.click_imitate(handle, 340, 380, wait_time1)  # 点击地震术
    defAll.click_imitate(handle, 340, 380, 2)  # 点击使用地震术

    defAll.click_match_img_url(handle, 'img/system/armor.png', 1)  # 寻找铠甲
    defAll.click_match_img_url(handle, 'img/system/up-armor.png', 1)  # 穿上铠甲
    defAll.click_match_img_url(handle, 'img/system/skill.png', 1)  # 寻找铠甲技能
    defAll.click_match_img_url(handle, 'img/system/armor_skill.png', 1)  # 选择铠甲4技能
    defAll.click_match_img_url(handle, 'img/system/skill4.png', 1)  # 使用铠甲4技能
    defAll.click_match_img_url(handle, 'img/system/tansuo.png', 0.5)  # 为防止怪不死，捡四个东西
    defAll.click_match_img_url(handle, 'img/system/gold.png', 0.5)  # 为防止怪不死，捡四个东西
    defAll.click_match_img_url(handle, 'img/system/hp.png', 0.5)  # 为防止怪不死，捡四个东西
    defAll.click_match_img_url(handle, 'img/system/mp.png', 0.5)  # 为防止怪不死，捡四个东西
    defAll.click_match_img_url(handle, 'img/system/treasure.png', 0.5)  # 捡起宝箱
    defAll.click_match_img_url(handle, 'img/system/treasure1.png', 0.5)  # 捡起宝箱




else:
    print('找不到句柄')
    exit()