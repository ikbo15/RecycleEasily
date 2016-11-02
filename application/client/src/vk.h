#ifndef VK_H
#define VK_H

#endif // VK_H

class VK{
private:
    string user_id;
public:
    int setUserID(string);
    string getUserID();
    bool syncUserData();
    string getUserData(int);
    string getDataFromWeb();
    bool createRequest(string, string, string);
};
