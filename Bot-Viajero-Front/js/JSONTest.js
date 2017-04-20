alert("Hola")
$.ajax({
    type: 'GET',
    url: "http://192.168.1.141:5016/api/ciudades",
    data: "format=json&id=123",
    dataType: 'jsonp',
    success: function x(feed) {
        document.write(feed);
        alert(feed);
    },
    error: function y(error) {
        alert(error + "Error");
    }
});