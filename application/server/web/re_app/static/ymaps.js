ymaps.ready(init);
var myMap, Placemark;

function init() {
    var myMap = new ymaps.Map('map', {
        center: [55.74, 37.58],
        zoom: 13,
        controls: ['geolocationControl']
    });
	
	Placemark = new ymaps.Placemark([55.752132, 37.670847], { 
            hintContent: 'Сфера экологии', 
            balloonContent: 'Сфера экологии'
        });

    myMap.geoObjects.add(Placemark);
}


