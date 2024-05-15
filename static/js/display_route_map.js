var map = L.map('map');

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

document.addEventListener("DOMContentLoaded", function() {
    // Parse the route data from the HTML
    var routeDataString = document.getElementById("route_path").textContent;

    var routeData = JSON.parse(routeDataString);

    routeData = JSON.parse(routeData);
    
    // Extract polyline coordinates
    var polylineCoords = routeData.polyline;
    
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

    // Check if there are points available
    if (pointsCoords.length > 0) {
        // Get the coordinates of the first point
        var firstPointCoord = pointsCoords[0];
        var firstPointLatLng = L.latLng(firstPointCoord[0], firstPointCoord[1]);

        // Set the map's view to the coordinates of the first point
        map.setView(firstPointLatLng, 12);
    }

    // Iterate over points coordinates and create LatLng objects
    for (var i = 0; i < pointsCoords.length; i++) {
        var pointCoord = pointsCoords[i];
        var pointLatLng = L.latLng(pointCoord[0], pointCoord[1]);
        var marker = L.marker(pointLatLng).addTo(map); // Add marker to the map
        marker.bindPopup("Marker Index: " + i).openPopup(); // Add popup with marker index
    }
});
