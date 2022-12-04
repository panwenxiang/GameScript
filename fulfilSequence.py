import cv2
import defAll

# 填入测序数组，模板： sq_list = [1, 2, 8, 33]
sq_list_no_change = [35, 62]
# 输入推序需要熔掉的装备的文件夹地址
template_address = "img/template/3level/"
# 输入窗口名
handle = defAll.get_handle('夜神模拟器')
print('句柄', handle)

npc_xy = {'x': 0, 'y': 0}
furnace_xy = {'x': 0, 'y': 0}
wait_time = 0.4
# hd = defAll.get_handle('夜神模拟器')
# img_bottom = defAll.get_screenshot(hd)
# cv2.imshow('11', img_bottom)
# cv2.waitKey()
first = True


def attack():
    defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)
def magic():
    defAll.click_imitate(handle, 480, 950, wait_time)  # 点击右下角魔法书
    defAll.click_imitate(handle, 480, 360, 0.1)  # 点击水系
    defAll.click_imitate(handle, 140, 360, 0.1)  # 点击治疗
    defAll.click_imitate(handle, 140, 360, 0.1)  # 点击使用治疗
def fuse():
    defAll.click_imitate(handle, furnace_xy['x'], furnace_xy['y'], 0.1)  # 点熔炉
    defAll.click_imitate(handle, 357, 488, wait_time)  # 点击 加
    global first
    if first:
        # 第一次进入，打开列表后先回到第一页
        first = False
        for _ in range(10):
            defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页
    match_result = defAll.template_all_search(handle, template_address)
    if match_result['is_found']:
        defAll.click_imitate(handle, match_result['center_x'], match_result['center_y'] + defAll.margin_top, wait_time)
        defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 选择按钮
        defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 熔炼装备
        defAll.click_imitate(handle, 480, 950, 0.1)  # 点击返回


if handle:

    # 找出铃铛或剑的坐标
    screenshot = defAll.get_screenshot(handle)
    bell1 = cv2.imread('img/system/npc-bell1.png')
    bell2 = cv2.imread('img/system/npc-bell2.png')
    sword1 = cv2.imread('img/system/npc-sword1.png')
    sword2 = cv2.imread('img/system/npc-sword2.png')
    for img_t in [bell1, bell2, sword1, sword2]:
        match_bell = defAll.match_template(screenshot, img_t)
        print('npc匹配结果：', match_bell)
        if match_bell['max_val'] > 90:
            npc_xy['x'], npc_xy['y'] = match_bell['center_x'], match_bell['center_y']
            print('设置了npc坐标：', npc_xy)
            break
    if npc_xy['x'] == 0:
        raise NameError('找不到铃铛NPC和剑NPC')

    # 找出熔炉的位置
    furnace = cv2.imread('img/system/furnace.png')
    match_furnace = defAll.match_template(screenshot, furnace)
    if match_furnace['max_val'] > 90:
        furnace_xy['x'], furnace_xy['y'] = match_furnace['center_x'], match_furnace['center_y']
    else:
        raise NameError('找不到熔炉')

    # 开始推序
    for i in range(1, 10):
        sq_list = sq_list_no_change.copy()
        number = 1
        while number <= 101:
            count = 2
            # 如果是最后一次，执行法术
            if number == 101:
                count = 1
            if len(sq_list) >= 1:
                count = sq_list[0] - number
            if count >= 2:
                print(number, '次，下一次熔炼：', sq_list[0] if len(sq_list) else '数组空了', '执行攻击+2次')
                attack()
                number += 2
            elif count == 1:
                print(number, '次，下一次熔炼：', sq_list[0] if len(sq_list) else '数组空了', '执行法术+1次')
                magic()
                number += 1
            elif count == 0:
                print(number, '次，下一次熔炼：', sq_list[0] if len(sq_list) else '数组空了', '****熔炼+1次')
                fuse()
                del (sq_list[0])
                number += 1


else:
    print('找不到句柄')
