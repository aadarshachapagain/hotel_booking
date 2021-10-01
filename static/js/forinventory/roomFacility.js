$(document).ready(function () {
    featureexistsornot();
    freeorpaid();
    $('.feature-detail').hide();
    $("input.pre_selected[name='available_checkbox']").each(function () {
        featureexistsornotinitial($(this));
    });
});

//converting checkbox tor radio
function featureexistsornot() {
    $('input[name="available_checkbox"]').click(function () {
        fvalue = $(this).val();
        if (fvalue === 'No') {
            $(this).parents().eq(6).children().eq(3).hide();
            $(this).parents().eq(6).children().eq(3).children().eq(1).children().eq(0).children().eq(1).val('');
            $(this).parents().eq(2).children().eq(0).children().children().prop('checked', false);
        } else {
            $(this).parents().eq(6).children().eq(3).show();
            $(this).parents().eq(2).children().eq(1).children().children().prop('checked', false);
        }
    });
}

function featureexistsornotinitial(instance) {
    if (instance.val() === 'Yes') {
        instance.parents().eq(6).children().eq(3).show();
    } else {

    }
}

//converting checkbox tor radio
function freeorpaid() {
    $('input[name="price_checkbox"]').click(function () {
        fvalue = $(this).val();
        if (fvalue === 'Paid') {
            $(this).parents().eq(2).children().eq(0).children().children().prop('checked', false);
        } else {
            $(this).parents().eq(2).children().eq(1).children().children().prop('checked', false);
        }
    });
}