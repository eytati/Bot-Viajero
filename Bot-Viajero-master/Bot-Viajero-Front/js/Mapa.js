(function(window, mapa){

    var Mapa = (function() {
        function Mapa(element, opts) {
            this.gMap = new google.maps.Map(element, opts)
        }
        Mapa.prototype = {
            zoom: function(level){
                if(level){
                    this.gMap.setZoom(level)
                } else{
                    return this.gMap.getZoom();
                }
            },

            _on: function(event, callback){
                google.maps.event.addListener(this.gMap, event, callback);
            },
            addMarker: function(opts){
                opts.position = {
                    lat: opts.lat,
                    lng: opts.lng
                }
                marker = this._newMarker(opts)


                return marker;
            },
            _newMarker: function(opts){
                opts.map = this.gMap;
                return new google.maps.Marker(opts);
            }
        };
        return Mapa;
    }());

    Mapa.create = function(element, opts){
        return new Mapa(element, opts);
    };

    window.Mapa = Mapa;

}(window, window.Mapa))
