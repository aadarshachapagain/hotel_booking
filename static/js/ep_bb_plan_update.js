$(document).ready(function () {
    $('#ep').show();
    $('#bb').show();

    if (!$('#ep').val())
    {
        $('#ep').val("").hide();
        $('.european_plan_hint').hide();
    }
    else if ($('#ep').val() != "0.00")
    {
        document.getElementById("ep_check").checked = true;
    }
    else{
        $('#ep').val("").hide();
        $('.european_plan_hint').hide();
    }

    if (!$('#bb').val())
    {
        $('#bb').val("").hide();
        $('.bedandbreakfast_plan_hint').hide();
    }
    else if($('#bb').val() != "" )
    {
        document.getElementById("bb_check").checked = true;
    }
    else
    {
        $('#bb').val("").hide();
        $('.bedandbreakfast_plan_hint').hide();
    }

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