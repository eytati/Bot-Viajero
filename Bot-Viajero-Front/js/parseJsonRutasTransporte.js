function read()
{
   // var td = $('#table1');

    var DATA = localStorage.json_transport;
    alert(DATA);
    var json = JSON.parse(DATA);
    var imp= json.Valores;
    alert(json.Valores);

    var news = document.getElementsByClassName("news-story")[0];
    var Valores = imp
    for(var i = 0; i < Valores.length; i++) {

    var h5 = document.createElement("h5");
    h5.innerHTML = Valores[i];
    news.appendChild(h5);
    var p = document.createElement("p");
    p.innerHTML = Valores[i].Ciudad;
    news.appendChild(p);

}
   // document.body.innerHTML=imp;
    //var json_3 = JSON.parse(json_2);
    //alert(json_3.Distancia);

    //for (var i = 0; i < json.Valores.length; i++)
    //{
      //  var json_2 = json.Valores[i];
        //if(json_2 != null)
        //{

         //   rows += "</td><td>" + gender + "</td><td>" + age + "</td><td>" + city + "</td></tr>"
        //}
        //alert(json_2);
   // }
    //var  juan = JSON.parse(json);
    //alert(juan.Transport[0]);
    //{

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