function selectAll() {
    $('.select_all').on('click', function () {
        if (this.checked) {
            $('.meroTable tr td label input[type="checkbox"]').each(function () {
                this.checked = true;
            });
        } else {
            $('.meroTable tr td label input[type="checkbox"]').each(function () {
                this.checked = false;
            });
        }
    });

    $('.meroTable tr td label input[type="checkbox"]').on('click', function () {
        if ($('.meroTable tr td label input[type="checkbox"]:checked').length == $('.meroTable tr td label input[type="checkbox"]').length) {
            $('.select_all').prop('checked', true);
        } else {
            $('.select_all').prop('checked', false);
        }
    });
};

function initialSelect(instance) {
    fvalue = instance.val();
    let limit = 2;
    let $all_available_checkbox = $('input[name="available_checkbox"][value="Yes"]:checked');
    if (fvalue === 'No') {
        instance.prop('disabled', true);
        instance.parents().eq(6).children().last().hide();
        instance.parents().eq(6).children().eq(3).children().eq(1).children().eq(0).children().eq(1).val('');
        instance.parents().eq(2).children().eq(0).children().children().prop('checked', false);
        instance.parents().eq(2).children().eq(0).children().children().prop('disabled', false);
        if ($all_available_checkbox.length!== limit) {
            $('.custom-fieldset').attr('style', 'filter: blur(0px);');
        }
    } else {
        instance.prop('disabled', true);
        let $price = instance.parents().eq(6).children().last().children().eq(0).children().eq(0);
        let $rate = $price.find('input[name="rate"]').val();
        $rate = parseFloat($rate);
        let $operator = $price.find('input[name="operator"]').val();
        let $price_tr = $price.children().last().children().eq(0);
        $price_tr.find('tr').each(function () {
            let $price_const = $(this).children().first().children().eq(0).val();
            let $price_amount_instance = $(this).children().last().children().eq(0);
            if ($operator === 'sub') {
                let temp = parseFloat($price_const) - (($rate * parseFloat($price_const)) / 100);
                $price_amount_instance.html(temp);
            } else if ($operator === 'add') {
                let temp = parseFloat($price_const) + (($rate * parseFloat($price_const)) / 100);
                $price_amount_instance.html(temp);
            } else {
            }
        });
        instance.parents().eq(6).children().last().show();
        instance.parents().eq(2).children().eq(1).children().children().prop('checked', false);
        instance.parents().eq(2).children().eq(1).children().children().prop('disabled', false);
        console.log($all_available_checkbox.length);
        if ($all_available_checkbox.length === limit) {
            let $not_available_checkbox = $('input[name="available_checkbox"]');
            $not_available_checkbox.each(function () {
                if ($(this)[0].value === 'No' && $(this)[0].checked === true) {
                    console.log('inside');
                    console.log($(this).parents().eq(6));
                    $(this).attr('disabled', true);
                    $(this).parents().eq(6).attr('style', 'filter: blur(2px);background-color: #fbfbfb;');
                }
            })
        }

    }
}
//converting checkbox tor radio
function policy_accepted_or_not() {
    $('input[name="available_checkbox"]').click(function () {
        fvalue = $(this).val();
        let limit = 2;
        let $all_available_checkbox = $('input[name="available_checkbox"][value="Yes"]:checked');
        if (fvalue === 'No') {
            $(this).prop('disabled', true);
            $(this).parents().eq(6).children().last().hide();
            $(this).parents().eq(6).children().eq(3).children().eq(1).children().eq(0).children().eq(1).val('');
            $(this).parents().eq(2).children().eq(0).children().children().prop('checked', false);
            $(this).parents().eq(2).children().eq(0).children().children().prop('disabled', false);
            if ($all_available_checkbox.length -1 !== limit) {
                $('.custom-fieldset').attr('style', 'filter: blur(0px);');
            }
        } else {
            if ($all_available_checkbox.length <= limit) {
                $(this).prop('disabled', true);
                let $price = $(this).parents().eq(6).children().last().children().eq(0).children().eq(0);
                let $rate = $price.find('input[name="rate"]').val();
                $rate = parseFloat($rate);
                let $operator = $price.find('input[name="operator"]').val();
                let $price_tr = $price.children().last().children().eq(0);
                $price_tr.find('tr').each(function () {
                    let $price_const = $(this).children().first().children().eq(0).val();
                    let $price_amount_instance = $(this).children().last().children().eq(0);
                    if ($operator === 'sub') {
                        let temp = parseFloat($price_const) - (($rate * parseFloat($price_const)) / 100);
                        $price_amount_instance.html(temp.toFixed(2));
                    } else if ($operator === 'add') {
                        let temp = parseFloat($price_const) + (($rate * parseFloat($price_const)) / 100);
                        $price_amount_instance.html(temp.toFixed(2));
                    } else {
                    }
                });
                $(this).parents().eq(6).children().last().show();
                $(this).parents().eq(2).children().eq(1).children().children().prop('checked', false);
                $(this).parents().eq(2).children().eq(1).children().children().prop('disabled', false);
                if ($all_available_checkbox.length === limit) {
                    let $not_available_checkbox = $('input[name="available_checkbox"]');
                    $not_available_checkbox.each(function () {
                         if ($(this)[0].value === 'No' && $(this)[0].checked === true)
                         {
                             $(this).attr('disabled', true);
                             $(this).parents().eq(6).attr('style', 'filter: blur(2px);background-color: #fbfbfb;');
                         }
                    })
                }

            } else {
                $(this).prop('checked', false);
            }
        }

    });
}

function date_wise_filter() {
    $('input[name="date_checkbox"]').click(function () {
        let check_value = $(this).val();
        if (check_value === 'No') {
            $(this).prop('disabled', true);
            $(this).parents().eq(6).children().last().hide();
            $(this).parents().eq(6).children().last().find('input[type="text"]').prop('value', '');
            $(this).parents().eq(2).children().eq(0).children().children().prop('checked', false);
            $(this).parents().eq(2).children().eq(0).children().children().prop('disabled', false);
        } else {
            $(this).prop('disabled', true);
            $(this).parents().eq(6).children().last().show();
            $(this).parents().eq(2).children().eq(1).children().children().prop('checked', false);
            $(this).parents().eq(2).children().eq(1).children().children().prop('disabled', false);
        }
    });
}

$(document).ready(function () {
    $('.feature-detail').hide();
    $('input[name="available_checkbox"]:checked').each(function () {
        initialSelect($(this));
    });

    selectAll();
    policy_accepted_or_not();
    date_wise_filter();
    //disabled checkboxes are not submitted via POST method
    $( "form" ).submit(function( ) {
        $('input[name="available_checkbox"]').each(function () {
            $(this).prop('disabled', false)
        })
    });
});