#include "mainwindow.h"
#include <QApplication>
#include <QtWebEngineCore>
#include <QtWebEngineWidgets>
#include <QUrl>
#include <QString>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
