import cv2
import defAll
import copy


# 填入测序数组，模板： sq_list = [1, 2, 8, 33]
sq_list_no_change = {
    '1': [10, 15],
    '2': [4, 10]
}
# 输入你要推序循环101的次数
cycles = 2


# 开始推序
for i in range(0, cycles):

    sq_list = copy.deepcopy(sq_list_no_change)
    print(i+1, '次循环，初始拿到的字典', sq_list)

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
            number += 2
        elif count == 1:
            print(number, '次，下一次熔炼：', t_list[0] if len(t_list) else '数组空了', '执行法术+1次')
            number += 1
        elif count == 0:
            print(number, '次，下一次熔炼：', t_list[0] if len(t_list) else '数组空了', '****熔炼+1次')
            ran = t_list[0]
            for elem in sq_list:
                if len(sq_list[elem]) >= 1 and ran == sq_list[elem][0]:
                    del (sq_list[elem][0])
        print('操作一次后：', sq_list)

