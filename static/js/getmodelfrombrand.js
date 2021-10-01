let retreivevehicledetail = function () {
    var brandId = document.getElementById('vehicle_brand').value;
    vehicle_brand = $('#vehicle_brand option:nth-child(0)').val();
    var url = window.location.origin;
    $.ajax({
        async: false,
        method: 'GET',
        url: url + '/rental/brand/getModelFromBrand',
        data: {'brandId': brandId},
        dataType: 'json',
        success: function (data) {
            console.log('success from select Brand');
            var ParsedData = JSON.parse(data);
            $('#vehicle_detail').empty();
            $.each(ParsedData, function (i, obj) {

                $('#vehicle_detail').append($('<option>').text(obj.fields.model).attr('value', obj.pk));
            });
        }
    }).done((result) => {
        console.log("------done------");
    }).fail((error) => {
        console.log("------fail------");
        console.log(error);
    });

}

$(document).ready(function () {
    // document is loaded and DOM is ready
    var brandId = document.getElementById('vehicle_brand').value;
    if (document.getElementById('vehicle_brand')) {
        alert(brandId);
        retreivevehicledetail();
    }


});


$(document).on("change", "#vehicle_brand", function () {
    if (document.getElementById('vehicle_brand')) {
        retreivevehicledetail();
    }
});

/*

$(document).on("change", "#vehicle_brand", function () {
    if (document.getElementById('vehicle_brand')) {
        var brandId = this.value;
        var url = window.location.origin;
        $.ajax({
            async: false,
            method: 'GET',
            url: url + '/rental/brand/getModelFromBrand',
            data: {'brandId': brandId},
            dataType: 'json',
            success: function (data) {
                console.log('success from select Brand');
                var ParsedData = JSON.parse(data);
                $('#vehicle_detail').empty();
                // $('#vehicle_detail').append($('<option>').text("Select"));
                $.each(ParsedData, function (i, obj) {
                    $('#vehicle_detail').append($('<option>').text(obj.fields.model).attr('value', obj.pk));
                });
            }
        }).done((result) => {
            console.log("------done------");
        }).fail((error) => {
            console.log("------fail------");
            console.log(error);
        });
    }
});*/
