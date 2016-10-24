//
//  classPoint.h
//  RecycleEasily
//
//  Created by Tim on 24.10.16.
//  Copyright (c) 2016 Tim. All rights reserved.
//

#ifndef RecycleEasily_classPoint_h
#define RecycleEasily_classPoint_h

#include <iostream>

using namespace std;

class Point{
private:
    string name;
    string adress;
    string description;
    string url;
    string type;
    int weight;
public:
    Point() {
        name = "";
        adress = "";
        description = "";
        url = "";
        type = "";
        weight = 0;
    }
    void SetName(string pointname) {
        name = pointname;
    }
    void SetAdress(string adr) {
        adress = adr;
    }
    void SetDescription(string dscrptn) {
        description = dscrptn;
    }
    void SetUrl(string link) {
        url = link;
    }
    void SetWeight(int w) {
        weight = w;
    }
    void SetType(string t) {
        type = t;
    }
    string GetName() {
        return name;
    }
    string GetAdress() {
        return adress;
    }
    string GetDescriptio() {
        return description;
    }
    string GetUrl() {
        return url;
    }
    int GetWeight() {
        return weight;
    }
    string GetType() {
        return type;
    }
    ~Point() {
        
    }
};

#endif
