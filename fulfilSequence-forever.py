import cv2
import defAll
import copy
import time

# 填入测序数组，模板： sq_list = [1, 2, 8, 33]
sq_list_no_change = [3, 10, 11]
# 输入你想要融几次淬火刻印就去淬炼刻印
fuse_count = 30

# 输入窗口名
handle = defAll.get_handle('大号')
# 输入你要推序循环101的次数
cycles = 1
# 输入要匹配的淬火刻印的图片文件夹路径
fire_url = 'img/fire/'


print('句柄', handle)
fuse_number = 0
npc_xy = {'x': 0, 'y': 0}
furnace_xy = {'x': 0, 'y': 0}
wait_time = 0.5
first = True
first_magic = True


def attack():
    defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)
def magic():
    global first_magic
    if first_magic:
        defAll.click_imitate(handle, 480, 950, 1)  # 点击右下角魔法书
        defAll.click_imitate(handle, 360, 800, 0.1)  # 点击特殊
        defAll.click_imitate(handle, 500, 360, 0.1)  # 点击中间黄星星
        defAll.click_imitate(handle, 130, 380, 0.1)  # 点击火元素球
        defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)  # 点击NPC
    else:
        defAll.click_imitate(handle, 480, 950, wait_time)  # 点击右下角魔法书
        defAll.click_imitate(handle, 130, 380, 0.1)  # 点击火元素球
        defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)  # 点击NPC
        first_magic = False
def wash():
    # 点击返回
    defAll.click_imitate(handle, 480, 950, 0.1)
    # 点击熔炉
    defAll.click_match_img_url(handle, 'img/system/wash.png', wait_time)
    # 点击洗
    defAll.click_imitate(handle, 490, 684, 0.5)



def fuse(number_f, sq_list_f):
    global fuse_number
    # 点击熔炉
    defAll.click_match_img_url(handle, 'img/system/furnace-2.png', wait_time)
    # 点击 加
    defAll.click_match_img_url(handle, 'img/system/add-forever.png', wait_time)
    # 打开列表后先回到第一页
    for _ in range(10):
        defAll.click_imitate(handle, 40, 660, 0.1)  # 点击 左翻页
    time.sleep(wait_time)

    match_result = defAll.template_all_search(handle, fire_url)
    if match_result['is_found']:
        # 找到模板，点击
        defAll.click_imitate(handle, match_result['center_x'], match_result['center_y'] + defAll.margin_top, wait_time)
        # 点击 选择按钮
        defAll.click_match_img_url(handle, 'img/system/select.png', 0.1)
        # 点击 熔炼装备
        defAll.click_imitate(handle, 277, 684, 0.1)
        number_f += 1
        del(sq_list_f[0])
        fuse_number += 1
        if fuse_number >= 30:
            wash()
        while len(sq_list) >= 1 and number_f == sq_list_f[0]:
            # 如果数组下一个又是，点击 熔炼装备
            defAll.click_imitate(handle, 277, 684, 0.1)
            number_f += 1
            del (sq_list_f[0])
            fuse_number += 1
            if fuse_number >= 30:
                wash()

        # 点击返回
        defAll.click_match_img_url(handle, 'img/system/back.png', 0.1)
        # defAll.click_imitate(handle, 480, 950, 0.1)
        return number_f


if handle:
    # 找出铃铛或剑的坐标
    screenshot = defAll.get_screenshot(handle)
    bell1 = cv2.imread('img/system/npc-bell1.png')
    bell2 = cv2.imread('img/system/npc-bell2.png')
    sword1 = cv2.imread('img/system/npc-sword1.png')
    sword2 = cv2.imread('img/system/npc-sword2.png')
    for img_t in [bell1, bell2, sword1, sword2]:
        match_npc = defAll.match_template(screenshot, img_t)
        print('npc匹配结果：', match_npc)
        if match_npc['max_val'] > 87:
            npc_xy['x'], npc_xy['y'] = match_npc['center_x'], match_npc['center_y']
            print('设置了npc坐标：', npc_xy)
            break
    if npc_xy['x'] == 0:
        raise NameError('找不到铃铛NPC和剑NPC')

        # 开始推序
    for i in range(0, cycles):

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
                number = fuse(number, sq_list)


