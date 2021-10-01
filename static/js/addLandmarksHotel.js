$(document).ready(function () {
    let formData = new FormData();
    landmarklist = [];
    hotel = document.getElementById('hotel').value;
    var base_url = window.location.origin;
    final_url = base_url + '/hotel/address/addlandmark/' + hotel;
    hotel = document.getElementById('hotel').value;

    $('#addlandmarkk').click(function () {
        $('input[name^="name"]').each(function () {
            landmarklist.push($(this).val());
        });
        landmarkname=document.getElementById('landmarkname').value;
        lat_landmark = document.getElementById('lat_landmark').value;
        lng_landmark = document.getElementById('lng_landmark').value;


        console.log('Everything ready for ajax');
        console.log('LANDMARK:'+landmarkname+lat_landmark+lng_landmark);
        console.log('URL:' + final_url);

        var token = '{{csrf_token}}';
        $.ajax({ // create an AJAX call...
            headers: {"X-CSRFToken": token},
            async: true,
            data: {'landmarklist': landmarklist,'landmarkname':landmarkname, 'lat_landmark': lat_landmark, 'lng_landmark': lng_landmark}, // get the form data
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


 table_rows='<tr>\n' +
                            '                                <td></td>\n' +
                            '                                <td></td>\n' +
                            '                                <td>'+ elem.paymentDate+' </td>\n' +
                            '                                <td>'+ elem.paymentData_user_name +'</td>\n' +
                            '                                <td>'+ elem.paymentData_amount +'</td>\n' +
                            '                                <td>'+ elem.paymentSource +'</td>\n' +
                            '                                <td>\n' +
                            '                                    &nbsp;\n' +
                            '                                </td>\n' +
                            '                            </tr>';
                            $('#rows_here').append(table_rows)
