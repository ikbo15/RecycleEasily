//
//  classUser.h
//  RecycleEasily
//
//  Created by Tim on 24.10.16.
//  Copyright (c) 2016 Tim. All rights reserved.
//

#ifndef RecycleEasily_classUser_h
#define RecycleEasily_classUser_h

using namespace std;

class User{
private:
    string name;
    string password;
    string email;
    string vk_url;
public:
    User(){
        name="";
        password="";
        email="";
        vk_url="";
    }
    void SetEmail(string mail){
        email=mail;
    }
    void SetName(string username){
        name=username;
    }
    void SetVkUrl(string link){
        vk_url=link;
    }
    void SetPassword(string psswrd){
        password=psswrd;
    }
    string GetEmail(){
        return email;
    }
    string GetName(){
        return name;
    }
    string GetVkUrl(){
        return vk_url;
    }
    bool IsPasswordTrue(string psswrd){
        return psswrd==password;
    }
    bool CreateUser(string username,string mail,string link,string psswrd){
        if ((""==username)&&(""==mail)&&(""==link))
            return false;
        if (""==password)
            return false;
        if (""!=username)
            SetName(username);
        if (""!=mail)
            SetEmail(mail);
        if (""!=link)
            SetVkUrl(link);
        SetPassword(password);
        return true;
    }
    ~User(){
        
    }
};


#endif
