//
//  classUser.h
//  RecycleEasily
//
//  Created by Tim on 24.10.16.
//  Copyright (c) 2016 Tim. All rights reserved.
//

#ifndef RecycleEasily_classUser_h
#define RecycleEasily_classUser_h

#include <iostream>
#include <time.h>

using namespace std;

class User{
private:
    string name;        //логин
    string password;    //пароль
    string email;       //адрес элктронной почты
    string vk_url;      //ссылка вконтакте
    int points;         //баллы за утилизацию
    long int CheckInTime;      //время последнего чек-ина
    
    //добавляет очуи за утилизацию
    void AddPoints(int pnts) {
        points += pnts;
    }
    void SetEmail(string mail) {
        email = mail;
    }
    void SetName(string username) {
        name = username;
    }
    void SetVkUrl(string link) {
        vk_url = link;
    }
    void SetCheckInTime(long int t) {
        CheckInTime = t;
    }
public:
    User() {
        name = "";
        password = "";
        email = "";
        vk_url = "";
        points = 0;
        CheckInTime = 0;
    }
    void SetPassword(string psswrd) {
        password = psswrd;
    }
    string GetEmail() {
        return email;
    }
    string GetName() {
        return name;
    }
    string GetVkUrl() {
        return vk_url;
    }
    int GetPoints() {
        return points;
    }
    long int GetCheckInTime() {
        return CheckInTime;
    }
    bool IsPasswordTrue(string psswrd) {
        return psswrd == password;
    }
    //создание нового пользователя
    bool CreateUser(string username, string mail, string link, string psswrd) {
        if (("" == username) && ("" == mail) && ("" == link))
            return false;
        if ("" == password)
            return false;
        if ("" != username)
            SetName(username);
        if ("" != mail)
            SetEmail(mail);
        if ("" != link)
            SetVkUrl(link);
        SetPassword(password);
        return true;
    }
    //проверка времени
    bool TimeVerification(long int t) {
        return (difftime(t, GetCheckInTime()) >= 600);
    }
    //чек-ин
    bool CheckIn(int x, int y, int pnts) {
        //добавить проверку координат
        if (TimeVerification(time(0)))
        {
            AddPoints(pnts);
            SetCheckInTime(time(0));
            return true;
        }
        else
            return false;
    }
    ~User() {
        
    }
};


#endif
