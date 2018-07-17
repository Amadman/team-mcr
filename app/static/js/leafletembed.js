var map;

function initmap()
{
    var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = L.tileLayer(osmUrl, {minZoom: 1, maxZoom: 22, attribution: osmAttrib});

    var latLng = L.latLng(4.624, -74.063)
    map = L.map('map', {center: latLng, zoom: 13, maxZoom: 22, layers: [osm]});
    var schools = L.geoJSON.ajax("static/data/schools.json",{
        onEachFeature: function(feature, layer) {
            layer.bindPopup(feature.properties.name);
        },
    });

    var marker = L.markerClusterGroup({chunkedLoading: true});
    schools.on('data:loaded', function(e){
        marker.addLayer(schools);
        map.addLayer(marker);
    });
}
