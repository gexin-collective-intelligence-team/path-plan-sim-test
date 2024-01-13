# 姓名：jujianqiang
# 2023/12/8 11:39
import math
'''
    对象Map，主要有地图数据、起点和终点
'''
class Map(object):
    def __init__(self,mapdata,startx,starty,endx,endy):
        self.data = mapdata
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy