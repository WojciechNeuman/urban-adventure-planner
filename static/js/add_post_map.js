var map = L.map('map').setView([51.505, -0.09], 13);
var markersGroup = L.layerGroup().addTo(map);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function toggleButtonState(state) {
    var button = document.getElementById('generatePathBtn');
    button.disabled = !state;
}

map.on('click', function(e) {
    var markerIndex = markersGroup.getLayers().length + 1; // Get the length of markersGroup and increment to get the index
    var marker = L.marker(e.latlng).addTo(markersGroup);
    marker.bindPopup('<b>' + markerIndex + '</b>').openPopup(); // Display marker index as popup
    toggleButtonState(true);

    // Fill Latitude and Longitude fields
    var latitudeInput = document.getElementById('latitude');
    var longitudeInput = document.getElementById('longitude');
    latitudeInput.value = e.latlng.lat;
    longitudeInput.value = e.latlng.lng;

    // Fill Point Description field
    var pointDescriptionInput = document.getElementById('pointDescription');
    pointDescriptionInput.value = ''; // Clear previous value

    // Find the first free row of the form and fill it with marker data
    var form = document.getElementById('pointForm');
    var rows = form.querySelectorAll('.form-row');
    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].querySelectorAll('input');
        if (!inputs[0].value) { // Check if the first input field is empty
            inputs[0].value = e.latlng.lat;
            inputs[1].value = e.latlng.lng;
            inputs[2].value = ''; // Clear previous value
            break; // Exit the loop after filling the first free row
        }
    }
}); 


function generatePath() {
    var markers = markersGroup.getLayers();
    var markersList = markers.map(function(marker) {
        return marker.getLatLng();
    });

    // Display List of Points
    var pointListDiv = document.getElementById('pointList');
    pointListDiv.innerHTML = ''; // Clear previous list
    markersList.forEach(function(point, index) {
        var newPointListItem = document.createElement('div');
        newPointListItem.textContent = 'Point ' + (index + 1) + ': Latitude: ' + point.lat + ', Longitude: ' + point.lng;
        pointListDiv.appendChild(newPointListItem);
    });
}
