$(document).ready(function () {
    init();


});

let init = function () {
    list_of_selected_name_amenities = document.getElementById('amenities_selected').value;
    // var parsedobj = JSON.parse(list_of_selected_name);
    if (list_of_selected_name_amenities) {
        var parsedobjamenities = JSON.parse(list_of_selected_name_amenities);
        parsedobjamenities.forEach(selectamenity);
    }


}

function selectamenity(item, index) {

    if (document.getElementById(item)) {
        // document.getElementById(item).prop('checked', 'checked');
        id = '#' + item;
        $(id).prop('checked', true);
    }

}

$(".select_all").on('click', function () {
    if ($(this).prop("checked") == true) {
        $(this).parent().nextAll().find("input[type='checkbox']").prop('checked', true);
    }
    if ($(this).prop("checked") == false) {
        $(this).parent().nextAll().find("input[type='checkbox']").prop('checked', false);
    }

});