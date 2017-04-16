var tokenTest = sessionStorage.getItem("tokenTest");

    alert("Hola");
function SelectJsonBus() {
    var jsonData = {
      "Table": [{
        //"id" : 1,
      "ciudad" : "La Fortuna",
      "latitude" : 10.4678335,
      "longitude" : -84.64268060000001
      }, {
        //  "id" : 2,
      "ciudad" : "Quepos",
      "latitude" : 9.431868099999999,
      "longitude" : -84.1619076
      }, {
      //"id" : 3,
      "ciudad" : "Monte Verde",
      "latitude" : 10.2749682,
      "longitude" : -84.8255097
      }, {
         //"id" : 4,
      "ciudad" : "Tortuguero",
      "latitude" : 10.5424838,
      "longitude" : -83.50235520000001
      }, {
         //"id" : 5,
      "ciudad" : "Puerto Jiménez",
      "latitude" : 8.5336439,
      "longitude" : -83.30678019999999
      },
      {
        // "id" : 6,
      "ciudad" : "Liberia",
      "latitude" : 10.6345964,
      "longitude" : -85.44067469999999
      },
      {
      //"id" : 7,
      "ciudad" : "Cantón de Alajuela",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
           {
      //"id" : 8,
      "ciudad" : "Volcán Miravalles",
      "latitude" : 10.0525756,
      "longitude" : -84.20679919999998
    },
           {
      //"id" : 9,
      "ciudad" : "Sarapiquí",
      "latitude" : 10.473523,
      "longitude" : -84.01674229999998
    },
          {
      //"id" : 10,
      "ciudad" : "Cahuita",
      "latitude" : 9.7347856,
      "longitude" : -82.84521459999996
    },
          {
      //"id" : 11,
      "ciudad" : "Bagaces",
      "latitude" : 10.5388321,
      "longitude" : -85.25413600000002
    },
           {
      //"id" : 12,
      "ciudad" : "Irazú",
      "latitude" : 9.9799813,
      "longitude" : -85.23084140000003
    },
            {
      //"id" : 13,
      "ciudad" : "Pérez Zeledón",
      "latitude" : 9.35473,
      "longitude" : -83.63484299999999
    },
           {
      //"id" : 14,
      "ciudad" : "Uvita",
      "latitude" : 9.163500899999999,
      "longitude" : -83.7358514
    },
          {
      //"id" : 15,
      "ciudad" : "Cartago",
      "latitude" : 9.8638091,
      "longitude" : -83.91619349999996
    },
           {
      //"id" : 16,
      "ciudad" : "Volcán Tenorio",
      "latitude" : 10.6713889,
      "longitude" : -85.01249999999999
    },
    {
      //"id" : 17,
      "ciudad" : "Turrialba",
      "latitude" : 9.9067054,
      "longitude" : -83.68005119999998
    },
    {
      //"id" : 18,
      "ciudad" : "Parque Nacional Chirripó",
      "latitude" : 9.5134327,
      "longitude" : -83.4946218
    },
    {
      //"id" : 19,
      "ciudad" : "Península de Santa Elena",
      "latitude" : 10.8841185,
      "longitude" : -85.78716630000002
    },
              {
     // "id" : 20,
      "ciudad" : "Parque Internacional La Amistad",
      "latitude" : 9.4071,
      "longitude" : -82.93880000000001
    },
    {
     // "id" : 21,
      "ciudad" : "Talamanca",
      "latitude" : 9.6540146,
      "longitude" : -84.08309109999999
    },
    {
    //  "id" : 22,
      "ciudad" : "Los Chiles",
      "latitude" : 11.0336891,
      "longitude" : -82.75494119999996
    },
    {
      //"id" : 23,
      "ciudad" : "Parque Nacional Braulio Carrillo",
      "latitude" : 10.1599,
      "longitude" : -83.974425
    },
    {
     // "id" : 24,
      "ciudad" : "Nicoya",
      "latitude" : 10.1445678,
      "longitude" : -85.45302950000001
    }
    ]

  };

     $(document).ready(function () {
         var listItems = '<option selected="selected" value="">- Seleccione lugar -</option>';

      for (var i = 0; i < jsonData.Table.length; i++) {
             listItems += "<option value='"+jsonData.Table[i].ciudad + "'>" + jsonData.Table[i].ciudad  +"</option>";

         }

         $("#origin").html(listItems);
         $("#destination").html(listItems);

     });
}

function registro_Bus() {
    var company = document.getElementById("company").value;
    var registration = document.getElementById("registration").value;
    var name = document.getElementById("name").value;
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;
    var passengers = document.getElementById("passengers").value;
    var departure_time= document.getElementById("departure_time").value;
    var arrival_time= document.getElementById("arrival_time");
    var total = document.getElementById("total").value;

       /* var json_data=
            {
           "companyname": "TicaBus",
           "registration": "67281",
           "name": "Luis",
           "origin": "Cartago",
           "destination": "Turrialba",
           "passengers": 50,
           "total": 3000
    }*/

       var jsonP=
           {
           "companyname": company,
           "registration": registration,
           "name": name,
           "origin": origin,
           "destination": destination,
           "passengers": passengers,
           "departure_time": departure_time,
           "arrival_time":arrival_time,
           "total": total

           }

     var data = JSON.stringify(jsonP);
      //alert(data)
            $.ajax({
                type: 'POST',
                url: 'http://192.168.1.140:5016/api/registrar/ruta/bus',
                contentType:"application/json",
                data: data,
                dataType: 'json',
                 //beforeSend: function (header,) {
                   // xhr.setRequestHeader("Authorization", "Basic "
                     //   + btoa(tokenTest + ":" + password));
                //},
                success : function(result) {
                    alert("Regisrado con éxito")
                 window.location.href="Index.html"

    },           error: function(error){
                 alert(error);
}
            })
        }

