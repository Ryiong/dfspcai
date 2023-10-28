global endPoint

    if key == 'Up':
        circle.move (0, -50)
        print("Up")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, 50)

    elif key == 'Down':
        circle.move (0, 50)
        print("Down")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(0, -50)

    elif key == 'Left':
        circle.move (-50, 0)
        print("Left")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(50, 0)

    elif key == 'Right':
        circle.move (50, 0)
        print("Right")
        for a in wallsList:
            pt1 = Point((a[0] - 1) * grid_side, (a[1] - 1) * grid_side)
            pt2 = Point(a[0] * grid_side, a[1] * grid_side)
            rect1 = Rectangle(pt1, pt2)
            if circle.getCenter().x == rect1.getCenter().x and circle.getCenter().y == rect1.getCenter().y:
                circle.move(-50, 0)

    endPoint = ((circle.p1.x / grid_side) + 1, (circle.p1.y / grid_side) + 1)

    path.clear()
    dfs(startPoint, endPoint)