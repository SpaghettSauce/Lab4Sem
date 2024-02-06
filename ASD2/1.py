import math

def dist(p1,p2):
    x1,x2,y1,y2 = *p1,*p2
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)

def orientation(p1, p2, p3):
    x1,y1,x2,y2,x3,y3 = *p1,*p2,*p3
    d = (y3-y2) * (x2-x1) - (y2-y1) * (x3-x2)
    if d > 0 :
        return 1 
    elif d < 0 :
        return -1
    else:
        return 0

def gift(points):
    n = len(points)
    if n < 3:
        return []
    hull = []
    p = min(points)

    while True:
        hull.append(p)
        nextp = points[0]
        for point in points:
            o = orientation(p,nextp,point)
            if nextp == p or o == 1 or (o == 0 and dist(p,point) > dist(p,nextp)):
                nextp = point
        p = nextp
        if p == hull[0]:
            break
    return hull
    

points = [(0, 3), (2, 2), (10, 1), (2, 1), (-3, 0), (0, 0),(3,3), (3, 3)]
convex_hull_points = gift(points)
print("Точки выпуклой оболочки:", convex_hull_points)