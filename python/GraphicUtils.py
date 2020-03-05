# 两个向量的向量积
# e.g. ScalarProduct((1,2),)
def ScalarProduct(vector1, vector2):
    return sum(v1*v2 for v1, v2 in zip(vector1, vector2))

# 找出一条线段中与指定点距离最短的点
# LinePoint1/LinePoint2 分别是线段的两个端点
# Point3 指定点
# 点的类型为一个二元组 (x, y) 或 三元组 (x, y, z)
# e.g. ShortestPoint((0,0), (3,0),(2,5)) => (2.0, 0.0)
# ShortestPoint((0,0,0), (6,6,6), (2,5,7)) => (4.67, 4.67, 4.67)
def ShortestPoint(LinePoint1, LinePoint2, Point3):
    if LinePoint1==LinePoint2:
        return LinePoint1
    vector21 = tuple(v1-v2 for v1, v2 in zip(LinePoint1, LinePoint2))
    vector23 = tuple(v3-v2 for v3, v2 in zip(Point3, LinePoint2))
    lamb = ScalarProduct(vector21, vector23)/ScalarProduct(vector21, vector21)
    if lamb > 1:
        return LinePoint1
    elif lamb < 0:
        return LinePoint2
    else:
        return tuple(i+lamb*j for i, j in zip(LinePoint2,vector21))

# 找出指定点到线段的最短距离
def ShortestDist(LinePoint1, LinePoint2, Point3):
    shortest_point = ShortestPoint(LinePoint1, LinePoint2, Point3)
    vec = tuple(p-p3 for p, p3 in zip(shortest_point, Point3))
    return ScalarProduct(vec, vec)**0.5

# 判断二维平面多边形是否为顺时针绘制
# 参数为一个二元组数组: [(x1,y1), (x2,y2), (x3,y3), ...]
def IsClockwise(polygon):
    if(len(polygon) < 3):
        return False
    vsum = 0
    for i in range(0, len(polygon)):
        vsum += (polygon[i][0]-polygon[i-1][0])*(polygon[i][1]+polygon[i-1][1])
    return vsum > 0
