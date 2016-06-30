ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
        center: [55.751574, 37.573856],
        zoom: 11,
        behaviors: ['default', 'scrollZoom'],
        controls: ['geolocationControl']  //Кнопка геолокации
    }, {
        searchControlProvider: 'yandex#search'
}),

clusterer = new ymaps.Clusterer({    //Создание кластера
    preset: 'islands#invertedVioletClusterIcons',
    groupByCoordinates: false,
    clusterDisableClickZoom: true,
    clusterHideIconOnBalloonOpen: false,
    geoObjectHideIconOnBalloonOpen: false
}),

getPointData = function (index) { //изменить параметры
    return {
        balloonContentHeader: points[i].name,   //Заголовок балуна, передается название объекта
        balloonContentBody: "<b>Адрес: </b>" + points[i].address,  //Вывод адреса в основной блок балуна
        hintContent: points[i].name,  //Подсказка при наведении на метку, вывод названия объекта
    };
},

getPointOptions = function () {
    return {
        preset: 'islands#violetIcon'  //Выбор отображения метки
    };
},

geoObjects = [];

for(var i = 0, len = points.length; i < len; i++) { //Цикл для вывода каждой метки
    var myPlacemark = new ymaps.Placemark(points[i].coordinates, getPointData(i), getPointOptions());
    geoObjects[i] = myPlacemark;
}

clusterer.add(geoObjects);
myMap.geoObjects.add(clusterer);

});