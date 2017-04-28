
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
             url: "http://192.168.43.26:5016/api/rutas/mejores/transporte",
             type: "POST",
             contentType: "application/json",
             data: data,
             dataType: 'json',

             success: function (response) {
                 json_transport= JSON.stringify(response);
                 alert(json_transport);
                 localStorage["json_transport"]= json_transport;
                 window.location.href = "calculoRutas.html"

             }, error: function (error) {
                 alert('Datos incorrectos');
             }
         });


}




