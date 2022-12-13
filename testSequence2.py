import time
import os
import defAll
import cv2
from datetime import datetime

# 输入窗口名
handle = defAll.get_handle('大号')
# 输入你想要测的星级，例如：[1, 2, 3]，请确保文件夹里有图片
test_level = [5, 6]


# 星级装备的地址字典
level_address = defAll.level_test_address
# 公共等待时间
wait_time = 0.5
# 测试结果
test_list = {}
number = 1

if handle:
    print('已找到句柄:', handle)

    for lv in test_level:
        test_list[str(lv)] = []

    defAll.click_match_img_url(handle, 'img/system/furnace.png', wait_time)  # 寻找点击熔炉
    defAll.click_imitate(handle, 357, 488, wait_time)  # 点击 加

    for lv in test_level:

        # 打开列表后先回到第一页
        for _ in range(10):
            defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页
        time.sleep(wait_time)

        for count in range(1, 102):
            # 模板匹配
            match_result = defAll.template_all_search(handle, [level_address[str(lv)]])

            if number == 102:
                number = 1
            if match_result['is_found']:
                defAll.click_imitate(handle, match_result['center_x'], match_result['center_y'] + defAll.margin_top,
                                     wait_time)
                defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 选择按钮
                defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 熔炼装备
                defAll.click_imitate(handle, 357, 488, 0.3)  # 点击 加

                print('进入判断时间**********************')
                need_url = 'img/imgNeed/'
                # 判断天下布武，截图12张，每次间隔0.05秒
                for i in range(12):
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
                            test_list[str(lv)].append(number)
                            print(item, '******找到天下布武：', match, '当前字典：', test_list)
                            is_found = True
                            break
                        else:
                            print(item, '天下布武匹配低于80%：', match)
                            # defAll.click_match_img_url(handle, 'img/imgTest/'+item)
                    print('本次没有天下布武，截图多次匹配结束')
                    if is_found:
                        break
                    # 每次截图判断天下布武后等待0.1秒再截图
                    time.sleep(0.05)

                number += 1
                print('结束判断时间**********************')
            else:
                print(lv, '星，', number, '次，找不到模板了，本星级测序结束，当前字典：', test_list)
                break

            print(number-1, '次结束，当前字典：', test_list)

        for i in test_list:
            test_list[i] = sorted(test_list[i])
        print(lv, '星测序完成，字典：', test_list)

else:
    print('没找到句柄：', handle)

# cv2.waitKey()
