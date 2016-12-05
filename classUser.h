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
    long int checkInTime;      //время последнего чек-ина
    
    //добавляет очки за утилизацию
    void AddPoints(int type) {
        //to do: баллы за каждый тип мусора можно распределить по-другому
        int pointsArray[]={1,2,3,4,5,6};
        points += pointsArray[type];
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
        checkInTime = t;
    }
public:
    User() {
        name = "";
        password = "";
        email = "";
        vk_url = "";
        points = 0;
        checkInTime = 0;
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
        return checkInTime;
    }
    bool IsPasswordTrue(string psswrd) {
        return psswrd == password;
    }
    //создание нового пользователя, пароль и хотябы одно поле кроме пароля не должны быть пустыми
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
    bool TimeVerification() {
        return (difftime(time(0), GetCheckInTime()) >= 600);
    }
    //возвращает время, оставшееся до чек-ина в секундах
    int GetTimeBeforeCheckIn() {
        return 600 - difftime(time(0), GetCheckInTime());
    }
    //чек-ин
    bool CheckIn(int userX, int userY, int pointX, int pointY, int type) {
        //to do: добавить возможную погрешность в координатах
        if ((TimeVerification()) && (userX == pointX) && (userY == pointY))
        {
            AddPoints(type);
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
