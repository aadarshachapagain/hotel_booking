$(document).ready(function () {
    //need to clean this code
    var radextrabed = $('input[name=extra_bed]:checked').val();
    if (radextrabed === 'True') {
        $(".showforextrabed").show();
        $('input[name="no_of_extra_bed"]').attr('value', 1);
    } else {
        $(".showforextrabed").hide();
        $('input[name="no_of_extra_bed"]').attr('value', 0);
    }

    var radextracrib = $('input[name=extra_crib]:checked').val();
    if (radextracrib === 'True') {
        $(".showforextracrib").show();
        $('input[name="no_of_extra_crib"]').attr('value', 1);
    } else {
        $(".showforextracrib").hide();
        $('input[name="no_of_extra_crib"]').attr('value', 0);
    }
});
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

/*Low rate for child*/
$(".rate_radio").change(function () {
    var offer_low_rate = $('input[name=rate_radio]:checked').val();
    if (offer_low_rate === 'True') {
        $(".offerlowrate").show();
    } else {

        $(".offerlowrate").hide();
    }
});
/*Low rate for child*/

//
// $(".perflatchild").change(function () {
//     var percentagechecked = $('input[name=perflatchild]:checked').val();
//     if (percentagechecked == 'True') {
//         base_price = document.getElementById('price').value;
//         flatdiscount = document.getElementById('discountforchild').value;
//         discountinpercent = (flatdiscount * 100) / base_price;
//         document.getElementById('discountforchild').value = discountinpercent;
//     } else {
//         discountinpercent = document.getElementById('discountforchild').value;
//         base_price = document.getElementById('price').value;
//         flatdiscount = (discountinpercent * base_price) / 100;
//         document.getElementById('discountforchild').value = flatdiscount;
//     }
// });
//
// $(".perflatinfant").change(function () {
//     var ipercentagechecked = $('input[name=perflatinfant]:checked').val();
//     if (ipercentagechecked == 'True') {
//         ibase_price = document.getElementById('price').value;
//         iflatdiscount = document.getElementById('discountforinfant').value;
//         idiscountinpercent = (iflatdiscount * 100) / ibase_price;
//         document.getElementById('discountforinfant').value = idiscountinpercent;
//     } else {
//         idiscountinpercent = document.getElementById('discountforinfant').value;
//         ibase_price = document.getElementById('price').value;
//         iflatdiscount = (idiscountinpercent * ibase_price) / 100;
//         document.getElementById('discountforinfant').value = iflatdiscount;
//     }
// });



