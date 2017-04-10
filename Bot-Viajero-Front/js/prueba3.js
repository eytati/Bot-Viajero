
function registerPlane() {
    var companyname = document.getElementById("companyname").value;
    var packageOrigen = document.getElementById("packageOrigen").value;
    var packageDestino = document.getElementById("packageDestino").value;
    var cantPasajeros = document.getElementById("cantPasajeros").value;
    var horarioSalida = document.getElementById("horarioSalida").value;
    var horarioLlegada = document.getElementById("horarioLlegada").value;
    var costoTotal = document.getElementById("costoTotal").value;

       /* var json_data=
            {
           "companyname": "American,
            "packageOrigen": "Irazu,
            "packageDestino": Puerto Viejo,
            "cantPasajeros": 100,
            "horarioSalida": 12: 00 am,
            "horarioLlegada": 4:00 pm,
            "costoTotal": 15000,

    }*/
       var jsonP=
           {"companyname": companyname,
            "packageOrigen": packageOrigen,
            "packageDestino": packageDestino,
            "cantPasajeros": cantPasajeros,
            "horarioSalida": horarioSalida,
            "horarioLlegada": horarioLlegada,
            "costoTotal": costoTotal,

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                success : function(result) {

                    //alert("done")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }


