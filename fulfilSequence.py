import cv2
import defAll

# [n,n,y,n,n,n,n,y,n,n,n]
sq_list = [1, 2, 8, 10]
npc_xy = {'x': 0, 'y': 0}

# hd = defAll.get_handle('夜神模拟器')
# img_bottom = defAll.get_screenshot(hd)
# cv2.imshow('11', img_bottom)
# cv2.waitKey()


handle = defAll.get_handle('夜神模拟器')
print('句柄', handle)
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

    # 开始推序
    number = 1
    while number <= 10:
        count = 2
        # 如果是最后一次，执行法术
        if number == 10:
            count = 1
        if len(sq_list) >= 1:
            count = sq_list[0] - number
        if count >= 2:
            print(number, '次，下一次熔炼：', sq_list[0] if len(sq_list) else '数组空了', '执行攻击+2次')
            attack()
            number += 2
        elif count == 1:
            print(number, '次，下一次熔炼：', sq_list[0] if len(sq_list) else '数组空了', '执行法术+1次')
            number += 1
        elif count == 0:
            print(number, '次，下一次熔炼：', sq_list[0] if len(sq_list) else '数组空了', '****熔炼+1次')
            del (sq_list[0])
            number += 1


else:
    print('找不到句柄')


def attack():
    defAll.click_imitate(handle, npc_xy['x'], npc_xy['y'], 0.1)
