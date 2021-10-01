$(document).ready(() => {
    var discountadult = document.getElementById("priceforadult").value;
    init(discountadult);
});

let init = (discountadult) => {
    if (discountadult) {
        var obj = JSON.parse(discountadult);
        count = Object.keys(obj).length;
        if (count > 0) {
            $('input:radio[name="adult_rate_radio"][value="True"]')
                .attr('checked', true);
            let groupedData = obj.reduce(function (result, current) {
                result[current.plan] = result[current.plan] || [];
                result[current.plan].push(current);
                return result;
            }, {});
            ep_data_array = groupedData['European Plan'];
            parentDiv = PlanTitle(0, 'European Plan');
            PlanRate(ep_data_array, parentDiv);
            bb_data_array = groupedData['Bed and Breakfast Plan'];
            parentDiv = PlanTitle(1, 'Bed and Breakfast Plan');
            PlanRate(bb_data_array, parentDiv);
        } else {
            $('input:radio[name="adult_rate_radio"][value="False"]')
                .attr('checked', true);
        }

    }
};

function PlanTitle(index, title) {
    let $div_id = "adultmax" + index;
    $("#adultdiv").append('<div class="grey-background mb-5" id=' + $div_id + '></div>');
    let plan_title = '<div class="form-group  mt-2">' +
        '<div class="form-row form-row-1 mb-0">' +
        '<label class="remove-label" for="bed_type"' +
        ' style="font-size: 18px; font-family: Proxima-Light;">' + title + '</label>' +
        '</div>' +
        '</div>';
    $('#' + $div_id).append(plan_title);
    return $div_id;
}

function PlanRate(dataArray, parentDiv) {
    $.each(dataArray, function (index, value) {
        var adultname =
            '<div class="form-group">' +
            '<div class="form-row">' +
            '<label>Discount offered when ' + value.adult_max + ' adult comes' + '</label>' +
            '<input style="width:80%"  type="text" class="input-text" value=' + value.rate + '  name=' + value.for + '>' +
            '<span style="padding:10px;">%</span>' +
            '</div>' +
            '</div>';
        $('#' + parentDiv).append(adultname);
    });
}

$("input[name='bb_checkbox'], input[name='ep_checkbox']").on("click", function () {
    $("#false_adult").prop('checked', true);
    $('#adultdiv').children().remove();
    let alert_text = '<div class="form-group  mt-2">' +
        '<div class="form-row mb-0 flashing-div">' +
        '<label class="remove-label " for="bed_type"' +
        ' style="font-size: 15px; font-family: Proxima-Light;">We detected that you have changed the meal plan, so you need to reset the discount offer for minimum adult occupancy.</label>' +
        '</div>' +
        '</div>';
    $('#adultdiv').append(alert_text);
});

$('input[name="adult_max"]').on('input', function (e) {
    $("#false_adult").prop('checked', true);
    $('#adultdiv').children().remove();
    let alert_text = '<div class="form-group  mt-2">' +
        '<div class="form-row mb-0 flashing-div">' +
        '<label class="remove-label" for="bed_type"' +
        ' style="font-size: 15px; font-family: Proxima-Light;">We detected that you have changed the maximum adult capacity, so you need to reset the discount offer for minimum adult occupancy.</label>' +
        '</div>' +
        '</div>';
    $('#adultdiv').append(alert_text);
});

$('input[name="bedandbreakfast_plan"], input[name="european_plan"]').on('input', function (e) {
    $("#false_adult").prop('checked', true);
    $('#adultdiv').children().remove();
    let alert_text = '<div class="form-group  mt-2">' +
        '<div class="form-row mb-0 flashing-div">' +
        '<label class="remove-label" for="bed_type"' +
        ' style="font-size: 15px; font-family: Proxima-Light;">We detected that you have changed the price of meal plan, so you need to reset the discount offer for minimum adult occupancy.</label>' +
        '</div>' +
        '</div>';
    $('#adultdiv').append(alert_text);
});

$(".adult_rate_radio").on("click", function () {
    radio_value = $("input[name='adult_rate_radio']:checked").val();
    showorhide(radio_value);
});

let showorhide = (a) => {
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
                '<div class="form-row form-row-1 mb-0">' +
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
            '<div class="form-row form-row-1 mb-0">' +
            '<label class="remove-label" for="bed_type"' +
            ' style="font-size: 15px; font-family: Proxima-Light;">Please select one meal plan at least.</label>' +
            '</div>' +
            '</div>';
        $('#adultdiv').append(alert_text);
    } else {
        $('#adultdiv').children().remove();
    }
};






