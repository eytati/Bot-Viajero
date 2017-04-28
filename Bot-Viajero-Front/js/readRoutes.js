
function readRoute() {

    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;

    localStorage["origin"]= origin;
    localStorage["destination"]= destination;
 //   localStorage["json_transport"]= 'nada';


    var jsonP =
        {
            "origin": origin,
            "destination": destination,
        };

    var data = JSON.stringify(jsonP);


      $.ajax({
             url: "http://192.168.1.138:5016/api/rutas/mejores/transporte",
             type: "POST",
             contentType: "application/json",
             data: data,
             dataType: 'json',

             success: function (data) {
                 json_transport= JSON.stringify(data);
                 alert(json_transport);
                 localStorage["json_transport"]= json_transport;
                 alert(json_transport.Valores);
                 window.location.href = "calculoRutas.html"

             }, error: function (error) {
                 alert('Datos incorrectos');
             }
         });


}




