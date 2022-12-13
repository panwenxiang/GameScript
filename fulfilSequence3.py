import time

import cv2
import defAll
import copy

# 输入测序字典
sq_list_no_change = {
    '5': [5, 10, 15],
    '6': [2, 5, 10, 15]
}
# 输入你要填的星级装备，会去拿img/template/fulfil/星级level/ 的图片做匹配
fill_list = [1, 2]
# 输入窗口名
handle = defAll.get_handle('大号')
# 输入你要推序循环101的次数
cycles = 1

print('句柄', handle)

# 星级装备的地址字典
level_address = defAll.level_fulfil_address

wait_time = 0.4
after_level = False
after_level_list = []
turn_pages = 1
# 熔装备方法
def fuse(level_list, number):
    global after_level_list, turn_pages

    if level_list != after_level_list:
        after_level_list = level_list
        if 1 in level_list or 2 in level_list:
            for _ in range(10):
                defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页
                turn_pages = 1
        else:
            for _ in range(10):
                defAll.click_imitate(handle, 520, 660, 0.1)  # 点击 右翻页
                turn_pages = 0

    time.sleep(0.5)
    print('****************推序方法拿到的数组', level_list)
    level_file_list = []
    for level in level_list:
        level_file_list.append(defAll.level_fulfil_address[str(level)])

    match_result = defAll.template_all_search(handle, level_file_list, turn_pages)
    if match_result['is_found']:
        defAll.click_imitate(handle, match_result['center_x'], match_result['center_y'] + defAll.margin_top, wait_time)
        defAll.click_match_img_url(handle, 'img/system/select.png')  # 点击 选择按钮
        defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 熔炼装备
        defAll.click_imitate(handle, 350, 460, wait_time)  # 点加
    else:
        if str(int(level_list[0])+1) in sq_list_no_change and number in sq_list_no_change[str(int(level_list[0])+1)]:
            return fuse([int(level_list[0])+1], number)
        else:
            exit()

if handle:
    defAll.click_match_img_url(handle, 'img/system/furnace.png', wait_time)  # 点熔炉
    defAll.click_imitate(handle, 350, 460, wait_time)  # 点加
    # 开始推序
    for i in range(0, cycles):
        for number in range(1, 102):
            is_find = False
            # 判断当前步骤是否可以出日光，低星有则 break
            for level in sq_list_no_change:
                if number in sq_list_no_change[level]:
                    print(number, '次，推序高星级，', level, '星级****************************')
                    fuse([level], number)
                    is_find = True
                    break
            if not is_find:
                fuse(fill_list, number)


else:
    print('找不到句柄')
