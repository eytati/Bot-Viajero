function registro_Avion() {

    var company = document.getElementById("company").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var passengers = document.getElementById("passengers").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("arrive_time").value;
    var total = document.getElementById("total").value;
    var User_token = sessionStorage.getItem("user_token");

               alert(JSON.stringify(User_token));

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
            $.ajax({
               async: true,
       crossDomain: true,
                type: 'POST',
                url: 'http://192.168.1.141:5016/api/registrar/ruta/avion',
                contentType:"application/json",
                data: jsonP,
                dataType: 'json',
              beforeSend: function (xhr) {
                 xhr.setRequestHeader("Authorization", "Basic "
                     + btoa(User_token + ":" + " "));
             },

                processData: false,
                success : function(datos, e) {

                    alert("Registrado con éxito");

                 window.location.href="Index.html";

    },           error: function(error){
                 alert(error);
}
            })
        }