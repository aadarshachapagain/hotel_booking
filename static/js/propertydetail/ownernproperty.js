$('document').ready(function () {
    init();
    blurred_other_company();
    blurred_other_acc();
    assign_value_on_check();
    $('#other_company').click(function () {
        $('#other_company_text').toggle();
    });

    $('#other_acc').click(function () {
        $('#other_acc_text').toggle();
        $('.disable_acc').prop('checked', false);

    });
    // get_old_value_for_update();


});

let init = function () {
    $('#other_company_text').hide();
    $('#other_acc_text').hide();

};

let blurred_other_company = function () {
    $("#other_com").blur(function () {
        company_text = $("#other_com").val();
        company_text = company_text.split('').join('_');
        document.getElementById('other_company').value = company_text;
    });
};

let blurred_other_acc = function () {
    $("#other_acc_text").blur(function () {
        acc_text = $("#other_acc_text").val();
        document.getElementById('other_acc').value = acc_text;
    });
};

let assign_value_on_check = function () {
    $(".assign_value").click(function () {
        stat = $(this).prop("checked");
        if (stat == true) {
            $(this).val('True');
        } else {
            $(this).val('False');
        }
    });
};

let get_old_value_for_update = function () {
    type_of_inc = $('#hidden_type_of_inc').val();
    if (type_of_inc) {
        $("input[name=type_of_inc][value=" + type_of_inc + "]").attr('checked', 'checked');
        company_text = $('#hidden_type_of_inc').val();
        company_text = company_text.split('_').join(' ');
        $('#other_com').val(company_text);
        readly_avail = $('.checktype').prop("checked");
        if (readly_avail == false) {
            $('#other_company').attr('checked', 'checked');
        }
    }
    other_com_checked = $('#other_company').prop("checked");
    if (other_com_checked == true) {
        $('#other_company_text').show();
    }

    prop_history = $('#hidden_prop_history').val();
    if (prop_history) {
        $("input[name=prop_history][value=" + prop_history + "]").prop('checked', true);
    }

    car_rental = $('#hidden_car_rental').val();
    if (car_rental == 'True') {
        $("input[name=car_rental]").attr('checked', 'checked');
        $("input[name=car_rental]").val('True');
    }
    transport_company = $('#hidden_transport_company').val();
    if (transport_company == 'True') {
        $("input[name=transport_company]").attr('checked', 'checked');
        $("input[name=transport_company]").val('True');
    }
    travel_agency = $('#hidden_travel_agency').val();
    if (travel_agency == 'True') {
        $("input[name=travel_agency]").attr('checked', 'checked');
        $("input[name=travel_agency]").val('True');
    }
    food_deliver_agent = $('#hidden_food_deliver_agent').val();
    if (food_deliver_agent == 'True') {
        $("input[name=food_deliver_agent]").attr('checked', 'checked');
        $("input[name=food_deliver_agent]").val('True');
    }
    restaurant_bar_lounge = $('#hidden_restaurant_bar_lounge').val();
    if (restaurant_bar_lounge == 'True') {
        $("input[name=restaurant_bar_lounge]").attr('checked', 'checked');
        $("input[name=restaurant_bar_lounge]").val('True');
    }
    tour_operator = $('#hidden_tour_operator').val();
    if (tour_operator == 'True') {
        $("input[name=tour_operator]").attr('checked', 'checked');
        $("input[name=tour_operator]").val('True');
    }
    ticketing_agent = $('#hidden_ticketing_agent').val();
    if (ticketing_agent == 'True') {
        $("input[name=ticketing_agent]").attr('checked', 'checked');
        $("input[name=ticketing_agent]").val('True');
    }
    travel_agent = $('#hidden_travel_agent').val();
    if (travel_agent == 'True') {
        $("input[name=travel_agent]").attr('checked', 'checked');
        $("input[name=travel_agent]").val('True');
    }
    trekking_company = $('#hidden_trekking_company').val();
    if (travel_agent == 'True') {
        $("input[name=trekking_company]").attr('checked', 'checked');
        $("input[name=trekking_company]").val('True');
    }
    expedition_company = $('#hidden_expedition_company').val();
    if (expedition_company == 'True') {
        $("input[name=expedition_company]").attr('checked', 'checked');
        $("input[name=expedition_company]").val('True');
    }

    accomodation = $('#hidden_accomodations').val();
    clean_data = JSON.parse(accomodation);
    clean_data.forEach(checkaccomodation);
    arr = []
    $("input[name='accomodation']").each(function (index, obj) {
        arr.push($(this).val())
    });
    result = clean_data.diff(arr)
    if (result.length > 0) {
        $('.disable_acc').prop('checked', false);
        $('#other_acc').prop("checked", true);
        $('#other_acc_text').show();
        $('#other_acc_text').val(result);
    }
};

function checkaccomodation(item, index) {
    name_acc = item;
    name_acc = name_acc.split(' ').join('_');
    $("input[name=accomodation][value=" + name_acc + "]").prop('checked', true);
}

Array.prototype.diff = function (a) {
    return this.filter(function (i) {
        return a.indexOf(i) < 0;
    });
};

/*

$('#document').change(function (e) {
    showfilename(e, $(this));
});

$('#id_busn_reg_cert').change(function (e) {
    showfilename(e, $(this));
});

$('#id_busn_lcn_cert').change(function (e) {
    showfilename(e, $(this));
});

$('#id_pan_card_cert').change(function (e) {
    showfilename(e, $(this));
});
$('#id_vat_cert').change(function (e) {
    showfilename(e, $(this));
});

let showfilename = function (e, a) {
    var fileName = e.target.files[0].name;
    htmlstring = `<label>Uploaded File's Name: ${fileName} </label>`;
    $(htmlstring).insertBefore(a.parent().parent());
};
*/

