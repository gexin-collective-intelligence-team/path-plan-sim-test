# 姓名：jujianqiang
# 2023/12/8 11:40
from arithmetic.Astar.Node import Node
def getKeyforSort(element:Node):
    return element.g #element#不应该+element.h，否则会穿墙
def astar(workMap):
    startx,starty = workMap.startx,workMap.starty
    endx,endy = workMap.endx,workMap.endy
    startNode = Node(startx, starty, 0, 0, None)
    openList = []
    lockList = []
    lockList.append(startNode)
    currNode = startNode
    while((endx,endy) != (currNode.x,currNode.y)):
        workList = currNode.getNeighbor(workMap.data,endx,endy)
        for i in workList:
            if (i not in lockList):
                if(i.hasNode(openList)):
                    i.changeG(openList)
                else:
                    openList.append(i)
        openList.sort(key=getKeyforSort)#关键步骤
        currNode = openList.pop(0)
        lockList.append(currNode)
    result = []
    while(currNode.father!=None):
        result.append((currNode.x,currNode.y))
        currNode = currNode.father
    result.append((currNode.x,currNode.y))
    return result