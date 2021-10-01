$(document).ready(function () {
    initroomfeature();

});


let initroomfeature = function () {
    list_of_selected_name = document.getElementById('features_selected').value;
    if (list_of_selected_name) {
        var parsedobj = JSON.parse(list_of_selected_name);
        parsedobj.forEach(selectroomfeature);
    }

}


function selectroomfeature(item, index) {

    if (document.getElementById(item)) {
        // document.getElementById(item).prop('checked', 'checked');
        id = '#' + item;
        $(id).prop('checked', true);
    }

}