function read()
{

    DATA = JSON.parse(localStorage.json_transport) ;
    alert(DATA);
    $.getJSON('jsondata', function(data){
        alert(data.result);
        $.each(data.Ciudades, function(key, val){
            alert(val.result)
        });
      });
}