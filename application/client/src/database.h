#ifndef DATABASE_H
#define DATABASE_H

#endif // DATABASE_H

class Database{
private:
    string host,
    db_name, username,
    password;
public:
    Database(){}
    ~Database(){}
    bool search(string);
    bool execQuery(string);
    bool save(string);
    bool sendAc(string, string);
    bool findUser(string);
    bool addUser(string);
    //getPoints(string): array of Point;
};
