/*var json_registro =
    {"username": username,
    "password": password,
    "repassword": repassword}
    register = $.ajax({
        type: 'POST',
        url: 'http://192.168.1.137:5016/api/registrar/persona',
        data: json_registro,
        success: function (response) {
            output= response;
            alert(output);
        }
    }).done(function (json_registro) {
        console.log(json_registro);
        alert(json_registro);
    });

$(document).ready(function() {

  $("#btn_fiscal").click(function(e) {

      var use_rname=$('#username').val()
      var password_=$('#password').val()
      var re_password=$('#repassword').val()
      console.log(use_rname);
      console.log(password_);
      console.log(re_password);

    var Username=use_rname;
    var Password=password_;
    var Repassword=re_password;

   e.preventDefault();

  $.ajax({
    type: "POST",
    url: "http://192.168.1.137:5016/api/registrar/persona",
    data: {
        Username,
     Password, Repassword},
    success: function (result) {
          if (result.Status == ("CORRECTO")){
            alert('ok');

          $(location).attr('href','Index.html');

          }else {
            alert('Revise los datos');
          }
          console.log(result.Status);
      },
    error: function(result) {
          alert('error'+result);
     }
   });
});
    */