
function register() {
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

                    //alert("done")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }


       /*  $(document).ready(function register4() {
            $("#buttonRegister").click(function (e) {
                var username2= $('#username').val()
                var password2= $('#password').val()
                var repassword2= $('#repassword').val()
                console.log(username2);
                console.log(password2);
                console.log(repassword2);

                var user_name= username2;
                var _password= password2;
                var re_password= re_password;

                var jsonP=
           {
                "username": user_name,
            "password": _password,
            "repassword": re_password
           }

     var data = JSON.stringify(jsonP);

                e.preventDefault();

                 $.ajax({
                type: 'POST',
                url: 'http://192.168.1.137:5016/api/registrar/ruta',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                success : function(result) {

                    //alert("done")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })

            })

        })*/
