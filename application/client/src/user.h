#ifndef USER_H
#define USER_H

#endif // USER_H
#include <string>
using namespace std;

class User{
private:
    string email,
    name, password, vk_url;
public:
    void setEmail(string);
    void setName(string);
    void setPassword(string);
    void setVk_url(string);
    string getEmail();
    string getName();
    string getVk_url();
   // bool createUser();
}
