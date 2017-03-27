(function(window, google, mapa) {

    // map options
        var options = mapa.MAP_OPTIONS,
        element = document.getElementById('cuadro_mapa'),
        map = mapa.create(element, options);
    map.zoom(10);

    map._on('click', function(){
        //aqui es donde se van a conectar las localizaciones señaladas
    })

    map.addMarker({
        lat: 10.4678335,
        lng: -84.64268060000001,
        content: 'ihfgirh gurf'
    });//La Fortuna

    map.addMarker({
        lat: 9.431868099999999,
        lng: -84.1619076
    });//Quepos

    map.addMarker({
        lat: 10.2749682,
        lng: -84.8255097
    });//Monte Verde

    map.addMarker(10.5424838, -83.50235520000001)//Tortuguero
    map.addMarker({
        lat: 10.5424838,
        lng: -83.50235520000001
    });//Tortuguero

    map.addMarker({
        lat: 8.5336439,
        lng: -83.30678019999999
    });//Puerto Jimenez

    map.addMarker({
        lat: 10.6345964,
        lng: -85.44067469999999
    });//Liberia

    map.addMarker({
        lat: 10.0525756,
        lng: -84.20679919999998
    });//Canton de Alajuela

    map.addMarker({
        lat: 10.0525756,
        lng: -84.20679919999998
    });//Volcan Miravalles

    map.addMarker({
        lat: 10.473523,
        lng: -84.01674229999998
    });//Sarapiqui

    map.addMarker({
        lat: 9.7347856,
        lng: -82.84521459999996
    });//Cahuita



}(window, google, window.Mapa));








