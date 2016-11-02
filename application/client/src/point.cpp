#include "point.h"
#include <string>
using namespace std;

Point::Point(){
    weight=0;
}

void Point::setName(string tname){
    name=tname;
}
void Point::setTime(string ttime){
    time=ttime;
}
void Point::setAdress(string tadress){
    adress=tadress;
}
void Point::setDescription(string tdescription){
    description=tdescription;
}
void Point::setUrl(string turl){
    url=turl;
}
void Point::setWeight(int tweight){
    weight=tweight;
}
void Point::setType(string ttype){
    type=ttype;
}
string Point::getName(){
    return name;
}
string Point::getTime(){
    return time;
}
string Point::getAdress(){
    return adress;
}
string Point::getDescription(){
    return description;
}
string Point::getUrl(){
    return url;
}
int Point::getWeight(){
    return weight;
}
string Point::getType(){
    return type;
}
