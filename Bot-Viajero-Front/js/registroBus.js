var tokenTest = sessionStorage.getItem("tokenTest");

    alert("Hola");

function registro_Bus() {
    var company = document.getElementById("companyname").value;
    var registration = document.getElementById("registration").value;
    var name = document.getElementById("name").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var passengers = document.getElementById("passengers").value;
    var total = document.getElementById("total").value;

       /* var json_data=
            {
           "companyname": "TicaBus",
           "registration": "67281",
           "name": "Luis",
           "origin": "Cartago",
           "destination": "Turrialba",
           "passengers": 50,
           "total": 3000
    }*/

       var jsonP=
           {
           "companyname": company,
           "registration": registration,
           "name": name,
           "origin": origin,
           "destination": destination,
           "passengers": passengers,
           "total": total

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta/bus',
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

