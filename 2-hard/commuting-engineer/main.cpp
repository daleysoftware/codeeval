#include <iostream>
#include <algorithm>
#include <fstream>
#include <limits>
#include <map>
#include <vector>
#include <math.h>

class Point
{
    private:
        const unsigned int _index;
        const double _lat;
        const double _lon;

    public:
        Point(const unsigned int index, const double lat, const double lon) :
            _index(index), _lat(lat), _lon(lon)
        {
            // no-op
        }

        double distanceTo(const Point& p) const
        {
            const double R = 6371;
            double diffLat = (p._lat-_lat) * M_PI/180;
            double diffLon = (p._lon-_lon) * M_PI/180;
            double lat1 = _lat * M_PI/180;
            double lat2 = p._lat * M_PI/180;
            double a = sin(diffLat/2) * sin(diffLat/2) +
                       sin(diffLon/2) * sin(diffLon/2) * cos(lat1) * cos(lat2);
            double c = 2 * atan2(sqrt(a), sqrt(1-a));
            return  R * c;
        }
};

class RouteAndDistance
{
    public:
        std::vector<int> route;
        double distance;

        RouteAndDistance() : distance(std::numeric_limits<double>::infinity())
        {
            // no-op
        }
};

double computeDistance(std::map<int, Point*>& map, std::vector<int>& route, int startingPoint)
{
    double distance = 0.0;
    Point* previous = map[startingPoint];

    for (int i : route) {
        Point* current = map[i];
        distance += current->distanceTo(*previous);
        previous = current;
    }

    return distance;
}

void findBestRoute(RouteAndDistance& result, std::vector<int>& prefix, std::map<int, Point*>& map,
        std::vector<int>& points, int startingPoint)
{
    if (prefix.size() == points.size()) {
        double distance = computeDistance(map, prefix, startingPoint);

        if (distance < result.distance) {
            result.distance = distance;

            result.route.clear();
            for (int i : prefix) {
                result.route.push_back(i);
            }
        }
    }


    for (int i : points) {
        // XXX in addition to the parsing this is the other part of this solution I dislike.
        // We could potentially replace the points vector with a set to avoid this linear search.
        if (std::find(prefix.begin(), prefix.end(), i) == prefix.end()) {
            prefix.push_back(i);
            findBestRoute(result, prefix, map, points, startingPoint);
            prefix.pop_back();
        }
    }
}

RouteAndDistance* findBestRoute(std::map<int, Point*>& map, std::vector<int>& points,
        int startingPoint)
{
    RouteAndDistance* best = new RouteAndDistance();
    std::vector<int> prefix;

    findBestRoute(*best, prefix, map, points, startingPoint);
    return best;
}

int main(int argc, char** argv)
{
    std::ifstream file(argv[1]);

    std::map<int, Point*> map;
    std::vector<int> points;

    std::string line;
    while (std::getline(file, line))
    {
        // XXX My C++ parsing is terrible, but it works.
        int index = atoi(line.substr(0, line.find(' ')).c_str());
        line = line.substr(line.find('(')+1, line.find(')')-1);
        double lat = std::stod(line.substr(0, line.find(',')-1));
        double lon = std::stod(line.substr(line.find(',')+2));

        // Add this point to our point map.
        map[index] = new Point(index, lat, lon);
        if (index != 1) {
            points.push_back(index);
        }
    }

    RouteAndDistance* result = findBestRoute(map, points, 1);

    std::cout << 1 << std::endl;
    for (int i : result->route) {
        std::cout << i << std::endl;
    }
}
