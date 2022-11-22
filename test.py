import cv2
import defAll

handle = defAll.get_window('企业微信')
print('获取的句柄:', handle, hex(eval(str(handle))))

if handle:
    imgz = defAll.get_screenshot(handle)
    cv2.imshow('2222', imgz)
    cv2.waitKey()

