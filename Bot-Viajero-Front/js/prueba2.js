/**
 * Created by hunterz on 4/7/17.
 */

function prueba2() {
    var jsonTest=
        {
            "username": "pame",
            "password": "123",
            "repassword": "123"
         }

         var output= $.ajax({
             url:'http://192.168.43.26:5016/api/registrar/persona',
             type: 'POST',
             data: jsonTest,
             dataType: 'json',
             succes: function(data) {
                    //
                    //Change data.source to data.something , where something is whichever part of the object you want returned.
                    //To see the whole object you can output it to your browser console using:
                    //console.log(data);
                    document.getElementById("output").innerHTML = data.source;
                },
                error: function(err) { alert(err); },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-Mashape-Authorization", "YOUR_API_KEY"); // Enter here your Mashape key
                }
             }


         )

}
