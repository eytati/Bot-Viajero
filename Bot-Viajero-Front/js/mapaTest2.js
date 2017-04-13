
function SelectJson() {
    var jsonData = {
      "Table": [{
          "stateid": "2",
          "statename": "Texas"
      }, {
          "stateid": "3",
          "statename": "Louisiana"
      }, {
          "stateid": "4",
          "statename": "California"
      }, {
          "stateid": "5",
          "statename": "Nevada"
      }, {
          "stateid": "6",
          "statename": "Massachusetts"
      }]
  };

     $(document).ready(function () {
         var listItems = '<option selected="selected" value="0">- Select -</option>';

      for (var i = 0; i < jsonData.Table.length; i++) {
             listItems += "<option value='" + jsonData.Table[i].stateid + "'>" + jsonData.Table[i].statename + "</option>";
         }

         $("#packageOrigen").html(listItems);
         $("#packageDestino").html(listItems);

     });
}