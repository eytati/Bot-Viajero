    alert("hola");

function registerPrueba() {
  //  var formP = document.getElementById("formP").submit();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var repassword = document.getElementById("repassword").value;

       /* var json_data=
            {
            "username": "palo",
            "password": "pass",
            "repassword": "pass"
    }*/
       var jsonP=
           {
                "username": username,
            "password": password,
            "repassword": repassword
           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.140:5016/api/registrar/persona',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                success : function(result) {
                 alert("Registrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }
