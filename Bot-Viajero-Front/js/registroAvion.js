var tokenTest = sessionStorage.getItem("tokenTest");
    alert("hola");

function registro_Avion() {

    var company = document.getElementById("company").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var passengers = document.getElementById("passengers").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("arrive_time").value;
    var total = document.getElementById("total").value;


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
           {"company": company,
            "origin": origin,
            "destination": destination,
            "passengers": passengers,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/avion',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                success : function(datos, e) {

                    alert(datos)

                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }