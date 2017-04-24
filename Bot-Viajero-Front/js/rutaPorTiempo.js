function readRouteTime() {

    var origin = sessionStorage.getItem('origin');
    var destination = sessionStorage.getItem('destination');

    var jsonP =
        {
            "origin": origin,
            "destination": destination,
        }

    var data = JSON.stringify(jsonP);
    alert(data);

      $.ajax({
             url: "http://192.168.43.26:5016/api/rutas/mejores/tiempo",
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