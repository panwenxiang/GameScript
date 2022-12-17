import win32api
import win32con

import defAll

# 请确保设置和游戏在桌面，确保使用雷霆账号登录时记录中只有一个账号密码

# 输入你需要的装备，[护腕,头盔,衣服,蓝球]，0是没有 需要黑，1是你的列表里已经有了不需要黑
need = [0, 0, 0, 0]

# 输入窗口名
handle = defAll.get_handle('大号')
wait_time1 = 0.1
wait_time3 = 0.3
wait_time5 = 0.5
if handle:
    for _ in range(101):
        defAll.temporarily_part(handle)  # 暂离，然后回迷宫

        defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
        defAll.click_match_img_url(handle, 'img/system/system-set-net.png', 1, 'stop')  # 点设置断网软件
        defAll.close_net(handle)  # 判断是否为断网状态，不是则断网
        defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
        defAll.click_match_img_url(handle, 'img/system/system-game.png', wait_time3, 'stop')  # 点游戏
        defAll.click_match_img_url(handle, 'img/system/down-stair.png', 1, 'no-stop', 0.3)  # 点下楼

        defAll.click_match_img_url(handle, 'img/system/magic-book.png', wait_time5, 'no-stop', 0.2)  # 点击右下角魔法书
        # defAll.click_imitate(handle, 480, 950, wait_time5)  # 点击右下角魔法书
        defAll.click_imitate(handle, 500, 450, wait_time1)  # 点击土系
        defAll.click_imitate(handle, 340, 380, wait_time1)  # 点击地震术
        defAll.click_imitate(handle, 340, 380, 0.1)  # 点击使用地震术
        #
        defAll.click_match_img_url(handle, 'img/system/armor.png', wait_time5)  # 寻找铠甲
        defAll.click_match_img_url(handle, 'img/system/up-armor.png', wait_time1)  # 穿上铠甲

        match_armor = defAll.match_template_file(handle, 'img/top-armor-icon')  # 给文件夹寻找上方盔甲图标点击
        if match_armor['max_val'] > 90:
            defAll.click_imitate(handle, match_armor['center_x'], match_armor['center_y'], wait_time5)
        defAll.click_imitate(handle, 448, 550, 0.2)  # 点击技能
        defAll.click_imitate(handle, 284, 648, 0.1)  # 点击施放技能按钮
        defAll.click_imitate(handle, 284, 648, 6)  # 点击使用技能

        match_box = defAll.match_template_file(handle, 'img/need_click_goods/box')  # 寻找宝箱点击
        print('宝箱匹配：', match_box)
        if match_box['max_val'] > 85:
            defAll.click_imitate(handle, match_box['center_x'], match_box['center_y'], wait_time5)

        defAll.click_imitate(handle, 70, 950, 0.2)  # 点击左下角打开列表

        # 先翻到最后一页
        for _ in range(10):
            defAll.click_imitate(handle, 520, 660, 0.1)  # 点击 右翻页
            turn_pages = 0
        # 开始查找没有的需要的
        need_img_file_list = []
        for index, item in enumerate(need):
            if item == 0:
                need_img_file_list.append('img/need_click_goods/need/' + str(index + 1) + '/')
        match_need = defAll.template_all_search(handle, need_img_file_list, 0)
        if match_need['is_found'] and match_need['max_val'] > 90:
            print('找到了需要的装备',)
            win32api.MessageBox(0, "**********************找到了需要的装备!********************", "提醒", win32con.MB_OK)
            break
        else:
            defAll.click_imitate(handle, 480, 950, wait_time1)  # 点击右下角返回
            defAll.click_imitate(handle, 500, 80, wait_time3)  # 点击右上角设置
            defAll.click_imitate(handle, 220, 450, wait_time5)  # 点击账号信息
            defAll.click_imitate(handle, 100, 960, 8)  # 点左下角登出
            defAll.click_imitate(handle, 580, 955, wait_time3)  # 点回到桌面
            defAll.click_match_img_url(handle, 'img/system/system-set-net.png', 1, 'stop')  # 点设置断网软件
            defAll.open_net(handle)  # 点关闭VPN
            defAll.click_imitate(handle, 580, 955, wait_time5)  # 点回到桌面
            defAll.click_match_img_url(handle, 'img/system/system-game.png', 2, 'stop')  # 寻找游戏图标打开游戏
            defAll.click_imitate(handle, 260, 630, wait_time3)  # 点中间开始游戏
            defAll.click_match_img_url(handle, 'img/system/login1.png', wait_time3, 'stop')  # 点击使用雷霆账号登录
            defAll.click_imitate(handle, 424, 495, wait_time3)  # 点选择账号小三角
            defAll.click_imitate(handle, 243, 547, wait_time1)  # 点选择账号
            defAll.click_imitate(handle, 125, 621, wait_time1)  # 点同意
            defAll.click_imitate(handle, 278, 677, wait_time3)  # 点登录
            defAll.click_match_img_url(handle, 'img/system/ok.png', wait_time5, 'no-stop', 0.2)  # 点击右下角魔法书
            defAll.click_imitate(handle, 220, 600, wait_time3)  # 点继续冒险

            find_magic = defAll.loop_match_img_url(handle, 'img/system/magic-book.png')
            if not find_magic:
                exit()


else:
    print('找不到句柄')
    exit()
