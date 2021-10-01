

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

