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
             async: true,
             crossDomain: true,
             url: "http://192.168.1.138::5016/api/token/" + username ,
             type: "GET",
             contentType: "application/json",
             data: jsonP,
             dataType: 'json',
            // header:
              // {
	           //'authorization': "Basic " + btoa(username + ":" +password),
	           //contentType: "application/json"
	        //},
         beforeSend: function (xhr) {
         xhr.setRequestHeader("Authorization", "Basic "
              + btoa(username + ":" + password));
         },
             success: function (datos) {
                 alert(datos)
                 sessionStorage.setItem('user_token', datos);
                 sessionStorage.setItem('user_name', username);
                 sessionStorage.setItem('password', password);
                 window.location.href = "Index.html"


             }, error: function (error) {
                 alert('Datos incorrectos');
             }

         })

}