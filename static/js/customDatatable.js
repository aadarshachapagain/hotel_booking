$(document).ready(function () {
    let example = $('#datatable').DataTable({
        state: true,
        responsive: true,
        columnDefs: [
            {
                targets: 1,
                orderable: false,
                sortable: false,
                className: 'select-checkbox',
            }
        ],
        select: {
            style: 'multi',
            selector: 'td:nth-child(2)'
        },
        order: [[1, 'asc']],
    });
    example.on("click", "th.select-checkbox", function () {

        if ($("th.select-checkbox").hasClass("selected")) {
            example.rows().deselect();
            $("th.select-checkbox").removeClass("selected");
        } else {
            example.rows().select();
            $("th.select-checkbox").addClass("selected");
        }
    }).on("select deselect", function () {
        ("Some selection or deselection going on");
        if (example.rows({
            selected: true
        }).count() !== example.rows().count()) {
            $("th.select-checkbox").removeClass("selected");
        } else {
            $("th.select-checkbox").addClass("selected");
        }
    });
});