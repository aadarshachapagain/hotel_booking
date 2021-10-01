$(document).ready(function () {
    initprice();
    toggleroompriceinput();
    $(".change_value").hide();
    $(".ratechangeall").hide();
    toggleallinput();

});

let toggleallinput = function () {
    $(".all_inv-inc").click(function () {
        // select-all-inc
        $(".select-all-inc").prop("checked", true);
        $(".ratechangeall").toggle();
        $(".change_value").show();
    });

    $(".all_inv-dec").click(function () {
        // select-all-inc
        $(".select-all-dec").prop("checked", true);
        $(".ratechangeall").toggle();
        $(".change_value").show();
    });

    $('.ratechangeall').keyup(function (e) {
        var txtVal = $(this).val();
        $('.change_value').attr("value", txtVal);


    });

    $(".closeall").click(function () {
        $(".select-all-inc").prop("checked", false);
        $(".select-all-dec").prop("checked", false);
        $(".all_inv-inc").prop("checked", false);
        $(".all_inv-dec").prop("checked", false);
        $(".change_value").hide();
        $(".ratechangeall").hide();
    });


}

let toggleroompriceinput = function () {
    $(".show-input").click(function () {
        numb = this.name;
        array_numb = numb.match(/\d/g);
        group_id = array_numb.join("");
        name_of_input = 'ratechange' + group_id;
        item = document.getElementsByName(name_of_input)[0];
        $(item).toggle();
    });
}

let initprice = function () {
    raw_data = document.getElementById('room_type_list').value;
    clean_data = JSON.parse(raw_data);
    for (i = 0; i < clean_data.length; i++) {
        title = Object.keys(clean_data[i]);
        inv_values = Object.values(clean_data[i]);
        list_items = Object.values(inv_values);
        append_list = [];
        var room_type_id;
        for (j = 0; j < list_items.length; j++) {
            for (k = 0; k < list_items[j].length; k++) {
                append_list.push(`<li>${list_items[j][k]['name']} </li>`);
                room_type_id = list_items[j][k]['room_type_id']
            }
        }
        appenddiv = `<div class="form-group row custom-form-group mt-5"
                         style="border-bottom: 1px solid gainsboro">
                    <div class="form-row form-row-1 " style="width: 36%">
                        <span style="font-family: Proxima-Bold; color: #808080de">
                            ${title}
                         </span>
                     </div>
                    <div class="form-row form-row-1 ">
                                <ul style="list-style: none">
                                <li><span>Increase By&nbsp;</span><input type="radio"  name="altertype${room_type_id}"  class="select_all show-input select-all-inc" value="increase"/><span>&nbsp;&nbsp;&nbsp; Decrease
                                                                By</span> <input name="altertype${room_type_id}" type="radio"  class="select_all show-input select-all-dec" value="decrease"/></li>
                                                            <li><input type="text" class="change_value" name="ratechange${room_type_id}"> </li>
                                        <ul style="list-style: none">
                                            ${append_list.join("")}
                                        </ul>
                                </ul>
                            </div>
                        </div>
                        </div>
                                `
        $('#appendhere').append(appenddiv);

    }
    console.log('clean_data');
    console.log(Object.keys(clean_data[0]));
    console.log(Object.values(clean_data[0]));

}