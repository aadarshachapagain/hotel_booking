$(document).ready(function () {
    $(".myselect").select2(
        {
            placeholder: "Select",
            closeOnSelect: true,
            // sorter: data => data.sort((a, b) => a.text.localeCompare(b.text)),
        });

});