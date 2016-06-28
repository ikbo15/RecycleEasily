ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
        center: [55.751574, 37.573856],
        zoom: 11,
        behaviors: ['default', 'scrollZoom'],
        controls: ['geolocationControl']
    }, {
        searchControlProvider: 'yandex#search'
}),

clusterer = new ymaps.Clusterer({
    preset: 'islands#invertedVioletClusterIcons',
    groupByCoordinates: false,
    clusterDisableClickZoom: true,
    clusterHideIconOnBalloonOpen: false,
    geoObjectHideIconOnBalloonOpen: false
}),

getPointData = function (index) { //изменить параметры
    return {
        balloonContentHeader: points[i].name,
        balloonContentBody: "<b>Адрес: </b>" + points[i].address,
        balloonContentFooter: points[i].link,
        hintContent: points[i].name,
        //clusterCaption: index
    };
},

getPointOptions = function () {
    return {
        preset: 'islands#violetIcon'
    };
},

geoObjects = [];

for(var i = 0, len = points.length; i < len; i++) { 
    var myPlacemark = new ymaps.Placemark(points[i].coordinates, getPointData(i), getPointOptions());
    geoObjects[i] = myPlacemark;
}

clusterer.add(geoObjects);
myMap.geoObjects.add(clusterer);

});