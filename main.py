import os
import cv2
import numpy as np
import win32gui


# 模板匹配
imgBottomList = ["img/bottomImg/1.png", "img/bottomImg/2.png", "img/bottomImg/3.png", "img/bottomImg/4.png"]
imgTemplateList = ["img/template/1.png", "img/template/2.png", "img/template/3.png", "img/template/4.png",
                   "img/template/5.png", "img/template/6.png", "img/template/77.png"]

# 读取图片
imgBottom = cv2.imread(imgBottomList[1])
imgTemplate = cv2.imread(imgTemplateList[4])
imgTemplate6 = cv2.imread(imgTemplateList[5])


# 转灰度图片
imgBottomGray = cv2.cvtColor(imgBottom, cv2.COLOR_BGR2GRAY)
imgTemplateGray = cv2.cvtColor(imgTemplate, cv2.COLOR_BGR2GRAY)
imgTemplate6Gray = cv2.cvtColor(imgTemplate6, cv2.COLOR_BGR2GRAY)

# 测试缩放
# hh1, ww1 = imgTemplateGray.shape[0:2]
# bf = 0.95
# new_cat = cv2.resize(imgTemplateGray, (int(ww1 * bf), int(hh1 * bf)))
# cv2.imshow("ceshi", new_cat)

# 获取模板图片的宽高
imgH, imgW = imgTemplate.shape[0:2]


batchImportPath = "img/template/"
# batchImportPath = "img/imgTest/"
for imgName in os.listdir(batchImportPath):
    imgTemplateRead = cv2.imread(batchImportPath + imgName)  # 读
    imgTemplateReadGray = cv2.cvtColor(imgTemplateRead, cv2.COLOR_BGR2GRAY)  # 转灰度

    hh1, ww1 = imgTemplateReadGray.shape[:2]

    # scaledTemplateImg = cv2.resize(imgTemplateReadGray, (int(ww1), int(hh1)))

    # 查看缩放比例的模板测试图片
    # testImg = scaledTemplateImg
    # cv2.putText(testImg, str(sl), (20, 20), cv2.FONT_ITALIC, .6, (0, 0, 255), 2)
    # cv2.imshow(str(sl), testImg)

    # 模板匹配
    match = cv2.matchTemplate(imgBottomGray, imgTemplateReadGray, cv2.TM_CCOEFF_NORMED)
    # cv2.imshow('2', scaledTemplateImg)

    # 第一种方法minMaxLoc：只能获取match中的最大和最小值
    # minVal—矩阵中的最小值 maxVal—矩阵中的最大值 minLoc—矩阵中的最小值的坐标 maxLoc—矩阵中的最大值的坐标
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
    print(imgName, '  最高匹配度', max_val)
    if max_val > 0.9:
        # 匹配度小数转成百分比
        matchPercent = "%.1f%%" % (max_val * 100)
        # 画方框，图片/初始坐标/结束坐标/rgb/粗细
        cv2.rectangle(imgBottom, max_loc, (max_loc[0] + ww1, max_loc[1] + hh1), (0, 255, 0), 2)
        cv2.putText(imgBottom, str(matchPercent), max_loc, cv2.FONT_ITALIC, .6, (0, 0, 255), 2)
        # break

# match = cv2.matchTemplate(img1Gray, imgTemplateGray, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
# matchPercent = "%.2f%%" % (max_val * 100)  # 匹配度小数转成百分比
# cv2.rectangle(img1, max_loc, (max_loc[0]+imgW, max_loc[1]+imgH), (0, 255, 0), 2)  # 画方框，图片/初始坐标/结束坐标/rgb/粗细
# cv2.putText(img1, str(matchPercent), max_loc, cv2.FONT_ITALIC, .6, (0, 0, 255), 2)

#     第二种方法zip：获取match中匹配度大于某值的点，循环画出所有的框
#     locations = np.where(match >= 0.8)
#     for p in zip(*locations[::-1]):
#         x1, y1 = p[0], p[1]
#         print(3333333, x1, y1)
#         x2, y2 = x1 + ww1, y1 + hh1
#         cv2.rectangle(imgBottom, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imshow("模板", imgTemplateGray)
cv2.imshow("匹配底图", imgBottom)

# print(666888888888, locations)

cv2.waitKey(0)
