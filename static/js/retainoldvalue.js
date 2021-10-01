let retainoldvalue = function () {

    var drivertype = document.getElementById('hidden_drivertype').value;
    if (drivertype != '') {
        $("#driver_type").val(drivertype).change();
    }
    var insurancetype = document.getElementById('hidden_insurance').value;
    if (insurancetype != '') {
        $("#insurance_type").val(insurancetype).change();
    }

    // Retrieve selected value of radio button
    var bootavailable = document.getElementById('vehiclebooty').value;
    // {#$("input[name=vehicle_boot][value=" + bootavailable + "]").prop('checked', true);#}


    // {#$("#vehicle_detail").val(vehicledetailid).change();#}
    if (document.getElementById('hidden_car_group')) {
        var hidden_car_group = document.getElementById('hidden_car_group').value;
        if (hidden_car_group != '') {
            $("#car_group").val(hidden_car_group).change();
        }
    }
    if (document.getElementById('hidden_drivertype')) {
        var drivertype = document.getElementById('hidden_drivertype').value;
        if (drivertype != '') {
            $("#driver_type").val(drivertype).change();
        }
    }

    var insurancetype = document.getElementById('hidden_insurance').value;
    if (insurancetype != '') {
        $("#insurance_type").val(insurancetype).change();
    }

    if (document.getElementById('hidden_vehicle_brand')) {
        var vehicle_brand = document.getElementById('hidden_vehicle_brand').value;
        if (vehicle_brand != '') {
            $("#vehicle_brand").val(vehicle_brand).change();
        }
    }

}