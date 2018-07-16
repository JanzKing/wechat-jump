import matplotlib.pyplot as plt
import cv2

#实现显示图片  绘制图片等功能
class Draw:
    #构造器
    def __init__(self):

        #初始化图像plt对象
        self.fig = plt.figure()

    #显示图片
    def show_pic(self,filename,scale=1):
        #读取图像
        img=cv2.imread(filename)
        #调整显示的比例
        img=cv2.resize(img,(0,0),fx=scale,fy=scale)
        #显示图像
        plt.imshow(img)
        plt.show()
