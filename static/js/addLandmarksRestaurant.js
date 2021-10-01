$(document).ready(function () {
    let formData = new FormData();
    landmarklist = [];
    hotel = document.getElementById('company').value;
    var base_url = window.location.origin;
    final_url = base_url + '/restaurant/address/addlandmark/' + hotel;
    hotel = document.getElementById('company').value;
    // landmarks=[];

    $('#addlandmarkk').click(function () {
        $('input[name^="name"]').each(function () {
            landmarklist.push($(this).val());
        });
        // $('[name="landmarks"]').each(function () {
        //     landmarks.push($(this).val());
        // });
         landmarks = $("[name='landmarks']").val();
        landmarkname=document.getElementById('landmarkname').value;
        lat_landmark = document.getElementById('lat_landmark').value;
        lng_landmark = document.getElementById('lng_landmark').value;


        console.log('Everything ready for ajax');
        console.log('LANDMARK:'+landmarkname+lat_landmark+lng_landmark);
        console.log('URL:' + final_url);
        console.log('lad'+landmarks);

        var token = '{{csrf_token}}';
        $.ajax({ // create an AJAX call...
            headers: {"X-CSRFToken": token},
            async: true,
            data: {'landmarks':landmarks,'landmarklist': landmarklist,'landmarkname':landmarkname, 'lat_landmark': lat_landmark, 'lng_landmark': lng_landmark}, // get the form data
            type: 'POST', // GET or POST
            url: final_url, // the file to call
            dataType: 'json',
            success: function (response) { // on success..

                var opts = response;
                $('#landmarks').empty();
                $.each(opts, function (i, d) {
                    var a = '<option  selected value="' + d.id + '">' + d.name + '</option>';
                    // You will need to alter the below to get the right values from your json object.  Guessing that d.id / d.modelName are columns in your carModels data

                    $('#landmarks').append(a);
                });
                $('#newlandmark').hide();

            }
        }).done((result) => {
            console.log('result:');
            console.log('--done--')

        }).fail((error) => {

            console.log("---failed---");
        });


    });

});