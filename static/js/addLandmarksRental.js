$(document).ready(function () {
    let formData = new FormData();
    landmarklist = [];
    hotel = document.getElementById('rental').value;
    var base_url = window.location.origin;
    final_url = base_url + '/rental/address/addlandmark/' + hotel;
    hotel = document.getElementById('rental').value;

    $('#addlandmarkk').click(function () {
        $('input[name^="name"]').each(function () {
            landmarklist.push($(this).val());
        });
        console.log('Everything ready for ajax');
        console.log('LANDMARK:' + landmarklist);
        console.log('URL:' + final_url);

        var token = '{{csrf_token}}';
        $.ajax({ // create an AJAX call...
            headers: {"X-CSRFToken": token},
            async: true,
            data: {'landmarklist': landmarklist}, // get the form data
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
            {

            }
            console.log("---failed---");
        });


    });

});