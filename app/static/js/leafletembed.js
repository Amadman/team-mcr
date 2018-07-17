var map;

function initmap()
{
    var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 20, attribution: osmAttrib});

    var schools = new L.GeoJSON.AJAX(school_file);
    
    map = new L.Map('map');

    map.setView(new L.LatLng(4.624, -74.063), 8);
    map.addLayer(osm);
    map.addLayer(schools);
};
