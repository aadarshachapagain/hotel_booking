$(document).ready(function () {
    featureslist = [];
    featureflag = false;
    var base_url = window.location.origin;
    url_add_features = base_url + '/hotel/api/addnewfeatures/';

    // {#To get  existing Feature#}
    $("#fetchfeature").click(function () {
        var base_url = window.location.origin;
        urlgetrmfeatures = base_url + '/hotel/api/getrooomfeatures'
        var token = '{{csrf_token}}';
        new Vue({
            el: '#app',
            delimiters: ['[[', ']]'],
            data() {
                return {
                    info: null,
                    featurelist: [],

                }
            },
            mounted() {
                axios
                    .get(urlgetrmfeatures)
                    .then(response => {
                        this.featurelist = response.data.maindict.RoomFeatures;
                    })
            }
        })
    });
    // {#To get  existing Feature#}

    // {#To add New Feature#}
    $('#addfeature').click(function () {
        $('input[name^="newfeatures"]').each(function () {
            featureslist.push($(this).val());
        });
        // var token = csrf_token;
        var token = getCookie('csrftoken');
        console.log('token');
        console.log(token);
        $.ajax({ // create an AJAX call...
            headers: {"X-CSRFToken": token},
            async: true,
            data: {'featureslist': featureslist}, // get the form data
            type: 'POST', // GET or POST
            url: url_add_features, // the file to call
            // {#processData: false, // IMPORTANT: Without this, ajax will not send Data object correctly#}
            // {#contentType: false,#}
            dataType: 'json',
            success: function (response) {
                featurearray = response.updatedlist;
                // console.log('featurearray:'+featurearray);
                $("#app").empty();
                featurearray.map(fa => {
                    $("#app").append('<p><input class="checkbox_room_feature input-check" name="roomfeature_id" type="checkbox" value=' + fa.id + '>' + fa.name + '</p>');
                })
            }
        }).done((result) => {
            console.log('result:');
            console.log('--done--')

        }).fail((error) => {
            console.log(error);
            console.log("---failed---");
        });

        $('#newrmfeatures').hide();
    });
    // {#To add New Feature#}

    // {#To Clone field#}


    $('#newrmfeatures').hide();

    $('.multi-field-wrapper').each(function () {
        var $wrapper = $('.multi-fields', this);
        $(".add-field", $(this)).click(function (e) {
            var a = $('.multi-field:first-child', $wrapper).clone(true).appendTo($wrapper).find('textarea').val("");
        });

        $('.multi-field .remove-field', $wrapper).click(function () {
            if ($('.multi-field', $wrapper).length > 1)
                $(this).parent('.multi-field').remove();
        });
    });

    $("#more-rm-features").click(function () {
        featureflag = !featureflag;
        if (featureflag) {
            $('#newrmfeatures').show();
        } else {
            $('#newrmfeatures').hide();
        }
    });
    // {#To Clone field#}
});
