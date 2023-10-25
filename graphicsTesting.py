from graphics import *
import time

grid_side = 50;
# create a graphics window
win = GraphWin ('Testing', 500, 500)

wallsList = [(9, 1), (10, 1), (2, 2), (4, 2), (5, 2), (7, 2), (7, 3), (9, 3),
             (3, 4), (5, 4), (7, 4), (9, 4), (3, 5), (5, 5), (7, 5), (8, 5), (9, 5), (2, 6),
             (3, 6), (5, 6), (8, 6), (2, 7), (5, 7), (6, 7), (8, 7), (10, 7), (2, 8), (6, 8), (8, 8),
             (10, 8), (4, 9), (5, 9), (6, 9), (1, 10), (2, 10)]

adjencyDict = {}
centerWall = {}
nodeVisit = [[False for i in range(11)] for j in range(11)]
nodeVisit[1][1] = True
for a in wallsList:
    pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
    pt2 = Point((a[0]) * grid_side, (a[1]) * grid_side)
    rect1 = Rectangle(pt1, pt2)
    rect1.setFill(color_rgb(0, 102, 248))
    rect1.draw(win)

startPoint = (1, 1)
circle1 = Circle (Point (((startPoint[0] - 1) * grid_side) + 25, ((startPoint[1] - 1) * grid_side) + 25), 25)
circle1.setFill ('red')
circle1.draw (win)
endPoint = (1, 4)
newEndPoint = endPoint
# create a circle object
circle = Circle (Point (((endPoint[0] - 1) * grid_side) + 25, ((endPoint[1] - 1) * grid_side) + 25), 25)
circle.setFill ('yellow')
circle.draw (win)

path = [];

def createAdjencyDict():
    for y in range(1, 11):
        for x in range(1, 11):
            point = (y, x)
            if point in wallsList:
                continue
            else:
                adjencyDict[point] = []
                if ((y - 1 != 0)):
                    if (y - 1, x) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y - 1, x))
                if ((y + 1 != 11)):
                    if (y + 1, x) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y + 1, x))
                if ((x - 1 != 0)):
                    if (y, x - 1) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y, x - 1))
                if ((x + 1 != 11)):
                    if (y, x + 1) not in wallsList:
                        currList = adjencyDict[point]
                        currList.insert(0, (y, x + 1))

def moving(key):
    if key == 'Up':
        circle.move (0, -50)
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, 50)
    elif key == 'Down':
        circle.move (0, 50)
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, -50)
    elif key == 'Left':
        circle.move (-50, 0)
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(50, 0)
    elif key == 'Right':
        circle.move (50, 0)
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(-50, 0)
    newEndPoint = ((circle.p1.x / grid_side) + 1, (circle.p1.y / grid_side) + 1)
    path.clear()
    dfs(startPoint, newEndPoint)


def dfs(node, target):
    endReached = False
    nodeVisit[node[0]][node[1]] = True
    path.insert(len(path), node)
    if node == target:
        return True
    for point in adjencyDict[node]:
        if (endReached == True):
            break
        if nodeVisit[point[0]][point[1]] == False:
            endReached = dfs(point, target)
            if not endReached:
                path.insert(len(path), node)
    return endReached

def main():
    createAdjencyDict()
    key = win.getKey()
    moving(key)


while True:
    nodeVisit = [[False for i in range(11)] for j in range(11)]
    nodeVisit[1][1] = True
    main()
    print(path, nodeVisit)




