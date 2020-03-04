#pragma once

#include <boost/geometry.hpp>
#include <boost/geometry/geometries/register/point.hpp>
#include <vector>

class Point{
public:
    double _x;
    double _y;
    Point(double x=0, double y=0): _x(x), _y(y) {}
};
BOOST_GEOMETRY_REGISTER_POINT_2D(Point, double, cs::cartesian, _x, _y);


