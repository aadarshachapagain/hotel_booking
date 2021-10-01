$(document).ready(function () {
    multiGenerateFunction();
});
let multiGenerateFunction = function () {
    $('.multi-field-wrapper').each(function () {
        var $wrapper = $('.multi-fields', this);
        $(".add-field", $(this)).click(function (e) {
            if ($('.multi-field:first-child #id_other_systems', $wrapper).data('select2')) {
                $('.multi-field:first-child #id_other_systems', $wrapper).select2('destroy');
                $('.multi-field:first-child #id_meal_plans', $wrapper).select2('destroy');

            }

            var a = $('.multi-field:first-child', $wrapper).clone(true);
            a.find('select, select, input').val("");
            other_sys_element = $('#id_other_systems');
            sysvalue = (other_sys_element[0].childNodes[3].value);
            other_meal_element = $('#id_meal_plans');
            mealvalue = (other_meal_element[0].childNodes[3].value);

            a.find('#id_other_systems').select2({width: ' 186.025px'});
            a.find('#id_other_systems').val(sysvalue).trigger('change.select2');
            $('.multi-field:first-child #id_other_systems', $wrapper).select2({width: ' 186.025px'});

            a.find('#id_meal_plans').select2({width: ' 186.025px'});
            a.find('#id_meal_plans').val(mealvalue).trigger('change.select2');
            $('.multi-field:first-child #id_meal_plans', $wrapper).select2({width: ' 186.025px'});

            a.find('#id_unit').select2({width: ' 186.025px'});
            a.find('#id_unit').val('per child per night').trigger('change.select2');
            $('.multi-field:first-child #id_unit', $wrapper).select2({width: ' 186.025px'});
            $wrapper.append(a);
        });

        $('.multi-field .remove-field', $wrapper).click(function () {
            if ($('.multi-field', $wrapper).length > 1)
                $(this).parent('.multi-field').remove();

        });
    });
};

$(".adult_rate_radio").change(function () {
    var adult_low_rate = $('input[name=adult_rate_radio]:checked').val();
    num_adults = document.getElementById('adult_max').value;
    changeadult_max = num_adults;
    if (num_adults) {
        if (adult_low_rate == 'True') {
            $("#adultdiv").append('<div id="adultmax"></div>');
            for (j = 0; j < num_adults - 1; j++) {
                var adultname = '<div class="form-row form-row-1"><label>Discount Offered when ' + (num_adults - j - 1) + ' adult comes' + '</label><input style="width:60%"  type="text" class="input-text"  name=adult' + j + '><span style="padding:10px;">%</span></div>'
                changeadult_max -= 1;
                $("#adultmax").append(adultname);
            }
        }
        else {
            $("#adultmax").remove();
        }
    }
});