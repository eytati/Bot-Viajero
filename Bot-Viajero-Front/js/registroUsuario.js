

alert("Hola Mundo");

function getMyData(data) {
    alert(data);
}

getMyData("Enter your data here");

var username = ana;
var password = ana;
var repassword = ana;

var json_registro = {"username": username, "password": password, "repassword": repassword};
alert2({
            type: 'POST',
            url: '127.0.0.1:5000/api/registrar/persona',
            data: json_registro,
            dataType: 'application/json',
            success: function(data) {
             alert("POSTED SUCCESSFULLY TO THE SERVER");
             $('#subscribePage').html('<h1>POSTED</h1>');
          } // Success Function
          });
