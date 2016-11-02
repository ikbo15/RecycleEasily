#ifndef MAP_H
#define MAP_H

#endif // MAP_H

struct Coordinates{
    double x, y;
};

class Map{
private:
    Coordinates user_location;
    double zoom;
    //point_list: array of Points
public:
    void findUser();
    void showPoints();
    void expand();
};
