/**
 * Created by hunterz on 4/8/17.
 */
//-----------------------------------SCRIPT REGISTRO DE RUTA POR AVION----------------------------------------------//
var tokenTest = sessionStorage.getItem("tokenTest");

function registroAvion() {
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
            "total": total,

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/avion',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                success : function(result, e) {

                    alert(result)

                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        };

//-----------------------------------SCRIPT REGISTRO DE RUTA POR TREN----------------------------------------------//

        function registroTren() {
    var company = document.getElementById("company").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    //var cantPasajeros = document.getElementById("cantPasajeros").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("arrival_time").value;
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
          //  "cantPasajeros": cantPasajeros,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total,

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/tren',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                beforeSend: function (xhr,) {
                    xhr.setRequestHeader("Authorization", "Basic "
                        + btoa(tokenTest + ":" + password));
                },
                success : function(result) {

                   // alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }

//-----------------------------------SCRIPT REGISTRO DE RUTA POR TAXI----------------------------------------------//

        function registroTaxi() {
    var company = document.getElementById("company").value;
    var registration = document.getElementById("registration").value;
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;
    var lastname = document.getElementById("lastname").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var total = document.getElementById("total").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("horarioLlegada").value;

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
                url: 'http://192.168.1.137:5016/api/registrar/ruta/Taxi',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                 beforeSend: function (header,) {
                    header.setRequestHeader("Authorization", "Basic "
                        + btoa(tokenTest + ":" + password));
                },
                success : function(result) {

                   // alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }


 //-----------------------------------SCRIPT REGISTRO DE RUTA POR BUS----------------------------------------------//

        function registroBus() {
    var company = document.getElementById("companyname").value;
    var placa = document.getElementById("placa").value;
    var nombreConductor = document.getElementById("nombreConductor").value;
    var packageOrigen = document.getElementById("packageOrigen").value;
    var packageDestino = document.getElementById("packageDestino").value;
    var capacidad = document.getElementById("capacidad").value;
    var costoTotal = document.getElementById("costoTotal").value;

       /* var json_data=
            {
           "companyname": "TicaBus",
           "placa": "67281",
           "nombreConductor": "Luis",
           "packageOrigen": "Cartago",
           "packageDestino": "Turrialba",
           "capacidad": 50,
           "costoTotal": 3000
    }*/

       var jsonP=
           {
           "companyname": company,
           "placa": placa,
           "nombreConductor": nombreConductor,
           "packageOrigen": packageOrigen,
           "packageDestino": packageDestino,
           "capacidad": capacidad,
           "costoTotal": costoTotal

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/Bus',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                 beforeSend: function (header,) {
                    xhr.setRequestHeader("Authorization", "Basic "
                        + btoa(tokenTest + ":" + password));
                },
                success : function(result) {

                   // alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }
