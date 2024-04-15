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
}); 


function generatePath() {
    var markers = markersGroup.getLayers();
    var markersList = markers.map(function(marker) {
        return marker.getLatLng();
    });

    var numMarkers = markersList.length;
    
    // AJAX request to fetch the HTML content of the partial
    $.ajax({
        url: 'templates/partials/add_point_form.html',
        method: 'GET',
        success: function(html) {
            // Append the HTML content to the container
            for (var i = 0; i < numMarkers; i++) {
                $('#point-form').append(html);
            }
        },
        error: function(xhr, status, error) {
            console.error('Error fetching partial:', error);
        }
    });
}

    // // Display List of Points
    // var pointListDiv = document.getElementById('pointList');
    // pointListDiv.innerHTML = ''; // Clear previous list
    // markersList.forEach(function(point, index) {
    //     var newPointListItem = document.createElement('div');
    //     newPointListItem.textContent = 'Point ' + (index + 1) + ': Latitude: ' + point.lat + ', Longitude: ' + point.lng;
    //     pointListDiv.appendChild(newPointListItem);
    // });

