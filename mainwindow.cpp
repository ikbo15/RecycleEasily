#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "vkapiwin.h"
#include <QUrlQuery>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_2_clicked()
{
 vkapiwin *vkapi= new vkapiwin();
 vkapi->show();
 if (vkapi == NULL)
 {
     vkapi->hide();
     this->show();
 }
}

void MainWindow::on_pushButton_clicked()
{
    QString login=ui->textEdit->toPlainText();
    QString password=ui->textEdit_2->toPlainText();
    if (login==NULL || password==NULL)
    {
        ui->label_3->setStyleSheet("color: rgb(200,0,0)");
        ui->label_3->setText("логин и пароль не получены");
    }
    else
    {
        ui->label_3->setStyleSheet("color: rgb(0,200,0)");
        ui->label_3->setText("логин и пароль получены");
    }
}
