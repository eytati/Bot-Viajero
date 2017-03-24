/**
 * Created by hunterz on 3/23/17.
 */
function checkPassword() {                             // Declare function
  var elMsg = document.getElementById('feedback');     // Get feedback element
  if (this.value.length < 5) {                         // If username too short
    elMsg.textContent = 'Username must be 5 characters or more'; // Set msg
  } else {                                             // Otherwise
    elMsg.textContent = '';                            // Clear msg
  }
}

var elUsername = document.getElementById('username');  // Get username input
var password = document.getElementById("pass1").value;
var confirmpassword = document.getElementById("pass2").value;
// When it loses focus call checkUsername()
elUsername.addEventListener('blur', checkPassword, false);


