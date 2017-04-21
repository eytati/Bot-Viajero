


alert('hola');
function readRoute() {
    var origen = document.getElementById("origin").value;
    var destino = document.getElementById("destination").value;

    var jsonP =
        {
            "origin": origen,
            "destination": destino,
        }

    var data = JSON.stringify(jsonP);

alert(data);

         $.ajax({
             url: "http://192.168.43.26:5016/api/rutas/mejores/transporte",
             type: "POST",
             contentType: "application/json",
             data: jsonP,
             dataType: 'json',

             success: function (datos) {
                 alert(datos);
                                  window.location.href = "calculoRutas.html"

                  //sessionStorage.setItem('origin', origen);
                 //sessionStorage.setItem('destination', destino);


             }, error: function (error) {
                 alert('Datos incorrectos');
             }

         })

}