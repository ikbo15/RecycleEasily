#-------------------------------------------------
#
# Project created by QtCreator 2016-11-07T11:29:00
#
#-------------------------------------------------

QT       += core gui webenginecore webenginewidgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = api
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    vkapiwin.cpp

HEADERS  +=main.cpp\
    mainwindow.h \
    vkapiwin.h

FORMS    += mainwindow.ui \
    vkapiwin.ui
