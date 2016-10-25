#ifndef POINT_H
#define POINT_H

#endif // POINT_H
#include <string>
using namespace std;

class Point{
    private:
        string name, time,
        adress, description,
        url, type;
        int weight;
        //Coordinates location;
    public:
        Point();
        void setName(string);
        void setTime(string);
        void setAdress(string);
        void setDescription(string);
        void setUrl(string);
        void setWeight(int);
        void setType(string);
        string getName();
        string getTime();
        string getAdress();
        string getDescription();
        string getUrl();
        int getWeight();
        string getType();
};
