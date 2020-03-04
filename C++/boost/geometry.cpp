#include <boost/geometry.hpp>
#include <boost/polygon/polygon.hpp>
#include <vector>
#include <boost/geometry/geometries/register/point.hpp>
#include "GraphicUtils.h"

using namespace std;

namespace bg = boost::geometry;

// template parameters: typename Point, bool ClockWise, bool Closed
typedef bg::model::polygon<Point, false, false> polygon_type;

int main(){
    vector<Point> points{{0,0}, {0,1}, {1,1}, {1,0}};
    polygon_type polygon;
    boost::geometry::assign_points(polygon, points);
    Point p1(0.7, 0.99), p2(0, 0.2), p3(2,2);
    // 判断点是否在多边形中
    cout << "p1" << (boost::geometry::within(p1, polygon)?"":" not") << " in polygon\n";
    cout << "p2" << (boost::geometry::within(p2, polygon)?"":" not") << " in polygon\n";
    cout << "p3" << (boost::geometry::within(p3, polygon)?"":" not") << " in polygon\n";
    
}

