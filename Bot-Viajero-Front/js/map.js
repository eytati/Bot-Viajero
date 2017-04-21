
var json = [
{
      "ciudad" : "Alajuela Provincia, La Fortuna, Costa Rica",
      "latitude" : 10.4678335,
      "longitude" : -84.64268060000001
      }, {
      "ciudad" : "Quepos, Provincia de Puntarenas, Costa Rica",
      "latitude" : 9.431868099999999,
      "longitude" : -84.1619076
      }, {
      "ciudad" : "Monte Verde, Costa Rica",
      "latitude" : 10.2749682,
      "longitude" : -84.8255097
      }, {
      "ciudad" : "Tortuguero, Provincia de Limón, Costa Rica",
      "latitude" : 	10.4488767,
      "longitude" : -83.5069226
      }, {
      "ciudad" : "Puerto Jiménez, Provincia de Puntarenas, Costa Rica",
      "latitude" : 8.5336439,
      "longitude" : -83.30678019999999
      },
      {
      "ciudad" : "Liberia, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.6345964,
      "longitude" : -85.44067469999999
      },
      {
      "ciudad" : "Cantón de Alajuela, Provincia de Alajuela, Costa Rica",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
           {
      "ciudad" : "Volcán Miravalles, Bagaces, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
           {
      "ciudad" : "Heredia, Sarapiquí, Costa Rica",
      "latitude" : 10.473523,
      "longitude" : -84.01674229999998
    },
          {
      "ciudad" : "Cahuita, Provincia de Limón, Costa Rica",
      "latitude" : 9.7347856,
      "longitude" : -82.84521459999996
    },
          {
      "ciudad" : "Bagaces, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.5388321,
      "longitude" : -85.25413600000002
    },
           {
      "ciudad" : "Irazú, Provincia de Cartago, Costa Rica",
      "latitude" : 9.9799813,
      "longitude" : -85.230841
    },
            {
      "ciudad" : "Pérez Zeledón, Provincia de San José, Costa Rica  ",
      "latitude" : 9.35473,
      "longitude" : -83.84907609999999
    },
           {
      "ciudad" : "Provincia de Puntarenas, Uvita, Costa Rica",
      "latitude" : 9.163500899999999,
      "longitude" : -83.7358514
    },
          {
      "ciudad" : "Cartago Province, Cartago, Costa Rica",
      "latitude" : 9.8638091,
      "longitude" : -83.91619349999996
    },
           {
      "ciudad" : "Volcan Tenorio, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.6713889,
      "longitude" : -85.01249999999999
    },
    {
      "ciudad" : "Turrialba, Provincia de Cartago, Costa Rica",
      "latitude" : 9.9067054,
      "longitude" : -83.68005119999998
    },
    {
      "ciudad" : "Parque Nacional Chirripó, Pérez Zeledón, Provincia de San José, Costa Rica",
      "latitude" : 9.5134327,
      "longitude" : -83.4946218
    },
    {
      "ciudad" : "Península de Santa Elena, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.8841185,
      "longitude" : -85.78716630000002
    },
              {
      "ciudad" : "Parque Nacional La Amistad, Provincia de Limón, Costa Rica",
      "latitude" : 9.4071,
      "longitude" : -82.93880000000001
    },
     {
      "ciudad" : "Cordillera de Talamanca, Provincia de San José, Costa Rica",
      "latitude" : 9.6540146,
      "longitude" : -84.08309109999999
    },{
      "ciudad" : "Los Chiles, Provincia de Alajuela, Costa Rica",
      "latitude" : 10.398795,
      "longitude" : -84.33874500000002
    },
  {
      "ciudad" : "Parque Nacional Braulio Carrillo, Provincia de Heredia, Costa Rica",
      "latitude" : 10.1599,
      "longitude" : -83.974425
    },
 {
      "ciudad" : "Nicoya, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.1445678,
      "longitude" : -85.45302950000001
    }
];

function initMap() {
    var directions= new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var lat= {lat: 9.748916999999999, lng: -83.75342799999999};
    var map = new google.maps.Map(document.getElementById('map'), {

        zoom: 8,
        center: lat
    });
      for (var i = 0, length = json.length; i < length; i++) {
          var data = json[i],
              latLng = new google.maps.LatLng(data.latitude, data.longitude);

          // Creating a marker and putting it on the map
          var marker = new google.maps.Marker({
              position: latLng,
              map: map,
              title: data.ciudad
          });

     var infoWindow = new google.maps.InfoWindow();
        google.maps.event.addListener(marker, "click", function(e) {
    infoWindow.setContent(data.ciudad);
    infoWindow.open(map, marker);
});
     (function(marker, data) {

  google.maps.event.addListener(marker, "click", function(e) {
    infoWindow.setContent(data.ciudad);
    infoWindow.open(map, marker);
  });

})(marker, data);
      }


    directionsDisplay.setMap(map);

    var onChangeHandler = function() {
        calculateAndDisplay(directions, directionsDisplay);
    };
    document.getElementById('origin').addEventListener('change', onChangeHandler);
    document.getElementById('destination').addEventListener('change', onChangeHandler);

}

function calculateAndDisplay(directionsService, directionsDisplay) {
    directionsService.route({
        origin: document.getElementById('origin').value,
        destination: document.getElementById('destination').value,

        travelMode: google.maps.TravelMode.DRIVING
    }, function(response, status) {
        if (status === google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        }
    });
}

