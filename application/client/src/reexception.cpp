#include "reexception.h"


static const int REexception::UNDEFINED_ERR = 000001;
static const int REexception::NO_CONNECTION = 000002;


REexception::REexception()
{

}

QString REexception::getUserDescription(int e) {
    switch (e){
    case REexception::NO_CONNECTION:
        return "Отсутствует соединение с интернетом";
        // break;
    }
}

void REexception::throwByCode(int e) {
    throw e;
}
