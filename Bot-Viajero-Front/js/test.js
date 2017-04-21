   var $table = $('#result_times').find("table");

    $.getJSON('Ciudades.json', function(data){

      $table.html('');

      $.each(data.Ciudades, function(key, val){
        $table.append($("<tr>"
            + "<td>"+ val.Ciudad +"</td>"
         + "<td>"+ val.Id +"</td>"
         + "<td>"+ val.Latitud +"</td>"
         + "<td>"+ val.Longitud +"</td>"
      +"</tr>"));

      })
    });
