var map = L.map('map').setView([49.883300, 19.050000], 12);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

document.addEventListener("DOMContentLoaded", function() {
    // Parse the route data from the HTML
    var routeDataString = document.getElementById("route_path").textContent;
    // const data = JSON.parse(routeDataString);
    // const _polyline = data.polyline;
    // console.log(_polyline);
    // console.log(typeof _polyline);

    console.log(typeof routeDataString)
    console.log(routeDataString)
    var routeData = JSON.parse(routeDataString);

    console.log(typeof routeData)
    console.log(routeData)
    routeData = JSON.parse(routeData);
    console.log(routeData)
    var array = routeData.polyline;
    console.log(typeof routeData)
    
    // Extract polyline coordinates
    var polylineCoords = routeData.polyline;

    console.log(polylineCoords)
    
    // Initialize an array to hold LatLng objects
    var latLngs = [];
    
    // Iterate over polyline coordinates and create LatLng objects
    for (var i = 0; i < polylineCoords.length; i++) {
        var coord = polylineCoords[i];
        var latLng = L.latLng(coord[0], coord[1]); // Leaflet expects [lat, lng]
        latLngs.push(latLng);
    }
    
    // Create a polyline using the coordinates and add it to the map
    var polyline = L.polyline(latLngs, {color: 'red'}).addTo(map);
    
    // Fit the map to the bounds of the polyline
    map.fitBounds(polyline.getBounds());

    var pointsCoords = routeData.points;

    // Iterate over points coordinates and create LatLng objects
    for (var i = 0; i < pointsCoords.length; i++) {
        var pointCoord = pointsCoords[i];
        var pointLatLng = L.latLng(pointCoord[0], pointCoord[1]);
        L.marker(pointLatLng).addTo(map); // Add marker to the map
    }
});