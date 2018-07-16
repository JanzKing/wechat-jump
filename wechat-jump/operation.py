import os
import datetime
from PIL import Image
#实现控制Android
class Operation():
    #构造方法
    def __init__(self):
        pass

    #截屏
    def screen_cap(self):

       # filename=time=datetime.datetime.now().strftime("%H%M%S") + ".png"
        #截屏并保存到手机目录上
        filename = "auto.png"
        cmd="adb shell screencap -p /sdcard/" + filename
        os.system(cmd)
        #把手机目录上的文件拷贝到PC上
        cmd="adb pull /sdcard/" + filename + " img/" +filename
        os.system(cmd)
        #打开图像文件

        return Image.open("img/" + filename)

    def jump(self, src, dst, press_time):
        press_time = int(press_time)
        cmd = "adb shell input swipe %d %d %d %d %d" % (
            int(src[0]), int(src[1]),
            int(dst[0]), int(dst[1]),
            press_time
        )
        print(cmd)
        os.system(cmd)



if __name__ == "__main__":
    op = Operation()
    op.screen_cap()