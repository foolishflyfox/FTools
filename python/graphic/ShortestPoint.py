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

