#include "vkapiwin.h"
#include "ui_vkapiwin.h"
#include <QUrlQuery>
#include <QSsl>
#include <QWidget>

vkapiwin::vkapiwin(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::vkapiwin)
{
    ui->setupUi(this);
    connect(ui->preview,SIGNAL(urlChanged(QUrl url)),this,SLOT(check_url(QUrl)));
    ui->preview->load(QUrl("https://oauth.vk.com/authorize?client_id=5681259&display=mobile&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.60&state=123456"));
    connect(ui->preview,SIGNAL(urlChanged(QUrl url)),this,SLOT(check_url(QUrl)));
    if (token == NULL)
    {
        ui->label->setText("не получилось");
    }
}

void vkapiwin::check_url(QUrl &url)
{
    QString url1 = url.toString().replace("#","?");
    this->token = QUrlQuery(url1).queryItemValue("access_token");
    this->id = QUrlQuery(url1).queryItemValue("user_id");
}

vkapiwin::~vkapiwin()
{
    delete ui;
}
