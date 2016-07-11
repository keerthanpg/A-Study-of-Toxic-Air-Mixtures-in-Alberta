function initMap() {
    year = document.getElementById('year').value
    chemicalname = document.getElementById('chemicalname').value
    radius = document.getElementById('radius').value


    var Emission;
    $.getJSON("EmissionByChemicalWeb.json", function(json) {
        Emission = json;
        $.getJSON("FacilityCoordinates.json", function(json) {
            FacilityCoordinates = json;

            $.getJSON("ChemicalNumbers.json", function(json) {
                ChemicalNumbers = json;
                casno = ChemicalNumbers[chemicalname];
                console.log(casno);
                var map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 5,
                    center: { lat: 55.5, lng: -115.0 },
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                });

                for (var i = 0; i < Emission[year][casno].length; i++) {


                    emissioncentre = FacilityCoordinates[Emission[year][casno][i]['NPRI_ID']]
                        // Add the circle for this city to the map.
                    var emissionCircle = new google.maps.Circle({
                        strokeColor: '#FF0000',
                        strokeOpacity: 0.8,
                        strokeWeight: 1,
                        fillColor: '#FF0000',
                        fillOpacity: 0.35,
                        map: map,
                        center: emissioncentre,
                        radius: Math.sqrt(Emission[year][casno][i]['Tonnes_Air']) * radius,
                        clickable: true
                    });
                    createClickableCircle(map, emissionCircle, 'hi');

                }
                google.maps.event.addDomListener(window, 'load', initialize);

            });

        });

    });

}

function createClickableCircle(map, circle, info) {
    var infowindow = new google.maps.InfoWindow({
        content: info
    });
    google.maps.event.addListener(circle, 'mouseover', function(ev) {
        // alert(infowindow.content);
        infowindow.setPosition(circle.getCenter());
        infowindow.open(map);
    });
    google.maps.event.addListener(circle, 'mouseout', function(ev) {

        infowindow.close();

    });
}
