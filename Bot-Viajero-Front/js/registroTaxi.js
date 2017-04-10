    alert("Hola");

function registro_Taxi() {
    var company = document.getElementById("company").value;
    var registration = document.getElementById("registration").value;
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;
    var lastname = document.getElementById("lastname").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var total = document.getElementById("total").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("arrive_time").value;

       /* var json_data=
            {
           "companyname": TaxiTico,
            "placa": 3454,
            "IDConductor": 2234213,
            "nombreConductor": Guillermo,
            "apellidosConductor": Rojas Fallas,
            "packageOrigen": Tortuguero,
            "packageDestino": Bagaces,
            "costoKilometro": 575,
            "horarioSalida": 9:00 pm,
            "horarioLlegada": 1:00 am,
    }*/

       var jsonP=
           {"company": company,
            "id": registration,
            "IDConductor": id,
            "name": name,
            "lastname": lastname,
            "origin": origin,
            "destination": destination,
            "total": total,
            "departure_time": departure_time,
            "horarioLlegada": arrival_time,

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/taxi',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                 //beforeSend: function (header,) {
                  //  header.setRequestHeader("Authorization", "Basic "
                //        + btoa(tokenTest + ":" + password));
              //  },
                success : function(result) {

                   // alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        };
