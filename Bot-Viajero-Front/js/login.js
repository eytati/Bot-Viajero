function login() {
    //  var formP = document.getElementById("formP").submit();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    /* var json_data=
     {
     "username": "palo",
     "password": "pass",
     }*/
    var jsonP =
        {
            "username": username,
            "password": password,
        }

    var datos = JSON.stringify(jsonP);
    //alert(datos)

       /*  $.ajax({
             //crossDomain: true,
             url: "http://192.168.1.137:5016/api/token/mari" ,
             type: "GET",
             contentType: "application/json",
             data: datos,
             dataType: 'json',
             beforeSend: function (xhr) {
                 xhr.setRequestHeader("Authorization", "Basic "
                     + btoa(username + ":" + password));
             },
             success: function (result) {

                 alert('Regsitrado')
                 window.location.href = "Index.html"
                 console.log(result.status)

             }, error: function (error) {
                 alert('Datos incorrectos');
             }
         })*/

           var  settings ={
             //crossDomain: true,
             url: "http://192.168.1.137:5016/api/token/mari" ,
             type: "GET",
             contentType: "application/json",
             data: datos,
             dataType: 'json',
             beforeSend: function (xhr) {
                 xhr.setRequestHeader("Authorization", "Basic "
                     + btoa(username + ":" + password));
             },
             success: function (result) {

                 alert('Regsitrado')
                 window.location.href = "Index.html"
                 console.log(result.status)

             }, error: function (error) {
                 alert('Datos incorrectos');
             }
         }

$.ajax(settings).done(function (response) {
  console.log(response);
});

}