$(".bed_radio").change(function () {
    var radextrabed = $('input[name=extra_bed]:checked').val();
    if (radextrabed === 'True') {
        $(".showforextrabed").show();
        $('input[name="no_of_extra_bed"]').attr('value', 1);
    } else {
        $(".showforextrabed").hide();
        $('input[name="no_of_extra_bed"]').attr('value', 0);
    }
});

$(".crib_radio").change(function () {
    var radextracrib = $('input[name=extra_crib]:checked').val();
    if (radextracrib === 'True') {
        $(".showforextracrib").show();
        $('input[name="no_of_extra_crib"]').attr('value', 1);
    } else {
        $(".showforextracrib").hide();
        $('input[name="no_of_extra_crib"]').attr('value', 0);
    }
});

$(".rate_radio").change(function () {
    var offer_low_rate = $('input[name=rate_radio]:checked').val();
    if (offer_low_rate === 'True') {
        $(".offerlowrate").show();
    } else {
        $(".offerlowrate").hide();
    }
});

$(document).ready(function () {
    $(".showforextrabed").hide();
    $('input[name="no_of_extra_bed"]').attr('value', 0);
    $(".showforextracrib").hide();
    $('input[name="no_of_extra_crib"]').attr('value', 0);
    $(".offerlowrate").hide();
});
