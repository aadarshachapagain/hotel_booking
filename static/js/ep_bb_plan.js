$(document).ready(function () {
    $('#ep').hide();
    $('#bb').hide();
    $('.bedandbreakfast_plan_hint').hide();
    $('.european_plan_hint').hide();
});

$(document).ready(function () {
    $('#ep_check').on('click', function () {
        if (this.checked) {
            $('#ep').show();
            $('.european_plan_hint').show();

        } else {
            $('#ep').val("").hide();
            $('.european_plan_hint').hide();
        }

    })
});

$(document).ready(function () {
    $('#bb_check').on('click', function () {
        if (this.checked) {
            $('#bb').show();
            $('.bedandbreakfast_plan_hint').show();
        } else
        {
            $('#bb').val("").hide();
            $('.bedandbreakfast_plan_hint').hide();
        }

    })
});
