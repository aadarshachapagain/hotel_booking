$(document).ready(function () {
    $(".myselect").select2(
        {
            placeholder: "Select",
            closeOnSelect: true,

        }
    );
    multiGenerateFunction();
    let cost = $("select[name='cost_status']");
    let temp1 = cost.parent().parent().parent();
    let priceTypeVal = cost.children(':selected').val();
    priceChangeFunction(priceTypeVal, temp1);
    priceType();

    let age = $("select[name='age_category']");
    let temp2 = age.parent().parent().parent();
    let ageTypeVal = age.children(':selected').val();
    ageChangeFunction(ageTypeVal, temp2);
    ageType();
    selectAll();
});


let init = function (a) {
    let cost = a.children().children().children("select[name='cost_status']");
    let temp1 = cost.parent().parent().parent();
    let priceTypeVal = cost.children(':selected').val();
    priceChangeFunction(priceTypeVal, temp1);

    let age = a.children().children().children("select[name='age_category']");
    let temp2 = age.parent().parent().parent();
    let ageTypeVal = age.children(':selected').val();
    ageChangeFunction(ageTypeVal, temp2);

};

let ageType = function () {
    $("select[name='age_category']").change(function () {
        let temp = $(this).parent().parent().parent();
        let ageTypeVal = $(this).children(':selected').val();
        ageChangeFunction(ageTypeVal, temp);
    });
};

let ageChangeFunction = function (ageTypeVal, temp) {
    if (ageTypeVal === 'From') {
        let age_end = temp.children().children().children("select[name='age_end']");
        let age_start = temp.children().children().children("select[name='age_start']");
        age_end.parent().css({'visibility': 'visible'});
        age_start.parent().css({'visibility': 'visible'});

    } else if (ageTypeVal === 'Up To') {
        let age_end = temp.children().children().children("select[name='age_end']");
        let age_start = temp.children().children().children("select[name='age_start']");
        age_end.parent().css({'visibility': 'hidden'});
        age_start.parent().css({'visibility': 'visible'});
    }
    else if (ageTypeVal === 'Over') {
        let age_end = temp.children().children().children("select[name='age_end']");
        let age_start = temp.children().children().children("select[name='age_start']");
        age_end.parent().css({'visibility': 'hidden'});
        age_start.parent().css({'visibility': 'visible'});
    }
    else if (ageTypeVal === 'Any') {
        let age_end = temp.children().children().children("select[name='age_end']");
        let age_start = temp.children().children().children("select[name='age_start']");
        age_end.parent().css({'visibility': 'hidden'});
        age_start.parent().css({'visibility': 'hidden'});
    }
    else if (ageTypeVal === 'Adult') {
        let age_end = temp.children().children().children("select[name='age_end']");
        let age_start = temp.children().children().children("select[name='age_start']");
        age_end.parent().css({'visibility': 'hidden'});
        age_start.parent().css({'visibility': 'hidden'});
    }

};

let priceType = function () {

    $("select[name='cost_status']").change(function () {
        let temp = $(this).parent().parent().parent();
        let priceTypeVal = $(this).children(':selected').val();
        priceChangeFunction(priceTypeVal, temp);
    });
};

let priceChangeFunction = function (priceTypeVal, temp) {
    if (priceTypeVal === 'Free') {
        let cost = temp.children().children().children("input[name='cost']");
        let unit = temp.children().children().children("select[name='unit']");
        cost.parent().css({'display': 'none'});
        unit.parent().css({'display': 'none'});

    } else if (priceTypeVal === 'Percentage') {
        let cost = temp.children().children().children("input[name='cost']");
        let unit = temp.children().children().children("select[name='unit']");
        cost.parent().css({'display': 'block'});
        unit.parent().css({'display': 'block'});
    }

};

let multiGenerateFunction = function () {
    $('.multi-field-wrapper').each(function () {
        var $wrapper = $('.multi-fields', this);
        $(".add-field", $(this)).click(function (e) {
            if ($('.multi-field:first-child #id_age_category', $wrapper).data('select2')) {
                $('.multi-field:first-child #id_age_category', $wrapper).select2('destroy');
                $('.multi-field:first-child #id_age_start', $wrapper).select2('destroy');
                $('.multi-field:first-child #id_age_end', $wrapper).select2('destroy');
                $('.multi-field:first-child #id_cost_status', $wrapper).select2('destroy');
                $('.multi-field:first-child #id_unit', $wrapper).select2('destroy');
            }
            $('.multi-field:first-child #id_season_start_date', $wrapper).datepicker('destroy');
            $('.multi-field:first-child #id_season_end_date', $wrapper).datepicker('destroy');
            // if ($('.multi-field:first-child #id_season_start_date', $wrapper).datepicker('myDatePicker')) {
            //     console.log('hey')
            // }
            var a = $('.multi-field:first-child', $wrapper).clone(true);
            a.find('select, input[type="text"], textarea').val("");
            a.find('input[type="checkbox"]').prop('checked', false);
            var i = 0;
            let temp1 = $('.multi-field', $wrapper).length;
            a.find('.customDay').each(function () {
                var customID = 'id_day_' + temp1 + String(i);
                $(this).parent().attr('for', customID);
                $(this).attr('id', customID);
                i++;
            });
            a.find('input[name="DayCount"]').val(0);



            a.find('#id_season_start_date').attr('id', 'start' + temp1);
            a.find('input[name="season_start_date"]').datepicker();
            let prevValStart = $('.multi-field:first-child #id_season_start_date', $wrapper).val();
            $('.multi-field:first-child #id_season_start_date', $wrapper).datepicker();
            $('.multi-field:first-child #id_season_start_date', $wrapper).datepicker("option", "dateFormat", "yy-mm-dd");
            $('.multi-field:first-child #id_season_start_date', $wrapper).val(prevValStart);

            a.find('#id_season_end_date').attr('id', 'end' + temp1);
            a.find('input[name="season_end_date"]').datepicker();
            let prevValEnd = $('.multi-field:first-child #id_season_end_date', $wrapper).val();
            $('.multi-field:first-child #id_season_end_date', $wrapper).datepicker();
            $('.multi-field:first-child #id_season_end_date', $wrapper).datepicker("option", "dateFormat", "yy-mm-dd");
             $('.multi-field:first-child #id_season_end_date', $wrapper).val(prevValEnd);

            a.find('.myDatePicker').datepicker( "option", "dateFormat", "yy-mm-dd" );



            a.find('#id_age_category').select2({width: ' 186.025px'});
            a.find('#id_age_category').val('From').trigger('change.select2');
            $('.multi-field:first-child #id_age_category', $wrapper).select2({width: ' 186.025px'});

            a.find('#id_age_start').select2({width: ' 186.025px'});
            a.find('#id_age_start').val(0).trigger('change.select2');
            $('.multi-field:first-child #id_age_start', $wrapper).select2({width: ' 186.025px'});

            a.find('#id_age_end').select2({width: ' 186.025px'});
            a.find('#id_age_end').val(0).trigger('change.select2');
            $('.multi-field:first-child #id_age_end', $wrapper).select2({width: ' 186.025px'});

            a.find('#id_cost_status').select2({width: ' 186.025px'});
            a.find('#id_cost_status').val('Free').trigger('change.select2');
            $('.multi-field:first-child #id_cost_status', $wrapper).select2({width: ' 186.025px'});

            a.find('#id_unit').select2({width: ' 186.025px'});
            a.find('#id_unit').val('per child per night').trigger('change.select2');
            $('.multi-field:first-child #id_unit', $wrapper).select2({width: ' 186.025px'});
            $wrapper.append(a);
            init(a);
        });

        $('.multi-field .remove-field', $wrapper).click(function () {
            if ($('.multi-field', $wrapper).length > 1)
                $(this).parent('.multi-field').remove();

        });
    });
};

let selectAll = function () {
    $('.select_all').on('click', function () {
        if (this.checked) {
            $(this).parent().parent().parent().parent().children().children().children().children().each(function () {
                this.checked = true;
                $(this).parent().parent().parent().parent().children(':last-child').children().children().val(7);
            });
        } else {
            $(this).parent().parent().parent().parent().children().children().children().children().each(function () {
                this.checked = false;
                $(this).parent().parent().parent().parent().children(':last-child').children().children().val(0);
            });
        }
    });

    $('.customDay').on('click', function () {
        if (this.checked) {
            let a = parseInt($(this).parent().parent().parent().parent().children(':last-child').children().children().val()) + 1;
            $(this).parent().parent().parent().parent().children(':last-child').children().children().val(a);
        } else {
            let a = parseInt($(this).parent().parent().parent().parent().children(':last-child').children().children().val()) - 1;
            $(this).parent().parent().parent().parent().children(':last-child').children().children().val(a);
        }

    })

};