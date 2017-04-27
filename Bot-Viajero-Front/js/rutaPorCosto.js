function readRouteCost() {
    alert("entro");

    localStorage["origin"]= origin;
    localStorage["destination"]= destination;

    var jsonP =
        {
            "origin": origin,
            "destination": destination,
        }

    var data = JSON.stringify(jsonP);

    alert(data);
      $.ajax({
             url: "http://192.168.1.138::5016/api/rutas/mejores/transporte",
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
}
