
function readRoute() {

    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;



    var jsonP =
        {
            "origin": origin,
            "destination": destination,
        }

    var data = JSON.stringify(jsonP);


      $.ajax({
             url: "http://192.168.43.26:5016/api/rutas/mejores/transporte",
             type: "POST",
             contentType: "application/json",
             data: data,
             dataType: 'json',

             success: function (datos) {
               var routes = JSON.stringify(datos);
                 alert(routes);

                 window.location.href = "calculoRutas.html"

             }, error: function (error) {
                 alert('Datos incorrectos');
             }

         });

         sessionStorage.setItem('origin', origin);
    sessionStorage.setItem('destination', destination);
}

/*function readRouteDistance2() {

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
                 window.location.href = "calculoRutas.html"

             }, error: function (error) {
                 alert('Datos incorrectos');
             }

         });

}*/