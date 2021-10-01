$(document).ready(function () {
    hidden_ammenities = document.getElementById('hidden_amenities_type').value;

    if (hidden_ammenities == 'False') {
        $('#amenities_type [value=False]').attr('selected', 'true');
    } else {
        $('#amenities_type [value=True]').attr('selected', 'true');
    }

});