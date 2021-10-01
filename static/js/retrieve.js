let retreivebrand = function () {
    var sendvehiclecategory = document.getElementById('vehicle_category').value;
    var url = window.location.origin;
    if (sendvehiclecategory) {
        var categoryId = document.getElementById('vehicle_category').value;
        $('#vehicle_brand').empty();
        var url = window.location.origin;
        $.ajax({
            async: false,
            method: 'GET',
            url: url + '/rental/detail/getBrandFromcategory/',
            data: {'categoryId': categoryId},
            dataType: 'json',
            success: function (data) {
                var ParsedData = JSON.parse(data);
                $.each(ParsedData, function (i, obj) {

                    $('#vehicle_brand').append($('<option>').text(obj.fields.name).attr('value', obj.pk));
                });
            }
        }).done((result) => {
            console.log("------done------");
        }).fail((error) => {
            console.log("------fail------");
            console.log(error);
        });
    }
//    select model after brand is selected
         retreivevehicledetail();
//    select model after brand is selected
}

let init_retreivebrand = function () {
    retreivebrand();
    var hidden_vehicle_brand = document.getElementById('hidden_vehicle_brand').value;
    if (hidden_vehicle_brand) {
        $("#vehicle_brand").val(hidden_vehicle_brand).attr('selected', 'selected');
    }
}

$(document).ready(function () {
    init_retreivebrand();
    $('#vehicle_category').change(function () {
        retreivebrand();
    });
});


/*get model from brand*/
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
        retreivevehicledetail();
    }
});

$(document).on("change", "#vehicle_brand", function () {
    if (document.getElementById('vehicle_brand')) {
        retreivevehicledetail();
    }
});
/*get model from brand*/