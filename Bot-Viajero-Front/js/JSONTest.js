   //get a reference to the select element
    var $select = $('#origin');
    var $select2 = $('#destination');

    //request the JSON data and parse into the select element
    $.getJSON('Ciudades.json', function(data){

      //clear the current content of the select
      $select.html('');

      //iterate over the data and append a select option
      $.each(data.Ciudades, function(key, val){
        $select.append('<option id="' + val.id + '">' + val.Ciudad + '</option>');
        $select2.append('<option id="' + val.id + '">' + val.Ciudad + '</option>');

      })
    });