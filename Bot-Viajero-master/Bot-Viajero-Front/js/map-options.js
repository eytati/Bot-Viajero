(function(window, google, mapa) {

    mapa.MAP_OPTIONS = {
        center: {
            lat: 10.0000000,
            lng: -84.0000000
        },
        zoom: 9,
        minZoom: 8,
        maxZoom: 9,
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
