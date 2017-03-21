(function(window, google){

    //map option
    var options = {
        center: {
            latitud: 9.6229339,
            longitud: -86.4994862
        },
        zoom: 10,
        disableDefaultUI: true,
        scrollwheel: false,
        draggable: true,
        mapTypeId: google.maps.MapTypeId.SATELLIT
    },

    element = document.getElementById('map-canvas'),
    //map
    map = new google.maps.Map(element, options);

}(window, wondow.google));
