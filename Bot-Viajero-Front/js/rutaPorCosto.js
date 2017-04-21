function readRouteCost() {
    alert("entro");
    var origin = document.getElementById("origin").value;
    alert(origin);
    var destination = document.getElementById("destination").value;
    alert(destination);

    var jsonP =
        {
            "origin": origin,
            "destination": destination,
        }

    var data = JSON.stringify(jsonP);
    alert(data);
      $.ajax({
             url: "http://192.168.43.26:5016/api/rutas/mejores/costo",
             type: "POST",
             contentType: "application/json",
             data: data,
             dataType: 'json',

             success: function (datos) {
               var routes = JSON.stringify(datos);
                 alert(routes);
                 window.location.href = "rutasPorCosto.html"

             }, error: function (error) {
                 alert('Datos incorrectos');
             }
         });
}
