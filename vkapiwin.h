#ifndef VKAPIWIN_H
#define VKAPIWIN_H

#include <QWidget>

namespace Ui {
class vkapiwin;
}

class vkapiwin : public QWidget
{
    Q_OBJECT

public:
    QString token, id;
    explicit vkapiwin(QWidget *parent = 0);
    ~vkapiwin();
    Ui::vkapiwin *ui;
public slots:
    virtual void check_url(QUrl &url);
};

#endif // VKAPIWIN_H
