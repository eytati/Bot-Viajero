function readRouteDistance() {

    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;

    var jsonP =
        {
            "origin": origin,
            "destination": destination,
        }

    var data = JSON.stringify(jsonP);


      $.ajax({
             url: "http://192.168.43.26:5016/api/rutas/mejores/distancia",
             type: "POST",
             contentType: "application/json",
             data: data,
             dataType: 'json',

             success: function (datos) {
               var routes = JSON.stringify(datos);
                 alert(routes);
                 window.location.href = "rutasPorDistancia.html"

             }, error: function (error) {
                 alert('Datos incorrectos');
             }

         });


}