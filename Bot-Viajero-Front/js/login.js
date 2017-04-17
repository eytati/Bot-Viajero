alert('Hola')
function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;


    var jsonP =
        {
            "username": username,
            "password": password,
        }

    var dataPerson = JSON.stringify(jsonP);


         $.ajax({
             //crossDomain: true,
             url: "http://192.168.43.26:5016/api/token/" + username ,
             type: "GET",
             contentType: "application/json",
             data: dataPerson,
             dataType: 'json',

             beforeSend: function (xhr) {
                 xhr.setRequestHeader("Authorization", "Basic "
                     + btoa(username + ":" + password));
             },
             success: function (datos,e) {
                 alert(datos)
                 sessionStorage.setItem("token", datos['token']);
                 window.location.href = "Index.html"
              //   console.log(result.status)
//              return datos

             }, error: function (error) {
                 alert('Datos incorrectos');
             }

         })

}