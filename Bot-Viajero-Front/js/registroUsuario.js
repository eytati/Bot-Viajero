alert("Hola Mundo");

function getMyData(data) {
    alert(data);
}

getMyData("Enter your data here");

var username = document.getElementById('username');
var password = document.getElementById('password');
var confirmPassword = document.getElementById('confirmPassword');

var json_registro = {"username": username, "password": password, "confirmPassword": confirmPassword};
alert2({
            type: 'POST',
            url: '127.0.0.1:5000/api/registrar/persona',
            data: json_registro,
            dataType: 'json',
            success: function(data) {
             alert("POSTED SUCCESSFULLY TO THE SERVER");
             $('#subscribePage').html('<h1>POSTED</h1>');
          } // Success Function
          });

function checkPassword() {

     if (password.value != confirmPassword.value){
      alert('Wrong confirm password !');
  }
  else {
      alert('Right confirm password !');
  }

}

/*
function checkUsername() {                             // Declare function
  var elMsg = document.getElementById('feedback');     // Get feedback element
  if (this.value.length < 5) {                         // If username too short
    elMsg.textContent = 'Nombre de usuario debe ser mayor a 5 caracteres'; // Set msg
  } else {                                             // Otherwise
    elMsg.textContent = '';                            // Clear msg
  }
}

var elUsername = document.getElementById('username');  // Get username input
// When it loses focus call checkUsername()
elUsername.addEventListener('blur', checkUsername, false);


function  checkPassword() {
  var confirmMessage = document.getElementById('confirmMessage');
  var password = document.getElementById('password');
  var confirmPassword = document.getElementById('confirmPassword');

  if (password.value != confirmPassword.value){
      alert('Wrong confirm password !');
  }
  else {
      alert('Right confirm password !');
  }
}
*/

