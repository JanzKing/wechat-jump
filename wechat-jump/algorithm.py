#算法类
import cv2
import math
class Algorithm():
    #偏移值
    piece_base_height = 10
    #构造器
    def __init__(self):
        pass

    #计算两点之间的欧式距离
    #p1和p2表示两个点 用元组来表示
    def euclidean_distance(self,p1,p2):
        return ((p1[0] -p2[0])**2+(p1[1]-p2[1])**2)**0.5

    #寻找关键坐标
    #返回值1，2 piece_x,piece_y 起跳点的坐标
    #返回值3,4 board_x,board_y 目标点的坐标
    def find_point(self,im):
        piece_x = piece_y = 0
        board_x = board_y =0

        #图像大小
        w,h = im.size
        im_pixel = im.load()
        points = []
        piece_y_max = 0
        for i in range(h // 3, h * 2 // 3):
            for j in range(w):
                pixel = im_pixel[j,i] #当前点的RGB的值
                #print(" i = ",i,"j = ",j,",pixel = ",pixel)
                if (50 < pixel[0] < 60 and 53 < pixel[1] < 63 and 95 < pixel[2] < 110):
                    points.append((j,i))
                    # 记录下y的值
                    if i > piece_y_max:
                        piece_y_max = i

        print("piece_y_max = %d" % (piece_y_max,))

        bottom_x = []
        for x,y in points:
            if y == piece_y_max:
                bottom_x.append(x)

        piece_x = sum(bottom_x) // len(bottom_x)
        print("piece_x = %d" % (piece_x))
        piece_y = piece_y_max - self.piece_base_height
        print("piece_y = %d" % (piece_y))
        points = []
        # 只取中间1/3进行扫描
        for i in range(h // 3, h * 2 // 3):
            if len(points) > 0:
                break
            # 取坐标的一个点作为背景的参照物
            last_pixel = im_pixel[0, i]
            # 逐个扫描右边的点
            for j in range(w):
                pixel = im_pixel[j, i]
                # 把当前点与最左边的点比较 如果RGB差异比较大 则认为是目标点
                if (abs(pixel[0] - last_pixel[0])
                        + abs(pixel[1] - last_pixel[1])
                        + abs(pixel[2] - last_pixel[2]) > 10):
                    points.append((j, i))

        top_x = []
        for x, y in points:
            top_x.append(x)

        board_x = sum(top_x) // len(top_x)
        print("board_x = %d" % (board_x,))

        center_x = w / 2 + 16  # x的偏差是16
        center_y = h / 2 + 14  # y的偏差是14
        # 格子高和宽的比例
        height_per_width = 175 / 301
        # 计算出目标格子的y值(需要转换成整数)

        if piece_x < board_x:
            board_y = int(center_y - height_per_width * (board_x - center_x))
        else:  # 从右往左跳
            board_y = int(center_y + height_per_width * (board_x - center_x))

        print("board_y = %d" % (board_y,))


        return piece_x,piece_y,board_x,board_y

    def distance_to_time(self, distance):
        # 当0分的时候 距离为 261.222128 时间为730
        p = 1.5  # 该算法后面待优化
        press_time = distance * p
        return press_time

