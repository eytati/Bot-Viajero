var tokenTest = sessionStorage.getItem("tokenTest");


function registro_Bus() {
    var company = document.getElementById("company").value;
    var registration = document.getElementById("registration").value;
    var name = document.getElementById("name").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var passengers = document.getElementById("passengers").value;
    var departure_time= document.getElementById("departure_time").value;
    var arrival_time= document.getElementById("arrival_time").value;
    var total = document.getElementById("total").value;


       var jsonP=
           {
           "companyname": company,
           "registration": registration,
           "name": name,
           "origin": origin,
           "destination": destination,
           "passengers": passengers,
           "departure_time": departure_time,
           "arrival_time":arrival_time,
           "total": total

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.141:5016/api/registrar/ruta/bus',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                 //beforeSend: function (header,) {
                   // xhr.setRequestHeader("Authorization", "Basic "
                     //   + btoa(tokenTest + ":" + password));
                //},
                success : function(result) {
                    alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }

