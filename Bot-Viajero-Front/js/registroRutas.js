/**
 * Created by hunterz on 4/8/17.
 */
//-----------------------------------SCRIPT REGISTRO DE RUTA POR AVION----------------------------------------------//
function registroAvion() {
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
                url: 'http://192.168.1.137:5016/api/registrar/ruta/Avion',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                success : function(result) {

                   // alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }

//-----------------------------------SCRIPT REGISTRO DE RUTA POR TREN----------------------------------------------//

        function registroTren() {
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
                url: 'http://192.168.1.137:5016/api/registrar/ruta/Tren',
                contentType:"application/json",
                data: data,
                dataType: 'json',
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
    var companyname = document.getElementById("companyname").value;
    var placa = document.getElementById("placa").value;
    var IDConductor = document.getElementById("IDConductor").value;
    var nombreConductor = document.getElementById("nombreConductor").value;
    var apellidosConductor = document.getElementById("apellidosConductor").value;
    var packageOrigen = document.getElementById("packageOrigen").value;
    var packageDestino = document.getElementById("packageDestino").value;
    var costoKilometro = document.getElementById("costoKilometro").value;
    var horarioSalida = document.getElementById("horarioSalida").value;
    var horarioLlegada = document.getElementById("horarioLlegada").value;

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
           {"companyname": companyname,
            "placa": placa,
            "IDConductor": IDConductor,
            "nombreConductor": nombreConductor,
            "apellidosConductor": apellidosConductor,
            "packageOrigen": packageOrigen,
            "packageDestino": packageDestino,
            "costoKilometro": costoKilometro,
            "horarioSalida": horarioSalida,
            "horarioLlegada": horarioLlegada,

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/Taxi',
                contentType:"application/json",
                data: data,
                dataType: 'json',
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
    var companyname = document.getElementById("companyname").value;
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
           "companyname": companyname,
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
                success : function(result) {

                   // alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }
