function initMap(year, chemicalname) {
    console.log(2006)

    var Emission;
    $.getJSON("EmissionByChemical.json", function(json) {
        Emission = json;
        $.getJSON("FacilityCoordinates.json", function(json) {
            FacilityCoordinates = json;
            //content=FacilityCoordinates["0000004385"];
            //console.log(content);
            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 5,
                center: { lat: 55.5, lng: -115.0 },
                mapTypeId: google.maps.MapTypeId.ROADMAP
            });
            //console.log('hi');
            // Construct the circle for each value in citymap.
            // Note: We scale the area of the circle based on the population.
            for (var i = 0; i < Emission['2006']['630-08-0'].length; i++) {
                //console.log(Emission['2006']['630-08-0'][i]['Tonnes_Air'] * 1000000);
                emissioncentre = FacilityCoordinates[Emission['2006']['630-08-0'][i]['NPRI_ID']]
                    // Add the circle for this city to the map.
                var emissionCircle = new google.maps.Circle({
                    strokeColor: '#FF0000',
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: '#FF0000',
                    fillOpacity: 0.35,
                    map: map,
                    center: emissioncentre,
                    radius: Emission['2006']['630-08-0'][i]['Tonnes_Air'] * 15
                });

                //console.log(Emission['2006']['630-08-0'][i]['Tonnes_Air'] * 1000000);


            }

        });
        //document.write(Emission['2006']['7647-01-0'][0]['CHEM_E']);
        //content=Emission['2006']['7647-01-0'][0]['CHEM_E'];
        //window.alert(content);
    });
    // Create the map.




}
