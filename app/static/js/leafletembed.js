var map;
var socket;

function initmap()
{
    socket = io.connect('http://' + document.domain + ':' + location.port);

    var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = L.tileLayer(osmUrl, {minZoom: 1, maxZoom: 22, attribution: osmAttrib});
    var realtime;

    var latLng = L.latLng(4.624, -74.063)

    function update(e) {
        console.log("Got an update!")
        realtime.update(JSON.parse(e));
    }

    function remove(e) {
        realtime.remove(JSON.parse(e.data));
    }

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
        map = L.map('map', {center: latLng, zoom: 13, maxZoom: 22, layers: [osm]}),
            realtime = L.realtime(undefined, {
                container: marker,
                getFeatureId: function(f) { return f.geometry.coordinates[0]+f.geometry.coordinates[1]; },
                start: false
            }).addTo(map);
        map.addLayer(healthCluster);
        realtime.on('update', function(e) {
            marker = L.markerClusterGroup({chunkedLoading: true});
            var popupContent = function(fId) {
                var feature = e.features[fId];
                // return feature.properties.name
                return "TODO: replace admin_id with name"
            };
            bindFeaturePopup = function(fId) {
                realtime.getLayer(fId).bindPopup(popupContent(fId));
            },
                updateFeaturePopup = function(fId) {
                    realtime.getLayer(fId).getPopup().setContent(popupContent(fId));
                },
                bindMarker = function(fId) {
                    marker.addLayer(realtime.getLayer(fId));
                };

            Object.keys(e.enter).forEach(bindFeaturePopup);
            Object.keys(e.enter).forEach(bindMarker);
            Object.keys(e.update).forEach(updateFeaturePopup);
        });
    })


    /*
    var schools = L.geoJSON.ajax("static/data/schools.json",{
        onEachFeature: function(feature, layer) {
            layer.bindPopup(feature.properties.name);
        },
    });

    var marker = L.markerClusterGroup({chunkedLoading: true});
    schools.on('data:loaded', function(e){
        async(function() {marker.addLayer(schools)}, null);
        map.addLayer(marker);
    });
    */

    socket.on('connect', function() {
        socket.emit('event', {data: 'Connected!'});
    });
    socket.on('data', function(e) {
        update(e);
    });

}

function async(run_function, callback) {
    setTimeout(function() {
        run_function();
        if (callback) {callback();}
    }, 500);
}
