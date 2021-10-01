final_url = "http://localhost:8000/hotel/payment/dropzoneuploads/";
Dropzone.options.dropZoneForm = {
    url: final_url,
    addRemoveLinks: true,
    method: "post",
    params: 'file_upload',
    maxFilesize: 256 * 4 * 2,
    dictFileTooBig: "File is too big.",
    autoProcessQueue: false,
    acceptedFiles: '.png, .jpg,.gif,.bmp,.jpeg',
    uploadMultiple: true,
    dictDefaultMessage: "Drag and Drop files here to upload",
    parallelUploads: 10,
    maxFiles: 12,
    clickable: true,
    init: function () {
        mydropzone = this;

        $("#submit-all").click(function (evt) {
            evt.preventDefault();
            evt.stopPropagation();
            mydropzone.autoProcessQueue = true;
            mydropzone.processQueue();
            mydropzone.on('sendingmultiple', function (data, xhr, formData) {
                // this will get sent
                {
                    // #formData.append('name', jQuery('#name').val());#
                }

                // this won't -- we don't need this rn, we can just use jQuery
                // var myForm = document.querySelector('form');

                // you are overwriting your formdata here.. remove this
                //formData = new FormData(myForm);

                // instead, just append the form elements to the existing formData
                $("#dropZoneForm").find("input").each(function () {
                    formData.append($(this).attr("name"), $(this).val());
                });
            });
        });
    },
    success: function f() {
        $('.dz-remove').hide();
    },
};