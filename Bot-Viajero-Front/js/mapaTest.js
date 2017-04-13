/**
 * Created by hunterz on 4/11/17.
 */
/*$('#packageDestino').empty();

var json=[{value:'1', text:'Option1'},
     {value:'2', text:'Option2'},
     {value:'3', text:'Option3'}];

//var options=$('<select/>');
    $.each(json, function (id,value) {
        $('#packageDestino')
            .append($('<option><option/>')
            .attr("value", id)
            .text(value));
    });*/

   // $('#packageDestino').html(options.html());
alert('hola')
var words = ["a",
    "able",
    "about",
    "account",
    "acid",
    "across",
    "act",
    "addition"]
   $(document).ready(function () {
        $.getJSON("words-small.json", function (result) {
            $.each(result, function (i, words) {
                $(".selectbox").append("<option>"+words+"</option>");
            });
        });
    });