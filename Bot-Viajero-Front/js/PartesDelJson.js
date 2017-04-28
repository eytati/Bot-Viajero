function read()
{

    var DATA = localStorage.json_transport;
    alert(DATA);
    var json = JSON.parse(DATA);
    alert(json.Valores);
    var json_2 = json.Valores[1].Distancia;
    alert(json_2);

    //var  juan = JSON.parse(json);
    //alert(juan.Transport[0]);
    //for (var i = 0; i < DATA.length; i++) {

    //alert(DATA.Valores[0].Transport);
    //}
    //alert(DATA);
    // $.each(DATA,function(key, val){
      //  alert(val.Transport);
//      });


    //alert(DATA);
    //alert(DATA[1].Valores);


  // alert(obj.Data);
}