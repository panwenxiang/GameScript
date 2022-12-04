import time
import os
import defAll
import cv2
from datetime import datetime
wait_time = 0.5

handle = defAll.get_handle('夜神模拟器')

if handle:
    print('已找到句柄:', handle)

    test_list = []

    defAll.click_match_img_url(handle, 'img/system/furnace.png', wait_time)  # 寻找点击熔炉
    defAll.click_imitate(handle, 357, 488, wait_time)  # 点击 加

    # 打开列表后先回到第一页
    for _ in range(10):
        defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页

    time.sleep(wait_time)

    for number in range(1, 102):
        # 模板匹配
        match_result = defAll.template_all_search(handle)
        # time.sleep(2)
        if match_result['is_found']:
            defAll.click_imitate(handle, match_result['center_x'], match_result['center_y']+defAll.margin_top, wait_time)
            defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 选择按钮
            print('点击了选择按钮')
            defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 熔炼装备
            defAll.click_imitate(handle, 357, 488, 0.3)  # 点击 加

            print('进入判断时间**********************')
            need_url = 'img/imgNeed/'
            # 判断天下布武，截图6张，每次间隔0.1秒
            for i in range(6):
                is_found = False  # 是否找到了天下布武，找到停止上面这个for循环
                screenshot_img = defAll.get_screenshot(handle)
                # 获取截图后切出天下布武那一块，top:310，left:130,待会点击记得加上
                screenshot_img = screenshot_img[310:400, 130:410]
                # 每张截图匹配img/imgNeed里的所有图片，找到停止匹配，记录数组
                for item in os.listdir(need_url):
                    template_img = cv2.imread(need_url + item)
                    match = defAll.match_template(screenshot_img, template_img)
                    if match['max_val'] > 90:
                        # 找到天下布武，记入数组
                        test_list.append(number)
                        print(item, '******找到天下布武：', match)
                        print(print(test_list))
                        is_found = True
                        break
                    else:
                        print(item, '天下布武匹配低于80%：', match)
                        # defAll.click_match_img_url(handle, 'img/imgTest/'+item)
                print('本次没有天下布武，截图多次匹配结束')
                if is_found:
                    break
                # 每次截图判断天下布武后等待0.1秒再截图
                time.sleep(0.1)
            # time.sleep(0.6)
        else:
            print('找不到模板了，结束任务，测序：', test_list)
            break
        print('本次结束，当前次数:', number)

    print('循环完成，结束任务，测序：', test_list)


else:
    print('没找到句柄：', handle)

# cv2.waitKey()