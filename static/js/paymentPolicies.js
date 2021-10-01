$(document).ready(function () {
    cardeexistsornot();
    $('.card-detail').hide();
    instance = $("input[name='available_radio']:checked").val();
    polociesexistsornotinitial(instance);

});

//converting checkbox tor radio
function cardeexistsornot() {
    $('input[name="available_radio"]').click(function () {
        fvalue = $(this).val();
        if (fvalue === 'No') {
            $('.card-detail').hide();
            $('.msg-detail').show();
            $('input[name="credit_card"]').each(function () {
                this.checked = false;
            });

        } else {
            $('.card-detail').show();
            $('.msg-detail').hide();
        }
    });
}

function polociesexistsornotinitial(instance) {
    if (instance === 'Yes') {
        $('.card-detail').show();
        $('.msg-detail').hide();
    } else {
        $('.card-detail').hide();
        $('.msg-detail').show();
    }
}

