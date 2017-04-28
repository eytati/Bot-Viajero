
function registro_Tren() {


    var company = document.getElementById("company").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("arrival_time").value;
    var total = document.getElementById("total").value;
    var  User_token = localStorage.user_token;
    var User_name = sessionStorage.getItem('user_name');

       var jsonP=
           {"company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total,

           }


     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.138:5016/api/registrar/ruta/tren',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("Authorization", "Basic "
                        + btoa(User_token + ":" + User_name));
                },
                success : function(result) {
                   alert("Regisrado con éxito");
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }

