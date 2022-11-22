import cv2
import win32con
import defAll

handle = defAll.get_handle('夜神模拟器-小号')
# handle = defAll.get_handle('文件传输助手')

if handle:
    print('获取的句柄:', handle, hex(eval(str(handle))))
    # defAll.set_window(handle, win32con.SWP_SHOWWINDOW)
    img_z = defAll.get_screenshot(handle)

    cv2.imshow('2222', img_z)
    cv2.waitKey()

