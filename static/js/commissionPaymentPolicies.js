$(document).ready(function () {
    cardeexistsornot();
    $('.alternative-address-detail').hide();
    instance = $("input[name='address_radio']:checked").val();
    polociesexistsornotinitial(instance);
});

//converting checkbox tor radio
function cardeexistsornot() {
    $('input[name="address_radio"]').click(function () {
        fvalue = $(this).val();
        if (fvalue === 'Yes') {
            $('.alternative-address-detail').hide();
            $('input[name="alternative_address"]').attr({'value': '', 'required':false});

        } else {
            $('.alternative-address-detail').show();
            $('input[name="alternative_address"]').attr({'required':true});
        }
    });
}

function polociesexistsornotinitial(instance) {
     if (instance === 'No') {
        $('.alternative-address-detail').show();
    } else {
        $('.alternative-address-detail').hide();
    }
}

