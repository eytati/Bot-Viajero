(function(window, google, mapa) {

    mapa.MAP_OPTIONS = {
        center: {
            lat: 9.7247129,
            lng: -85.1929077
        },
        zoom: 30,
        disableDefaultUI: false,
        scrollwheel: true,
        draggable: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoomControlOptions: {
            position: google.maps.ControlPosition.RIGHT_BOTTOM,
            style: google.maps.ZoomControlStyle.DEFAULT
        },

        panControlOptions: {
            position: google.maps.ControlPosition.LEFT_BOTTOM
        }
    };

}(window, google, window.Mapa || (window.Mapa = {})))
