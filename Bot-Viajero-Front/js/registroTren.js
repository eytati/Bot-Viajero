var tokenTest = sessionStorage.getItem("tokenTest");
 /*$.ajax({ 
    type: "GET", 
    url: "http://192.168.1.141:5016/api/ciudades", 
    contentType: "application/json", 
  //  data: data, 
     dataType: 'json',  
    success: function (datos, e) { 
             alert(datos + "Datos del json"); 
             var jsonTest=  $.parseJSON(datos);

             var listItems = '<option selected="selected" value="" widht="100px">- Seleccione lugar -</option>';

      for (var i = 0; i < jsonTest.Ciudades.length; i++) {
             listItems += "<option value='"+jsonTest.Ciudades[i].Ciudad+ "'>" + jsonTest.Ciudades[i].Ciudad +"</option>";

         }

         $("#origin").html(listItems);
         $("#destination").html(listItems);
            alert(jsonTest);

    //   console.log(result.status) //
    //       return datos  

      }, error: function (error) { 
          alert('Error'); 
      }
        // success: function(data) {
});*/


$.ajax({
    url: "http://192.168.43.26::5016/api/ciudades",
    //force to handle it as text
    dataType: "application/json",
    success: function(data) {

        //data downloaded so we call parseJSON function
        //and pass downloaded data
        var json = $.parseJSON(data);
        //now json variable contains data in json format
        //let's display a few items
        for (var i=0;i<json.cuidades.length;++i)
        {
            listItems += "<option value='"+json.ciudades[i].ciudad + "'>" + json.ciudades[i].ciudad  +"</option>";
           // $('#origin').append('<div class="name">'+json[i].name+'</>');
           // $('#destination').append('<div class="name">'+json[i].name+'</>');

        }
    }
});

function SelectJsonTrain() {
    var jsonData = {
     "ciudades": [
            {
      "id": 1,
      "ciudad" : "Alajuela Provincia, La Fortuna, Costa Rica",
      "latitude" : 10.4678335,
      "longitude" : -84.6426806
      },
      {
      "id": 2,
      "ciudad" : "Quepos, Provincia de Puntarenas, Costa Rica",
      "latitude" : 9.431868099999999,
      "longitude" : -84.1619076
      },
       {
      "id": 3,
      "ciudad" : "Monte Verde, Costa Rica",
      "latitude" : 10.2749682,
      "longitude" : -84.8255097
      },
      {
      "id": 4,
          "ciudad" : "Tortuguero, Provincia de Limon, Costa Rica",
      "latitude" : 	10.4488767,
      "longitude" : -83.5069226
      },
      {
      "id": 5,
      "ciudad" : "Puerto Jimenez, Provincia de Puntarenas, Costa Rica",
      "latitude" : 8.5336439,
      "longitude" : -83.30678019999999
      },
      {
       "id": 6,
      "ciudad" : "Liberia, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.6345964,
      "longitude" : -85.44067469999999
      },
      {
      "id": 7,
      "ciudad" : "Canton de Alajuela, Provincia de Alajuela, Costa Rica",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
     {
      "id": 8,
      "ciudad" : "Volcan Miravalles, Bagaces, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
    {
      "id": 9,
      "ciudad" : "Heredia, Sarapiqui, Costa Rica",
      "latitude" : 10.473523,
      "longitude" : -84.01674229999998
    },
     {
      "id": 10,
      "ciudad" : "Cahuita, Provincia de Limon, Costa Rica",
      "latitude" : 9.7347856,
      "longitude" : -82.84521459999996
    },
    {
      "id": 11,
      "ciudad" : "Bagaces, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.5388321,
      "longitude" : -85.25413600000002
    },
     {
      "id": 12,
      "ciudad" : "Irazu, Provincia de Cartago, Costa Rica",
      "latitude" : 9.9799813,
      "longitude" : -85.230841
    },
     {
      "id": 13,
      "ciudad" : "Perez Zeledon, Provincia de San José, Costa Rica",
      "latitude" : 9.35473,
      "longitude" : -83.84907609999999
    },
     {
      "id": 14,
      "ciudad" : "Provincia de Puntarenas, Uvita, Costa Rica",
      "latitude" : 9.163500899999999,
      "longitude" : -83.7358514
    },
     {
      "id": 15,
      "ciudad" : "Cartago Provincia, Cartago, Costa Rica",
      "latitude" : 9.8638091,
      "longitude" : -83.91619349999996
    },
     {
      "id": 16,
      "ciudad" : "Volcan Tenorio, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.6713889,
      "longitude" : -85.01249999999999
    },
    {
      "id": 17,
      "ciudad" : "Turrialba, Provincia de Cartago, Costa Rica",
      "latitude" : 9.9067054,
      "longitude" : -83.68005119999998
    },
    {
      "id": 18,
      "ciudad" : "Parque Nacional Chirripo, Perez Zeledon, Provincia de San Jose, Costa Rica",
      "latitude" : 9.5134327,
      "longitude" : -83.4946218
    },
    {
      "id": 19,
      "ciudad" : "Peninsula de Santa Elena, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.8841185,
      "longitude" : -85.78716630000002
    },
     {
      "id": 20,
      "ciudad" : "Parque Nacional La Amistad, Provincia de Limón, Costa Rica",
      "latitude" : 9.4071,
      "longitude" : -82.93880000000001
    },
     {
      "id": 21,
      "ciudad" : "Talamanca",
      "latitude" : 9.6540146,
      "longitude" : -84.08309109999999
    },
     {
      "id": 22,
      "ciudad" : "Los Chiles, Provincia de Alajuela, Costa Rica",
      "latitude" : 10.398795,
      "longitude" : -84.33874500000002
    },
  {
      "id": 23,
      "ciudad" : "Parque Nacional Braulio Carrillo, Provincia de Heredia, Costa Rica",
      "latitude" : 10.1599,
      "longitude" : -83.974425
    },
 {
      "id": 24,
      "ciudad" : "Nicoya, Provincia de Guanacaste, Costa Rica",
      "latitude" : 10.1445678,
      "longitude" : -85.45302950000001
    }
      ]
  };

     $(document).ready(function () {
         var listItems = '<option selected="selected" value="" widht="100px">- Seleccione lugar -</option>';

      for (var i = 0; i < jsonData.ciudades.length; i++) {
             listItems += "<option value='"+jsonData.ciudades[i].ciudad + "'>" + jsonData.ciudades[i].ciudad  +"</option>";

         }

         $("#origin").html(listItems);
         $("#destination").html(listItems);

     });
}
function registro_Tren() {


    var company = document.getElementById("company").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var departure_time = document.getElementById("departure_time").value;
    var arrival_time = document.getElementById("arrival_time").value;
    var total = document.getElementById("total").value;

       var jsonP=
           {"company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total,

           }



     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.141:5016/api/registrar/ruta/tren',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                //beforeSend: function (xhr,) {
                   // xhr.setRequestHeader("Authorization", "Basic "
                 //       + btoa(tokenTest + ":" + password));
               // },
                success : function(result) {
                    sessionStorage.setItem("token", datos['token']);
                   alert("Regisrado con éxito");
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }

