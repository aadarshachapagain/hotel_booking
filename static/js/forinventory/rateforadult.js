$(".adult_rate_radio").change(function () {
    var adult_low_rate = $('input[name=adult_rate_radio]:checked').val();
    num_adults = document.getElementById('adult_max').value;
    selected_plan_array = [];
    selected_plan_object = {};
    if ($('input[name="ep_checkbox"]').prop('checked') === true) {
        ep_plan_price = $('input[name="european_plan"]').val();
        selected_plan_object =
            {
                value: 'European Plan',
                tag: 'ep'
            };
        selected_plan_array.push(selected_plan_object);
    }
    if ($('input[name="bb_checkbox"]').prop('checked') === true) {
        bb_plan_price = $('input[name="bedandbreakfast_plan"]').val();
        // selected_plan_array.push('Bed and Breakfast Plan');
        selected_plan_object =
            {
                value: 'Bed and Breakfast Plan',
                tag: 'bb'
            };
        selected_plan_array.push(selected_plan_object);
    }
    changeadult_max = num_adults;
    if (selected_plan_array.length !== 0) {
        if (num_adults > 1) {
            if (adult_low_rate === 'True') {
                $.each(selected_plan_array, function (index, value) {
                    let $div_id = "adultmax" + index;
                    $("#adultdiv").append('<div class="grey-background mb-5" id=' + $div_id + '></div>');
                    let plan_title = '<div class="form-group  mt-2">' +
                        '<div class="form-row form-row-1 mb-0">' +
                        '<label class="remove-label" for="bed_type"' +
                        ' style="font-size: 18px; font-family: Proxima-Light;">' + value.value + '</label>' +
                        '</div>' +
                        '</div>';
                    $('#' + $div_id).append(plan_title);
                    for (let j = 0; j < num_adults - 1; j++) {
                        var adultname =
                            '<div class="form-group">' +
                            '<div class="form-row">' +
                            '<label>Discount offered when ' + (num_adults - j - 1) + ' adult comes' + '</label>' +
                            '<input style="width:80%"  type="text" class="input-text"  name=adult' + j + '-' + value.tag + '>' +
                            '<span style="padding:10px;">%</span>' +
                            '</div>' +
                            '</div>';
                        changeadult_max -= 1;
                        $('#' + $div_id).append(adultname);
                    }
                });
                } else {
                    $('#adultdiv').children().remove();
                    // $('#' + $div_id).remove();
                }

        } else if (num_adults === '1' && adult_low_rate === 'True') {
            let alert_text = '<div class="form-group  mt-2">' +
                '<div class="form-row form-row-1 mb-0">' +
                '<label class="remove-label" for="bed_type"' +
                ' style="font-size: 15px; font-family: Proxima-Light;">Maximum adult count is 1 so this offer is not available..</label>' +
                '</div>' +
                '</div>';
            $('#adultdiv').append(alert_text);
        } else if (!num_adults && adult_low_rate === 'True') {
            let alert_text = '<div class="form-group  mt-2">' +
                '<div class="form-row form-row-1 flashing-div mb-0">' +
                '<label class="remove-label" for="bed_type"' +
                ' style="font-size: 15px; font-family: Proxima-Light;">Please enter max adult occupancy at first.</label>' +
                '</div>' +
                '</div>';
            $('#adultdiv').append(alert_text);
        } else {
            $('#adultdiv').children().remove();
        }
    } else if (selected_plan_array.length === 0 && adult_low_rate === 'True') {
        let alert_text = '<div class="form-group  mt-2">' +
            '<div class="form-row form-row-1 flashing-div mb-0">' +
            '<label class="remove-label" for="bed_type"' +
            ' style="font-size: 15px; font-family: Proxima-Light;">Please select at least one meal plan .</label>' +
            '</div>' +
            '</div>';
        $('#adultdiv').append(alert_text);
    } else {
        $('#adultdiv').children().remove();
    }
});

$("input[name='bb_checkbox'], input[name='ep_checkbox']").on("click", function () {
    var adult_low_rate = $('input[name=adult_rate_radio]:checked').val();
    if (adult_low_rate === 'True') {
        $("#false_adult").prop('checked', true);
        $('#adultdiv').children().remove();
        let alert_text = '<div class="form-group  mt-2">' +
            '<div class="form-row mb-0 flashing-div">' +
            '<label class="remove-label " for="bed_type"' +
            ' style="font-size: 15px; font-family: Proxima-Light;">We detected that you have changed the meal plan, so you need to reset the discount offer for minimum adult occupancy.</label>' +
            '</div>' +
            '</div>';
        $('#adultdiv').append(alert_text);
    }
});

$('input[name="adult_max"]').on('input', function (e) {
    var adult_low_rate = $('input[name=adult_rate_radio]:checked').val();
    if (adult_low_rate === 'True') {
        $("#false_adult").prop('checked', true);
        $('#adultdiv').children().remove();
        let alert_text = '<div class="form-group  mt-2">' +
            '<div class="form-row mb-0 flashing-div">' +
            '<label class="remove-label" for="bed_type"' +
            ' style="font-size: 15px; font-family: Proxima-Light;">We detected that you have changed the maximum adult capacity, so you need to reset the discount offer for minimum adult occupancy.</label>' +
            '</div>' +
            '</div>';
        $('#adultdiv').append(alert_text);
    }
});

$('input[name="bedandbreakfast_plan"], input[name="european_plan"]').on('input', function (e) {
    var adult_low_rate = $('input[name=adult_rate_radio]:checked').val();
    if (adult_low_rate === 'True') {
        $("#false_adult").prop('checked', true);
        $('#adultdiv').children().remove();
        let alert_text = '<div class="form-group  mt-2">' +
            '<div class="form-row mb-0 flashing-div">' +
            '<label class="remove-label" for="bed_type"' +
            ' style="font-size: 15px; font-family: Proxima-Light;">We detected that you have changed the price of meal plan, so you need to reset the discount offer for minimum adult occupancy.</label>' +
            '</div>' +
            '</div>';
        $('#adultdiv').append(alert_text);
    }
});