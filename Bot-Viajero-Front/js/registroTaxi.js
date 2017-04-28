
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
    var User_token = localStorage.user_token;
    var User_name = sessionStorage.getItem('user_name');

       var jsonP=
           {"company": company,
            "registration": registration,
            "id": id,
            "name": name,
            "lastname": lastname,
            "origin": origin,
            "destination": destination,
            "total": total,
            "departure_time": departure_time,
            "arrival_time": arrival_time

           } ;
      var data = JSON.stringify(jsonP);
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.138:5016/api/registrar/ruta/taxi',
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
                },
                error: function(error){
                alert(error);
}
            })
        }
