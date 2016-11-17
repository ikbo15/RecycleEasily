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
    ui->preview->load(QUrl("https://oauth.vk.com/authorize?client_id=5681259&display=mobile&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.60&state=123456"));
    ui->preview->show();
    connect(ui->preview,SIGNAL(urlChanged(QUrl)),this,SLOT(check_url(QUrl)));
}

vkapiwin::~vkapiwin()
{
    delete ui;
}

void vkapiwin::check_url(QUrl url)
{
    url = url.toString().replace("#","?");
    QString token = QUrlQuery(url).queryItemValue("access_token");
    QString id = QUrlQuery(url).queryItemValue("user_id");

}
