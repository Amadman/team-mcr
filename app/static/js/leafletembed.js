var map;
var socket;

function initmap()
{
    socket = io.connect('http://' + document.domain + ':' + location.port);

    var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = L.tileLayer(osmUrl, {minZoom: 1, maxZoom: 22, attribution: osmAttrib});

    var latLng = L.latLng(4.624, -74.063)

    var healthIcon = new L.Icon({
      iconUrl: 'static/data/RedCross.png',
      iconSize: [32, 32],
      iconAnchor: [16, 0]
    });

    function update(e) {
        updateSchools(JSON.parse(e));
    }

    function remove(e) {
        realtime.remove(JSON.parse(e.data));
    }

    var healthCluster = L.markerClusterGroup({chunkedLoading: true});

    var health = L.shapefile("static/data/healthsites.zip", {
        pointToLayer: function (feature, latlng) {
            return L.marker(latlng, {icon: healthIcon});
        },
        onEachFeature: function(feature, layer) {
            if (feature.properties) {
                layer.bindPopup(feature.properties['name']);
            }
        }
    });
    health.on('data:loaded', function(e){
        healthCluster.addLayer(health);
        map = L.map('map', {center: latLng, zoom: 13, maxZoom: 22, layers: [osm]});
        map.addLayer(healthCluster);
    })

    var schoolCluster = new PruneClusterForLeaflet();

    var updateSchools = function(e){
        schoolCluster.RemoveMarkers();
        var addMarker = function(fId)
        {
            var geometry = e.features[fId].geometry;
            var marker = new PruneCluster.Marker(geometry.coordinates[1], geometry.coordinates[0]);
            marker.data.popup = e.features[fId].name;
            schoolCluster.RegisterMarker(marker);
        }
        Object.keys(e.features).forEach(addMarker)
        schoolCluster.ProcessView();
        map.addLayer(schoolCluster);
    }

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
