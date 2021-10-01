let pricingoptionchange = function (flag) {
    $('#pricing_option').click(function () {
        if (flag == 1) {
            $('input[name=priceperkm]').parent().parent().show();
            $('input[name=priceperhr]').parent().parent().show();
            flag = 0;
            document.getElementById('pricing_option').innerText = 'Remove other Option';
        } else {
            $('input[name=priceperkm]').parent().parent().hide();
            $('input[name=priceperhr]').parent().parent().hide();
            flag = 1;
            document.getElementById('pricing_option').innerText = 'Add other Option';
        }
    });
    // To hide different  pricing option initially
    var priceperday = document.getElementById('priceperday');
    var priceperkm = document.getElementById('priceperkm');
    var priceperhr = document.getElementById('priceperhr');

    if (priceperkm.value == '') {
        $('input[name=priceperkm]').parent().parent().hide();
    }
    if (priceperhr.value == '') {
        $('input[name=priceperhr]').parent().parent().hide();
    }
}