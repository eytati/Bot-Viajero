
var json = [
{
      "Ciudad" : "Alajuela Provincia, La Fortuna, Costa Rica",
      "latitude" : 10.4678335,
      "longitude" : -84.64268060000001
      }, {
      "Ciudad" : "Quepos, Provincia de Puntarenas, Costa Rica",
      "latitude" : 9.431868099999999,
      "longitude" : -84.1619076
      }, {
      "Ciudad" : "Monte Verde, Costa Rica",
      "latitude" : 10.2749682,
      "longitude" : -84.8255097
      }, {
      "Ciudad" : "Tortuguero, Provincia de Limón, Costa Rica",
      "latitude" : 	10.4488767,
      "longitude" : -83.5069226
      }, {
      "Ciudad" : "Puerto Jiménez, Provincia de Puntarenas, Costa Rica",
      "latitude" : 8.5336439,
      "longitude" : -83.30678019999999
      },
      {
      "Ciudad" : "Liberia, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.6345964,
      "longitude" : -85.44067469999999
      },
      {
      "Ciudad" : "Cantón de Alajuela, Provincia de Alajuela, Costa Rica",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
           {
      "Ciudad" : "Volcán Miravalles, Bagaces, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
           {
      "Ciudad" : "Heredia, Sarapiquí, Costa Rica",
      "latitude" : 10.473523,
      "longitude" : -84.01674229999998
    },
          {
      "Ciudad" : "Cahuita, Provincia de Limón, Costa Rica",
      "latitude" : 9.7347856,
      "longitude" : -82.84521459999996
    },
          {
      "Ciudad" : "Bagaces, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.5388321,
      "longitude" : -85.25413600000002
    },
           {
      "Ciudad" : "Irazú, Provincia de Cartago, Costa Rica",
      "latitude" : 9.9799813,
      "longitude" : -85.230841
    },
            {
      "Ciudad" : "Pérez Zeledón, Provincia de San José, Costa Rica  ",
      "latitude" : 9.35473,
      "longitude" : -83.84907609999999
    },
           {
      "Ciudad" : "Provincia de Puntarenas, Uvita, Costa Rica",
      "latitude" : 9.163500899999999,
      "longitude" : -83.7358514
    },
          {
      "Ciudad" : "Cartago Province, Cartago, Costa Rica",
      "latitude" : 9.8638091,
      "longitude" : -83.91619349999996
    },
           {
      "Ciudad" : "Volcan Tenorio, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.6713889,
      "longitude" : -85.01249999999999
    },
    {
      "Ciudad" : "Turrialba, Provincia de Cartago, Costa Rica",
      "latitude" : 9.9067054,
      "longitude" : -83.68005119999998
    },
    {
      "Ciudad" : "Parque Nacional Chirripó, Pérez Zeledón, Provincia de San José, Costa Rica",
      "latitude" : 9.5134327,
      "longitude" : -83.4946218
    },
    {
      "Ciudad" : "Península de Santa Elena, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.8841185,
      "longitude" : -85.78716630000002
    },
              {
      "Ciudad" : "Parque Nacional La Amistad, Provincia de Limón, Costa Rica",
      "latitude" : 9.4071,
      "longitude" : -82.93880000000001
    },
     {
      "Ciudad" : "Cordillera de Talamanca, Provincia de San José, Costa Rica",
      "latitude" : 9.6540146,
      "longitude" : -84.08309109999999
    },{
      "Ciudad" : "Los Chiles, Provincia de Alajuela, Costa Rica",
      "latitude" : 10.398795,
      "longitude" : -84.33874500000002
    },
  {
      "Ciudad" : "Parque Nacional Braulio Carrillo, Provincia de Heredia, Costa Rica",
      "latitude" : 10.1599,
      "longitude" : -83.974425
    },
 {
      "Ciudad" : "Nicoya, Provincia de Guanacaste, Costa Rica",
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
              title: data.Ciudad
          });

     var infoWindow = new google.maps.InfoWindow();
        google.maps.event.addListener(marker, "click", function(e) {
    infoWindow.setContent(data.Ciudad);
    infoWindow.open(map, marker);
});
     (function(marker, data) {

  google.maps.event.addListener(marker, "click", function(e) {
    infoWindow.setContent(data.Ciudad);
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
  /* var origin2= document.getElementById('origin').value;

     var destination2= document.getElementById('destination').value;
     var jsonP =
     {
     "origin": origin2,
     "destination": destination2,
     }

     var data = JSON.stringify(jsonP);

     $.ajax({
     url: "http://192.168.43.26:5016/api/ruta/corta",
     type: "POST",
     contentType: "application/json",
     data: data,
     dataType: 'json',
     async: false,

     success: function (data) {
     json_short= JSON.stringify(data);
     alert(json_short);
     localStorage["json_short"]= json_short;
     window.location.href = "calculoRutas.html"

     }, error: function (error) {
     alert('Datos incorrectos');
     }
     });
  //var DATA = localStorage.json_transport;
    //alert(DATA);
    //var json = JSON.parse(DATA);
    //alert(json.Valores);
    //var json_3 = JSON.parse(json_2);
    //alert(json_3.Distancia);

    var routes= localStorage.json_short;
    //alert("1 " + routes);
    var routes2= JSON.parse(routes);
    //alert("2 " + routes2.City);
    var  route3= JSON.parse(routes2.City[0]);
    //alert("3" + route3.ciudad);

    var waypts = [];
     var checkboxArray = routes;
    for (var i = 0; i < checkboxArray.length; i++) {
     if (checkboxArray[i].City) {
     waypts.push({
     location: checkboxArray[i].ciudad,
     stopover: true
     });
     }
     };     */

    directionsService.route({
        origin: document.getElementById('origin').value,
        destination: document.getElementById('destination').value,
       // waypoint: waypts,
        //optimizeWaypoints: true,
        travelMode: google.maps.TravelMode.DRIVING
    }, function (response, status) {
        if (status === google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        }
    });
}

