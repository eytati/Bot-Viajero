function initMap() {
    var directions= new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {lat: 10.0000000, lng: -84.0000000},
        draggable: false
    });
    directionsDisplay.setMap(map);

    var onChangeHandler = function() {
        calculateAndDisplay(directions, directionsDisplay);
    };
    document.getElementById('packageDestino').addEventListener('change', onChangeHandler);
    document.getElementById('packageDestino').addEventListener('change', onChangeHandler);
}

function calculateAndDisplay(directionsService, directionsDisplay) {
    directionsService.route({
        origin: document.getElementById('packageOrigen').value,
        destination: document.getElementById('packageDestino').value,
        travelMode: google.maps.TravelMode.DRIVING
    }, function(response, status) {
        if (status === google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}

/*$.ajax({
    type: "POST",
    contentType: "application/json; charset=utf-8",
    url: "<URL WEBSERVICE>",
    dataType: "json",
    data: "<PARÁMETROS>",
    success: function (data){<RESPUESTA_WEB_SERVICE>},
    error: function (data){<ERROR_WEB_SERVICE>}
});*/