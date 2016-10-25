#ifndef REEXCEPTION_H
#define REEXCEPTION_H
#include "QString"

/*!
   \class REexception (RecycleEasilyException)
   \brief Класс, оргранизующий собственные исключения.

   \reentrant
    Данный класс нужен, что бы можно было удобно выводить пользователю
    сообщения об ошибках, логгировать возникающие ошибки, повысить
    отказоустойчивость приложения.
    В идеале надо класифицировать ошибки, а пока классицикации нет, можно
    просто инкрементировать коды ошибок.

    Пример использования класса.
    При попытке загрузить описание объекта утилизации в методе
    "Trash::getDescription()" возникает ошибка соединения:
    try {
        ...
        DB.connect();
        ...
    } catch {
        REexception.throwByCode(REexception::NO_CONNECTION);
    }
    Далее в конроллере мы перехватываем эту ошибку:
    try {
        ...
        Trash.getDescription();
        ...
    } catch (int e) {
        if (e == REexception::NO_CONNECTION) {
            //вывод пользователю сообщения об отсутствии соединения
        }
    }
 */
class REexception
{
public:

    static const int UNDEFINED_ERR = 000001; //неизвестная ошибка
    static const int NO_CONNECTION = 000002; //отсутствие соединения


    // конструктор
    REexception();

    // выкидывает исключение с соответсвующим кодом. e - код ошибки
    // в перспективе будет логировать выброшенные исключения
    void throwByCode(int e) {
        throw e;
    }

    // возвращает пользовательское описание ошибки. е - код ошибки
    QString getUserDescription(int e);

};

#endif // REEXCEPTION_H
