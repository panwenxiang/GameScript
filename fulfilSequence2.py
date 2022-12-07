import cv2
import defAll
import copy

# 填入测序数组，模板： sq_list = [1, 2, 8, 33]
sq_list_no_change = {
    '1': [10, 15],
    '2': [4, 10]
}
template_address = "img/template/3level/"
# 输入窗口名
handle = defAll.get_handle('大号')
# 输入你要推序循环101的次数
cycles = 1
# 输入你要选择的魔法:1-治疗术，2-元素球
magic_type = 2


print('句柄', handle)

# 星级装备的地址字典
level_address = defAll.level_fulfil_address
npc_xy = {'x': 0, 'y': 0}
furnace_xy = {'x': 0, 'y': 0}
wait_time = 0.4
after_level = False


def attack():
    defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)


def magic():
    if magic_type == 1:
        defAll.click_imitate(handle, 480, 950, wait_time)  # 点击右下角魔法书
        defAll.click_imitate(handle, 480, 360, 0.1)  # 点击水系
        defAll.click_imitate(handle, 140, 360, 0.1)  # 点击治疗
        defAll.click_imitate(handle, 140, 360, 0.1)  # 点击使用治疗
    if magic_type == 2:
        defAll.click_imitate(handle, 480, 950, 1)  # 点击右下角魔法书
        defAll.click_imitate(handle, 360, 800, 0.1)  # 点击特殊
        defAll.click_imitate(handle, 500, 360, 0.1)  # 点击中间黄星星
        defAll.click_imitate(handle, 130, 380, 0.1)  # 点击火元素球
        defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)  # 点击NPC


def fuse(fuse_level):
    global after_level
    defAll.click_imitate(handle, furnace_xy['x'], furnace_xy['y'], 0.1)  # 点熔炉
    defAll.click_imitate(handle, 357, 488, wait_time)  # 点击 加
    if fuse_level != after_level:
        # 第一次进入，打开列表后先回到第一页
        first = False
        for _ in range(10):
            defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页
    match_result = defAll.template_all_search(handle, level_address[str(fuse_level)])
    if match_result['is_found']:
        defAll.click_imitate(handle, match_result['center_x'], match_result['center_y'] + defAll.margin_top, wait_time)
        defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 选择按钮
        defAll.click_imitate(handle, 277, 684, 0.1)  # 点击 熔炼装备
        defAll.click_imitate(handle, 480, 950, 0.1)  # 点击返回
    after_level = fuse_level


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
    print(11, sq_list_no_change)
    for i in range(0, cycles):

        sq_list = copy.deepcopy(sq_list_no_change)
        print(i + 1, '次循环，初始拿到的字典', sq_list)

        number = 1
        while number <= 101:
            count = 2
            # 如果是最后一次，执行法术
            if number == 101:
                count = 1

            level = False
            t_list = [102]  # 离下一个出的最小距离的字典的数组的浅拷贝
            for li in sq_list:
                if len(sq_list[li]) >= 1 and sq_list[li][0] < t_list[0]:
                    t_list = sq_list[li]
                    level = li
                    # 都没有时为空
            print('匹配得到字典中的哪一项数组：', t_list, '星级：', level)
            if t_list[0] == 102:
                del (t_list[0])

            if len(t_list) >= 1:
                count = t_list[0] - number

            if count >= 2:
                print(number, '次，下一次熔炼：', t_list[0] if len(t_list) else '数组空了', '执行攻击+2次')
                attack()
                number += 2
            elif count == 1:
                print(number, '次，下一次熔炼：', t_list[0] if len(t_list) else '数组空了', '执行法术+1次')
                magic()
                number += 1
            elif count == 0:
                print(number, '次，下一次熔炼：', t_list[0] if len(t_list) else '数组空了', '****熔炼+1次')
                fuse(level)
                number += 1
                ran = t_list[0]
                for elem in sq_list:
                    if len(sq_list[elem]) >= 1 and ran == sq_list[elem][0]:
                        del (sq_list[elem][0])
            print('101循环执行1次后的字典：', sq_list)


else:
    print('找不到句柄')
