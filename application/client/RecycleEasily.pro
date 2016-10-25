TEMPLATE = app

QT += qml quick widgets

CONFIG += c++11

SOURCES += main.cpp \
    control.cpp \
    reexception.cpp \
    src/control.cpp \
    src/reexception.cpp \
    src/point.cpp \
    src/user.cpp

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)

HEADERS += \
    control.h \
    reexception.h \
    src/control.h \
    src/reexception.h \
    src/point.h \
    src/user.h

DISTFILES += \
    lib/README.md \
    src/model/README.md
