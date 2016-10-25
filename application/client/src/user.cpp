#include "user.h"

void User::setEmail(string temail){
    email=temail;
}
void User::setName(string tname){
    name=tname;
}
void User::setPassword(string tpassword){
    password=tpassword;
}
void User::setVk_url(string tvk_url){
    vk_url=tvk_url;
}
string User::getEmail(){
    return email;
}
string User::getName(){
    return name;
}
string User::getVk_url(){
    return vk_url;
}
/*bool User::createUser(){

}*/
