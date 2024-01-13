'''
    Node.py主要是描述对象Node
'''
class Node(object):
    '''
        初始化节点信息
    '''
    def __init__(self,x,y,g,h,father):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.father = father
    '''
        处理边界和障碍点
    '''
    def getNeighbor(self,mapdata,endx,endy):
        x = self.x
        y = self.y
        result = []
    #先判断是否在上下边界
    #if(x!=0 or x!=len(mapdata)-1):
    #上
    #Node(x,y,g,h,father)
        if(x!=0 and mapdata[x-1][y]!=0):
            upNode = Node(x-1,y,self.g+10,(abs(x-1-endx)+abs(y-endy))*10,self)
            result.append(upNode)
    #下
        if(x!=len(mapdata)-1 and mapdata[x+1][y]!=0):
            downNode = Node(x+1,y,self.g+10,(abs(x+1-endx)+abs(y-endy))*10,self)
            result.append(downNode)
    #左
        if(y!=0 and mapdata[x][y-1]!=0):
            leftNode = Node(x,y-1,self.g+10,(abs(x-endx)+abs(y-1-endy))*10,self)
            result.append(leftNode)
    #右
        if(y!=len(mapdata[0])-1 and mapdata[x][y+1]!=0):
            rightNode = Node(x,y+1,self.g+10,(abs(x-endx)+abs(y+1-endy))*10,self)
            result.append(rightNode)
    #西北  14
        if(x!=0 and y!=0 and mapdata[x-1][y-1]!=0 ):
            wnNode = Node(x-1,y-1,self.g+14,(abs(x-1-endx)+abs(y-1-endy))*10,self)
            result.append(wnNode)
    #东北
        if(x!=0 and y!=len(mapdata[0])-1 and mapdata[x-1][y+1]!=0 ):
            enNode = Node(x-1,y+1,self.g+14,(abs(x-1-endx)+abs(y+1-endy))*10,self)
            result.append(enNode)
    #西南
        if(x!=len(mapdata)-1 and y!=0 and mapdata[x+1][y-1]!=0 ):
            wsNode = Node(x+1,y-1,self.g+14,(abs(x+1-endx)+abs(y-1-endy))*10,self)
            result.append(wsNode)
    #东南
        if(x!=len(mapdata)-1 and y!=len(mapdata[0])-1 and mapdata[x+1][y+1]!=0 ):
            esNode = Node(x+1,y+1,self.g+14,(abs(x+1-endx)+abs(y+1-endy))*10,self)
            result.append(esNode)
        # #如果节点在关闭节点 则不进行处理
        # finaResult = []
        # for i in result:
        #     if(i not in lockList):
        #         finaResult.append(i)
        # result = finaResult
        return result
    def hasNode(self,worklist):
        for i in worklist:
            if(i.x==self.x and i.y ==self.y):
                return True
        return False
    #在存在的前提下
    def changeG(self,worklist):
        for i in worklist:
            if(i.x==self.x and i.y ==self.y):
                if(i.g>self.g):
                    i.g = self.g