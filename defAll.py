import os
import sys
import time
from datetime import datetime

import cv2
import qimage2ndarray
import win32api
import win32con
import win32gui
from PyQt5.QtWidgets import QApplication

margin_top = 480  # 模板匹配截图到顶部的距离
sleep_next = 0.5

# 不同星级对应的不同模板地址
level_test_address = {
    '1': 'img/template/test/1level/',
    '2': 'img/template/test/2level/',
    '3': 'img/template/test/3level/',
    '4': 'img/template/test/4level/',
    '5': 'img/template/test/5level/',
    '6': 'img/template/test/6level/',
}
# 不同星级对应的不同模板地址
level_fulfil_address = {
    '1': 'img/template/fulfil/1level/',
    '2': 'img/template/fulfil/2level/',
    '3': 'img/template/fulfil/3level/',
    '4': 'img/template/fulfil/4level/',
    '5': 'img/template/fulfil/5level/',
    '6': 'img/template/fulfil/6level/',
}


# 查找窗口方法
def get_handle(name):
    # 通过名字或类名获取窗口句柄
    handle = win32gui.FindWindow(0, name) | win32gui.FindWindow(name, None)
    if handle == 0:
        return None
    else:
        # 返回句柄handle
        return handle


# 设置位置与z顺序
def set_window(handle, uFlags):
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, 0, 0, 596, 1020, uFlags)
    # 夜神 0, 0, 596, 1020


# handle-句柄; 获取截图，可选转灰
def get_screenshot(handle, is_gray=None):
    if handle:
        # 打开窗口，不移动，设置大小
        set_window(handle, win32con.SWP_NOMOVE)

        # Qt5截图
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(handle).toImage()

        # Qimage转ndarray(我日泥马的格式转化方法搞了我半天)
        img_z = qimage2ndarray.rgb_view(img)

        img_z = cv2.cvtColor(img_z, cv2.COLOR_BGR2RGB)  # BGR转RGB
        if is_gray:
            img_z = cv2.cvtColor(img_z, cv2.COLOR_BGR2GRAY)  # BGR转灰度
        return img_z


# 给出点击点的坐标测试截图
def test_lcation(handle, x, y):
    img = get_screenshot(handle)
    cv2.rectangle(img, (x, y), (x + 10, y + 10), (0, 255, 0), 2)
    cv2.imshow('test', img)
    cv2.waitKey(0)


# 模板匹配，找到模板return，找不到点下一页就递归调用自身匹配，当没有下一页时return
# 句柄， 模板img文件地址数组，  找不到点下一页还是上一页，1为下一页，0为上一页
def template_all_search(handle, batch_import_path_list, turn_pages=1):
    print('对照路径为：', batch_import_path_list)
    img_bottom = get_screenshot(handle)
    # h, w = imgBottom.shape[:2]
    # imgr = imgBottom[int(h*0.5):int(h*0.8), 0:int(w)]
    # 距离顶部
    img_bottom = img_bottom[margin_top:800, 0:596]
    # img_bottom_gray = cv2.cvtColor(img_bottom, cv2.COLOR_BGR2GRAY)
    # batch_import_path = "img/imgTest/"
    # batch_import_path = "img/template/"
    is_found = False  # 是否找到了模板

    all_img_url = []
    for level_file_url in batch_import_path_list:
        for img_url in os.listdir(level_file_url):
            all_img_url.append(level_file_url + img_url)

    for imgName in all_img_url:
        print('对照的图片为：', imgName)
        img_template_read = cv2.imread(imgName)  # 读
        # img_template_read = cv2.cvtColor(img_template_read, cv2.COLOR_BGR2GRAY)  # 转灰度
        #
        # hh1, ww1 = img_template_read.shape[:2]

        # 模板匹配
        match = match_template(img_bottom, img_template_read)
        # match = cv2.matchTemplate(img_bottom_gray, imgTemplateRead, cv2.TM_CCOEFF_NORMED)
        # cv2.imshow('2', scaledTemplateImg)
        print('公用所有模板匹配方法，', imgName, '最高匹配度:', match['max_val'])
        # print('  最高匹配度', int(match['max_val']))

        if match['max_val'] > 90:
            is_found = True
            # 加上截图距离top的距离margin_top
            # click_imitate(handle, match['center_x'], match['center_y'] + margin_top)
            data = {'is_found': True, 'max_val': match['max_val'], 'center_x': match['center_x'],
                    'center_y': match['center_y']}
            print('公用所有模板匹配方法，', imgName, '匹配到了模板,返回：', data)
            return data
            #     match['center_point'][0] += 50
            #     print('22222匹配度超90%：', match['center_point'])
            #     click_imitate(handle, match['center_point'])
            #     # 匹配度小数转成百分比
            #     matchPercent = "%.1f%%" % (max_val * 100)
            #     # 画方框参数:图片/初始坐标/结束坐标/rgb/粗细
            #     cv2.rectangle(img_bottom, (match['center_x'], match['center_y']), (match['center_x'], match['center_y']), (0, 255, 0), 5)
            # cv2.putText(img_bottom, str(matchPercent), max_loc, cv2.FONT_ITALIC, .6, (0, 0, 255), 2)
            # cv2.imshow('m', img_template_read)
            # cv2.imshow('66', img_bottom)
            # cv2.waitKey()
            # break

    # for循环匹配模板结束，没有找到模板点击下一页
    if not is_found:
        if turn_pages:
            img_template_read_next = cv2.imread('img/system/listNext.png')
        else:
            img_template_read_next = cv2.imread('img/system/listBack.png')
        match_next = match_template(img_bottom, img_template_read_next)
        print('翻页按钮：', turn_pages)
        if match_next['max_val'] > 90:
            print('找到了翻页按钮：', turn_pages, '，点击翻页，再次匹配模板')
            # cv2.imshow('66', img_bottom)
            # cv2.waitKey()

            # return {'is_found': True, 'max_val': match['max_val'], 'center_x': match['center_x'], 'center_y': match['center_y']}
            # 翻页后等0.5秒才翻页好
            click_imitate(handle, match_next['center_x'], match_next['center_y'] + margin_top, sleep_next)

            return template_all_search(handle, batch_import_path_list, turn_pages)
        else:
            print('没有翻页按钮了', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
            return {'is_found': False}


# 543   949  744  1183

# 公共匹配方法,返回：最匹配处概率,中心点x,y坐标
def match_template(img_bottom, img_template):
    img_bottom_gray = cv2.cvtColor(img_bottom, cv2.COLOR_BGR2GRAY)
    img_template = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
    match = cv2.matchTemplate(img_bottom_gray, img_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
    # 最高匹配值
    # max_val = "%.1f%%" % (max_val * 100)
    max_val = float("%.2f" % (max_val * 100))
    # 计算中心点
    h, w = img_template.shape[:2]
    center_x = int(max_loc[0] + w * 0.5)
    center_y = int(max_loc[1] + h * 0.5)
    # cv2.rectangle(img_bottom, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
    # cv2.rectangle(img_bottom, (center_x, center_y), (center_x, center_y), (0, 255, 0), 4)
    # cv2.putText(img_bottom, str(max_val), max_loc, cv2.FONT_ITALIC, .6, (0, 0, 255), 2)
    # cv2.imshow('44', img_bottom)
    # cv2.waitKey()
    return {'max_val': max_val, 'center_x': center_x, 'center_y': center_y}


# 给句柄、坐标，点击
def click_imitate(handle, center_x, center_y, sleep_time=0):
    # 模拟鼠标按下
    position = win32api.MAKELONG(center_x, center_y)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
    # win32api.SendMessage(hd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, position)
    time.sleep(sleep_time)


# 暂离，然后回迷宫
def temporarily_part(handle):
    click_imitate(handle, 40, 60, 0.5)  # 寻找暂离
    click_imitate(handle, 250, 960, 4)  # 点击暂离
    click_match_img_url(handle, 'img/system/ok.png', 0.1)  # 点击确定

    bottom_img = get_screenshot(handle)
    back_maze = 'img/back-maze'
    for url in os.listdir(back_maze):
        template_img = cv2.imread(back_maze + '/' + url)
        match = match_template(bottom_img, template_img)
        if match['max_val'] > 85:
            click_imitate(handle, match['center_x'], match['center_y'], 7)
            break
    # click_imitate(handle, 400, 200, 0.5)  # 回迷宫
    # click_imitate(handle, 470, 200, 0.5)  # 回迷宫


# 模板匹配文件夹中所有模板图片，给出最大匹配值与其坐标
def match_template_file(handle, file_src):
    bottom_img = get_screenshot(handle)
    match = {'max_val': 0}
    for url in os.listdir(file_src):
        template_img = cv2.imread(file_src + '/' + url)
        match_m = match_template(bottom_img, template_img)
        if match_m['max_val'] > match['max_val']:
            match = match_m
    print(file_src, '，模板匹配文件夹中所有模板图片，最大匹配度：', match)
    return match


# 断网，准备黑装备
def close_net(handle):
    is_open_vpn = False
    bottom_img = get_screenshot(handle)
    bottom_img = bottom_img[940:1020, 0:400]
    # 先判断是否已经打开VPN
    template = ['img/system/connected-1.png', 'img/system/connected-2.png']
    for template_url in template:
        template_img = cv2.imread(template_url)
        match = match_template(bottom_img, template_img)
        if match['max_val'] > 90:
            is_open_vpn = True
            print('VPN已经打开,匹配度：', match['max_val'], '图片url:', template_url)
            break
    # 如果没有打开，则去点击，打开
    if not is_open_vpn:
        print('打开了VPN')
        click_imitate(handle, 490, 950, 0.1)


# 联网，准备登号
def open_net(handle):
    is_close_vpn = False
    bottom_img = get_screenshot(handle)
    bottom_img = bottom_img[940:1020, 0:400]
    # 先判断是否已经关闭VPN
    template = ['img/system/not-connected-1.png', 'img/system/not-connected-2.png']
    for template_url in template:
        template_img = cv2.imread(template_url)
        match = match_template(bottom_img, template_img)
        if match['max_val'] > 90:
            is_close_vpn = True
            print('VPN已经关闭,匹配度：', match['max_val'], '图片url:', template_url)
            break
    # 如果没有关闭，则去点击，关闭
    if not is_close_vpn:
        print('关闭了VPN')
        click_imitate(handle, 490, 950, 0.1)

# 循环匹配模板，最长20秒，匹配到则返回
def loop_match_img_url(handle, url, loop_time=0.5):
    loop = True
    wait_time = 0
    img_template = cv2.imread(url)
    while loop:
        img_bottom = get_screenshot(handle)
        match = match_template(img_bottom, img_template)
        if match['max_val'] > 90:
            print(url, '循环匹配已找到，匹配度：', match['max_val'])
            loop = False
            return True
        else:
            print('循环匹配方法找不到', url, '继续匹配')
            time.sleep(loop_time)
            if wait_time >= 20:
                print('循环匹配方法找了20秒找不到', url)
                return False
        wait_time += loop_time



# 参数：1句柄，2template url，3匹配成功点击后等待时间，4找不到是否终止程序-'stop'终止 0不终止,
# 参数：5 间隔多少秒循环匹配一次，默认不循环，使用这个变量的前提是第4个变量不能是stop，否则会在第一次匹配不到时直接停止所有程序
# 给图片url —> 截图 —> 匹配成功则点击，匹配失败无操作
def click_match_img_url(handle, url, sleep_time=0, notIsExit=0, loop_time=False):
    loop = True
    img_template = cv2.imread(url)
    while loop_time or loop:
        img_bottom = get_screenshot(handle)
        loop = False
        match = match_template(img_bottom, img_template)
        if match['max_val'] > 90:
            print(url, '给图片url匹配，点击，匹配度：', match['max_val'])
            click_imitate(handle, match['center_x'], match['center_y'], sleep_time)
            loop_time = False
        else:
            print('没有找到：', url, '匹配度：', match['max_val'])
            if notIsExit == 'stop':
                exit()
        time.sleep(loop_time)
        print('给图片url方法，等待了', loop_time, '秒继续匹配')
# 窗口放到最上层
# win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 1200, 800, win32con.SWP_SHOWWINDOW)
# 获取坐标
# (x1, y1, x2, y2) = win32gui.GetWindowRect(handle)
# 获取坐标
# (x1, y1, x2, y2) = win32gui.GetWindowRect(handle)
# print(x1, y1, x2, y2)

# 一开始想的，启动设置一下最上层
# defAll.set_window(handle, win32con.SWP_SHOWWINDOW)
# 10进制转16进制
# hex(eval(str(handle)))
# 16进制转换10进制句柄
# hd = int('005C03A2', 16)
# 输出时间
# datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
# 储存图片
# url = 'C:/Users/j/Desktop/test/' + str(i) + item
# cv2.imwrite(url, bottom_img)
# 抛出异常
# raise NameError("count设置错误")
# 画方框参数:图片/初始坐标/结束坐标/rgb/粗细
# cv2.rectangle(img_bottom, (match['center_x'], match['center_y']), (match['center_x'], match['center_y']), (0, 255, 0), 5)
# cv2.putText(imgBottom, str(matchPercent), max_loc, cv2.FONT_ITALIC, .6, (0, 0, 255), 2)
# 全局变量在方法中使用报错的问题：global 声明一下该变量是全局变量
# global 变量名
