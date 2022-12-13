import time
import os
import defAll
import cv2
from datetime import datetime

# 输入窗口名
handle = defAll.get_handle('大号')
# 要匹配的淬火刻印的图片文件夹路径
fire_url = 'img/fire/'

wait_time = 0.5
npc_xy = {'x': 0, 'y': 0}
furnace2_xy = {'x': 0, 'y': 0}
test_list = []

if handle:
    print('已找到句柄:', handle)

    # 点击熔炉
    defAll.click_match_img_url(handle, 'img/system/furnace-2.png', wait_time)
    # 点击 加
    defAll.click_imitate(handle, 300, 400, wait_time)
    # 打开列表后先回到第一页
    for _ in range(10):
        defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页
    time.sleep(wait_time)

    match_result = defAll.template_all_search(handle, [fire_url])
    if match_result['is_found']:
        # 找到模板，点击
        defAll.click_imitate(handle, match_result['center_x'], match_result['center_y'] + defAll.margin_top, wait_time)

        # 点击 选择按钮
        defAll.click_match_img_url(handle, 'img/system/select.png', 0.1)

        for number in range(1, 102):
            # 点击 熔炼，   神性结晶出现持续1秒，紧接奇怪的东西持续1秒
            defAll.click_imitate(handle, 277, 684, 1)

            print('进入判断时间**********************')
            need_url = 'img/fire-need/'
            # 判断奇怪的东西，截图6张，每次间隔0.1秒
            for i in range(10):
                is_found = False  # 是否找到了奇怪的东西，找到停止上面这个for循环
                screenshot_img = defAll.get_screenshot(handle)
                # 获取截图后切出奇怪的东西那一块，增加匹配效率，[y1:y2,x1:x2]
                screenshot_img = screenshot_img[320:390, 70:480]
                # 每张截图匹配Need里的所有图片，找到停止匹配，记录数组
                for item in os.listdir(need_url):
                    template_img = cv2.imread(need_url + item)
                    match_furnace2 = defAll.match_template(screenshot_img, template_img)
                    if match_furnace2['max_val'] > 90:
                        # 找到奇怪的东西，记入数组
                        test_list.append(number)
                        print(item, '*******找到奇怪的东西：', match_furnace2)
                        print('*******当前记录数组：', test_list)
                        is_found = True
                        break
                    else:
                        print(item, '奇怪的东西匹配低于80%：', match_furnace2)
                        # defAll.click_match_img_url(handle, 'img/imgTest/'+item)
                print('----------------本次没有奇怪的东西，截图多次匹配结束-------------')
                if is_found:
                    break
                # 每次截图判断天下布武后等待0.1秒再截图
                time.sleep(0.1)
            print('本次结束，当前次数：', number)
        print('任务执行完成101次，测序结果：', test_list)

    else:
        print('找不到淬火刻印，结束任务，测序：', test_list)
