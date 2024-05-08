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

window.onload = function() {
    document.getElementById('point-form').style.display = 'none'; // Hide the index field initially
    document.getElementById('generatePathBtn').addEventListener('click', function() {
        document.getElementById('point-form').style.display = 'block'; // Show the index field when the button is clicked
    });
};

function generatePath() {
    var markers = markersGroup.getLayers();
    var markersList = markers.map(function(marker) {
        return marker.getLatLng();
    });

    // Clear previous content of the container
    var container = document.getElementById('point-form');
    container.innerHTML = '';

    // Fetch and append the add_point_form.html content for each marker
    markersList.forEach(function(point, index) {
        var url = '/add-adventure/add-point';  // Use the correct URL pattern

        // Perform the AJAX request
        fetch(url)
            .then(response => response.text())  // Convert response to text
            .then(html => {
                // Create a temporary div element to hold the HTML content
                var tempDiv = document.createElement('div');
                tempDiv.innerHTML = html;

                // Populate latitude and longitude fields in the form
                var latitudeField = tempDiv.querySelector('#id_latitude');
                var longitudeField = tempDiv.querySelector('#id_longitude');
                var indexField = tempDiv.querySelector('#index');
                if (latitudeField && longitudeField && indexField) {
                    latitudeField.value = point.lat;
                    longitudeField.value = point.lng;
                    indexField.value = index + 1; // Index starts from 1
                }

                // Append the content to the container
                container.appendChild(tempDiv.firstChild);
            })
            .catch(error => {
                console.error('Error fetching add_point_form.html:', error);
            });
    });
    container.style.display = 'block';
}


function displayFormInfo() {
    // Select all the forms on the page
    var forms = document.querySelectorAll('form');

    // Iterate over each form
    forms.forEach(function(form, index) {
        // Create a container to display the form information
        var formInfoContainer = document.createElement('div');
        formInfoContainer.classList.add('form-info');

        // Get the form data
        var formData = new FormData(form);

        // Create a paragraph element to display the form data
        var formInfoParagraph = document.createElement('p');
        formInfoParagraph.textContent = 'Form ' + (index + 1) + ' data: ';

        // Iterate over each form field and append its data to the paragraph
        formData.forEach(function(value, key) {
            formInfoParagraph.textContent += key + ': ' + value + ', ';
        });

        // Append the paragraph to the form info container
        formInfoContainer.appendChild(formInfoParagraph);

        // Append the form info container to the body
        document.body.appendChild(formInfoContainer);
    });
}

function addAdventure() {
    var routeForm = document.getElementById('route-form');
    console.log(routeForm)
    var forms = document.querySelectorAll('point-form');
    console.log(forms)
    // get these variables to addAdventure view and handle them there
}




// function generatePath() {
//     var markers = markersGroup.getLayers();
//     var markersList = markers.map(function(marker) {
//         return marker.getLatLng();
//     });

//     // AJAX request to fetch add_point_form.html and append it for each marker
//     // markersList.forEach(function(point, index) {
//     //     var url = '/add-adventure/add-point';  // Use the correct URL pattern
//     //     var container = document.getElementById('point-form');

//     //     // Perform the Htmx request
//     //     container.hxGet(url, {
//     //         target: container,
//     //         params: {},
//     //         spinner: 'dots',
//     //         historyUpdate: 'replace',
//     //         headers: {}
//     //     });
//     // });
//     var container = document.getElementById('point-form');
//     container.innerHTML = '';
//     // markersList.forEach(function(point, index) {
//     //     var helloWorldElement = document.createElement('div');
//     //     helloWorldElement.textContent = 'Hello World';
//     //     container.appendChild(helloWorldElement);
//     // });
//     markersList.forEach(function(point, index) {
//         var url = '/add-adventure/add-point';  // Use the correct URL pattern

//         // Perform the AJAX request
//         fetch(url)
//             .then(response => response.text())  // Convert response to text
//             .then(html => {
//                 // Create a temporary div element to hold the HTML content
//                 var tempDiv = document.createElement('div');
//                 tempDiv.innerHTML = html;

//                 // Append the content to the container
//                 container.appendChild(tempDiv.firstChild);
//             })
//             .catch(error => {
//                 console.error('Error fetching add_point_form.html:', error);
//             });
//     });
// }

    // // Display List of Points
    // var pointListDiv = document.getElementById('pointList');
    // pointListDiv.innerHTML = ''; // Clear previous list
    // markersList.forEach(function(point, index) {
    //     var newPointListItem = document.createElement('div');
    //     newPointListItem.textContent = 'Point ' + (index + 1) + ': Latitude: ' + point.lat + ', Longitude: ' + point.lng;
    //     pointListDiv.appendChild(newPointListItem);
    // });

