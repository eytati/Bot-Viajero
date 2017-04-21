    var $select = $('#origin');
    var $select2 = $('#destination');

    $.getJSON('Ciudades.json', function(data){

      $select.html('');

      $.each(data.Ciudades, function(key, val){
        $select.append('<option id="' + val.id + '" class="opt2">' + val.Ciudad + '</option>');
        $select2.append('<option id="' + val.id + '">' + val.Ciudad + '</option>');

      })
    });