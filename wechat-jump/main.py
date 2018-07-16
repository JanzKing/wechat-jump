from PIL.Image import Image


import os
from operation import Operation
from algorithm import Algorithm
import time
import random

#测试截屏



def test_screen_cap():
    op=Operation()
    op.screen_cap()

#测试显示图片
def test_show_pic():
    draw = Draw()
    draw.show_pic("img/193924.png")

def test_euclidean_distance():
    algorithm = Algorithm()
    p1 = (337,1110)
    p2 = (790,850)
    d = algorithm.euclidean_distance(p1,p2)
    print(d)

def test_find_point():
    algorithm = Algorithm()
    im = Image.open("img/101411.png")
    start_x,start_y,end_x,end_y = algorithm.find_point(im)
    print("start_point:",start_x,start_y)
    print("end_point:", end_x, end_y)
    p1 = (start_x , start_y)
    p2 = (end_x , end_y)
    d = algorithm.euclidean_distance(p1, p2)
    print(d)

def test_jump():
    algorithm = Algorithm()
    op = Operation()
    im = op.screen_cap()
    start_x, start_y, end_x, end_y = algorithm.find_point(im)
    start_point = (start_x, start_y)
    end_point = (end_x, end_y)
    distance = algorithm.euclidean_distance(start_point,end_point)
    press_time = algorithm.distance_to_time(distance)
    print(press_time)
    #op.jump(start_point, end_point, press_time)
    cmd = "adb shell input swipe %d %d %d %d %d" % (
        100, 100,
        100, 100,
        press_time
    )
    os.system(cmd)

if __name__=="__main__":

    # os.system( cmd = "adb shell input swipe %d %d %d %d %d" % (
    #     100, 100,
    #     # 100, 100,
    #     700
    # )cmd)

    while True:
        test_jump()
        time.sleep(2)
#test_screen_cap()
#test_show_pic()
#test_euclidean_distance()
#test_find_point()
# for i in range(10):
#     test_jump()
#     j=random.uniform(0.5,1)
#     time.sleep(j)