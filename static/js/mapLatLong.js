$(document).ready(function(){
$('.map_canvas').ready(function () {
    var lat = document.getElementById("lat").value;
    var lng = document.getElementById("lng").value;
    if (lat.length == 0 && lng.length == 0) {
        lat = 27.708436852621933;
        lng = 85.32513849941404;
    }
    var myLatlng = new google.maps.LatLng(lat, lng);
    document.getElementById("lat").value = lat;
    document.getElementById("lng").value = lng;
    var myOptions = {
        zoom: 15,
        center: myLatlng,
        draggable: true,
        mapTypeId: google.maps.MapTypeId.STREET,
        mapTypeControl:false,
        fullscreenControl: false
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    var marker = new google.maps.Marker({
        map: map,
        draggable: true,
        position: myLatlng
    });
    google.maps.event.addListener(marker, 'dragend', function (event) {
            document.getElementById("lat").value = this.getPosition().lat();
            document.getElementById("lng").value = this.getPosition().lng();
        }
    );
    // Create the search box and link it to the UI element.
    var input = document.getElementById('pac-input');
    var searchBox = new google.maps.places.SearchBox(input);
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);

    // Bias the SearchBox results towards current map's viewport.
    map.addListener('bounds_changed', function () {
        searchBox.setBounds(map.getBounds());
    });
    // Clear out the old markers.

    // Listen for the event fired when the user selects a prediction and retrieve
    // more details for that place.
    searchBox.addListener('places_changed', function () {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
        }

        marker.setMap(null);
        marker = null;
        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();
        places.forEach(function (place) {
            if (!place.geometry) {
                console.log("Returned place contains no geometry");
                return;
            }

            marker = new google.maps.Marker({
                map: map,
                draggable: true,
                title: place.name,
                position: place.geometry.location
            });

            // Create a marker for each place.
            document.getElementById("lat").value = place.geometry.location.lat();
            document.getElementById("lng").value = place.geometry.location.lng();
            google.maps.event.addListener(marker, 'dragend', function (event) {
                    document.getElementById("lat").value = this.getPosition().lat();
                    document.getElementById("lng").value = this.getPosition().lng();
                }
            );
            if (place.geometry.viewport) {
                // Only geocodes have viewport.
                bounds.union(place.geometry.viewport);
            } else {
                bounds.extend(place.geometry.location);
            }
        });
        map.fitBounds(bounds);
    });


});});