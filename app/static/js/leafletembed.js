var map;

function initmap()
{
    var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = L.tileLayer(osmUrl, {minZoom: 1, maxZoom: 22, attribution: osmAttrib});

    var latLng = L.latLng(4.624, -74.063)
    map = L.map('map', {center: latLng, zoom: 16, maxZoom: 22, layers: [osm]});
    var schools = L.geoJSON.ajax("static/data/schools.json",{
        onEachFeature: function(feature, layer) {
            layer.bindPopup(feature.properties.name);
        },
    });

    var health = L.shapefile("static/data/healthsites.zip", {
        pointToLayer: function (feature, latlng) {
           return L.circleMarker(latlng, {radius: 20, fillOpacity: 0.8, fillColor: "#ff0000"}) 
        },
        onEachFeature: function(feature, layer) {
            if (feature.properties) {
                layer.bindPopup(Object.keys(feature.properties).map(function(k) {
                    return k + ": " + feature.properties[k];
                }).join("<br />"), {
                    maxHeight: 200
                });
            }
        }
    });
    var healthCluster = L.markerClusterGroup({chunkedLoading: true});
    var marker = L.markerClusterGroup({chunkedLoading: true, chunkSize: 200});
    health.on('data:loaded', function(e){
        healthCluster.addLayer(health);
        map.addLayer(healthCluster);
    })
    schools.on('data:loaded', function(e){
        async(function() {marker.addLayer(schools)}, null);
        map.addLayer(marker);
    });
}

function async(run_function, callback) {
    setTimeout(function() {
        run_function();
        if (callback) {callback();}
    }, 500);
}
